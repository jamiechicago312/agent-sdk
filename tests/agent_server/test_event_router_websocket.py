"""Tests for websocket functionality in event_router.py"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest
from fastapi import WebSocketDisconnect

from openhands.agent_server.event_service import EventService
from openhands.agent_server.sockets import _WebSocketSubscriber
from openhands.sdk import Message
from openhands.sdk.event.llm_convertible import MessageEvent
from openhands.sdk.llm.message import TextContent


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket for testing."""
    websocket = MagicMock()
    websocket.accept = AsyncMock()
    websocket.receive_json = AsyncMock()
    websocket.send_json = AsyncMock()
    websocket.close = AsyncMock()
    websocket.application_state = MagicMock()
    return websocket


@pytest.fixture
def mock_event_service():
    """Create a mock EventService for testing."""
    service = MagicMock(spec=EventService)
    service.subscribe_to_events = AsyncMock(return_value=uuid4())
    service.unsubscribe_from_events = AsyncMock(return_value=True)
    service.send_message = AsyncMock()
    service.search_events = AsyncMock()
    return service


@pytest.fixture
def sample_conversation_id():
    """Return a sample conversation ID."""
    return uuid4()


class TestWebSocketSubscriber:
    """Test cases for _WebSocketSubscriber class."""

    @pytest.mark.asyncio
    async def test_websocket_subscriber_call_success(self, mock_websocket):
        """Test successful event sending through WebSocket subscriber."""
        subscriber = _WebSocketSubscriber(websocket=mock_websocket)
        event = MessageEvent(
            id="test_event",
            source="user",
            llm_message=Message(role="user", content=[TextContent(text="test")]),
        )

        await subscriber(event)

        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["id"] == "test_event"

    @pytest.mark.asyncio
    async def test_websocket_subscriber_call_exception(self, mock_websocket):
        """Test exception handling in WebSocket subscriber."""
        mock_websocket.send_json.side_effect = Exception("Connection error")
        subscriber = _WebSocketSubscriber(websocket=mock_websocket)
        event = MessageEvent(
            id="test_event",
            source="user",
            llm_message=Message(role="user", content=[TextContent(text="test")]),
        )

        # Should not raise exception, just log it
        await subscriber(event)

        mock_websocket.send_json.assert_called_once()


class TestWebSocketDisconnectHandling:
    """Test cases for WebSocket disconnect handling in the socket endpoint."""

    @pytest.mark.asyncio
    async def test_websocket_disconnect_breaks_loop(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that WebSocketDisconnect exception breaks the loop."""
        # Setup mock to raise WebSocketDisconnect on first receive_json call
        mock_websocket.receive_json.side_effect = WebSocketDisconnect()

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            # Mock config to not require authentication
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            # Import and call the socket function directly
            from openhands.agent_server.sockets import events_socket

            # This should not hang or loop infinitely
            await events_socket(
                sample_conversation_id, mock_websocket, session_api_key=None
            )

        # Verify that unsubscribe was called
        mock_event_service.unsubscribe_from_events.assert_called()

    @pytest.mark.asyncio
    async def test_websocket_no_double_unsubscription(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that unsubscription only happens once even with disconnect."""
        subscriber_id = uuid4()
        mock_event_service.subscribe_to_events.return_value = subscriber_id
        mock_websocket.receive_json.side_effect = WebSocketDisconnect()

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            # Mock config to not require authentication
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            await events_socket(
                sample_conversation_id, mock_websocket, session_api_key=None
            )

        # Should be called exactly once (not in both except and finally blocks)
        assert mock_event_service.unsubscribe_from_events.call_count == 1
        mock_event_service.unsubscribe_from_events.assert_called_with(subscriber_id)

    @pytest.mark.asyncio
    async def test_websocket_general_exception_continues_loop(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that general exceptions don't break the loop immediately."""
        call_count = 0

        def side_effect():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise ValueError("Some error")
            elif call_count == 2:
                raise WebSocketDisconnect()  # This should break the loop

        mock_websocket.receive_json.side_effect = side_effect

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            # Mock config to not require authentication
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            await events_socket(
                sample_conversation_id, mock_websocket, session_api_key=None
            )

        # Should have been called twice (once for ValueError, once for disconnect)
        assert mock_websocket.receive_json.call_count == 2
        mock_event_service.unsubscribe_from_events.assert_called_once()

    @pytest.mark.asyncio
    async def test_websocket_successful_message_processing(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test successful message processing before disconnect."""
        message_data = {"role": "user", "content": "Hello"}
        call_count = 0

        def side_effect():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return message_data
            else:
                raise WebSocketDisconnect()

        mock_websocket.receive_json.side_effect = side_effect

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            # Mock config to not require authentication
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            await events_socket(
                sample_conversation_id, mock_websocket, session_api_key=None
            )

        # Should have processed the message
        mock_event_service.send_message.assert_called_once()
        args, kwargs = mock_event_service.send_message.call_args
        message = args[0]
        assert message.role == "user"
        assert len(message.content) == 1
        assert message.content[0].text == "Hello"
        # send_message only takes a message parameter, no run parameter

    @pytest.mark.asyncio
    async def test_websocket_unsubscribe_in_finally_when_no_disconnect(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that unsubscription happens in finally block when no disconnect."""
        # Simulate a different kind of exception that doesn't trigger disconnect handler
        mock_websocket.receive_json.side_effect = RuntimeError("Unexpected error")

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            # Mock config to not require authentication
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            # This should raise the RuntimeError but still clean up
            with pytest.raises(RuntimeError):
                await events_socket(
                    sample_conversation_id, mock_websocket, session_api_key=None
                )

        # Should still unsubscribe in the finally block
        mock_event_service.unsubscribe_from_events.assert_called_once()


class TestResendAllFunctionality:
    """Test cases for resend_all parameter functionality."""

    @pytest.mark.asyncio
    async def test_resend_all_false_no_resend(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that resend_all=False doesn't trigger event resend."""
        mock_websocket.receive_json.side_effect = WebSocketDisconnect()

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            await events_socket(
                sample_conversation_id,
                mock_websocket,
                session_api_key=None,
                resend_all=False,
            )

        # search_events should not be called when not resending
        mock_event_service.search_events.assert_not_called()

    @pytest.mark.asyncio
    async def test_resend_all_true_resends_events(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that resend_all=True resends all existing events."""
        # Create mock events to resend
        mock_events = [
            MessageEvent(
                id="event1",
                source="user",
                llm_message=Message(role="user", content=[TextContent(text="Hello")]),
            ),
            MessageEvent(
                id="event2",
                source="agent",
                llm_message=Message(role="assistant", content=[TextContent(text="Hi")]),
            ),
        ]

        from typing import cast

        from openhands.agent_server.models import EventPage
        from openhands.sdk.event import Event

        mock_event_page = EventPage(
            items=cast(list[Event], mock_events), next_page_id=None
        )
        mock_event_service.search_events = AsyncMock(return_value=mock_event_page)
        mock_websocket.receive_json.side_effect = WebSocketDisconnect()

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            await events_socket(
                sample_conversation_id,
                mock_websocket,
                session_api_key=None,
                resend_all=True,
            )

        # search_events should be called to get all events
        mock_event_service.search_events.assert_called_once_with(page_id=None)

        # All events should be sent through websocket
        assert mock_websocket.send_json.call_count == 2
        sent_events = [call[0][0] for call in mock_websocket.send_json.call_args_list]
        assert sent_events[0]["id"] == "event1"
        assert sent_events[1]["id"] == "event2"

    @pytest.mark.asyncio
    async def test_resend_all_handles_search_events_exception(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that exceptions during search_events cause the WebSocket to fail."""
        mock_event_service.search_events = AsyncMock(
            side_effect=Exception("Search failed")
        )

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            # Should raise the exception from search_events
            with pytest.raises(Exception, match="Search failed"):
                await events_socket(
                    sample_conversation_id,
                    mock_websocket,
                    session_api_key=None,
                    resend_all=True,
                )

        # search_events should be called
        mock_event_service.search_events.assert_called_once()
        # WebSocket should be subscribed but then unsubscribed due to exception
        mock_event_service.subscribe_to_events.assert_called_once()
        mock_event_service.unsubscribe_from_events.assert_called_once()

    @pytest.mark.asyncio
    async def test_resend_all_handles_send_json_exception(
        self, mock_websocket, mock_event_service, sample_conversation_id
    ):
        """Test that exceptions during send_json are handled gracefully."""
        # Create mock events to resend
        mock_events = [
            MessageEvent(
                id="event1",
                source="user",
                llm_message=Message(role="user", content=[TextContent(text="Hello")]),
            ),
        ]

        from typing import cast

        from openhands.agent_server.models import EventPage
        from openhands.sdk.event import Event

        mock_event_page = EventPage(
            items=cast(list[Event], mock_events), next_page_id=None
        )
        mock_event_service.search_events = AsyncMock(return_value=mock_event_page)

        # Make send_json fail during resend
        mock_websocket.send_json.side_effect = Exception("Send failed")
        mock_websocket.receive_json.side_effect = WebSocketDisconnect()

        with (
            patch(
                "openhands.agent_server.sockets.conversation_service"
            ) as mock_conv_service,
            patch("openhands.agent_server.sockets.get_default_config") as mock_config,
        ):
            mock_config.return_value.session_api_keys = None
            mock_conv_service.get_event_service = AsyncMock(
                return_value=mock_event_service
            )

            from openhands.agent_server.sockets import events_socket

            # Should not raise exception, should handle gracefully
            await events_socket(
                sample_conversation_id,
                mock_websocket,
                session_api_key=None,
                resend_all=True,
            )

        # search_events should be called
        mock_event_service.search_events.assert_called_once()
        # send_json should be called (and fail)
        mock_websocket.send_json.assert_called_once()
        # WebSocket should still be subscribed and unsubscribed normally
        mock_event_service.subscribe_to_events.assert_called_once()
        mock_event_service.unsubscribe_from_events.assert_called_once()
