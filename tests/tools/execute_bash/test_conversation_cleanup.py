"""
Tests for proper cleanup of tool executors in conversations.

This test suite verifies that tool executors are properly cleaned up
when conversations are closed or destroyed.
"""

import tempfile
from unittest.mock import Mock

from openhands.sdk import Agent, Conversation
from openhands.sdk.tool import Tool, register_tool
from openhands.tools.execute_bash import BashExecutor, BashTool


def test_conversation_close_calls_executor_close(mock_llm):
    """Test that Conversation.close() calls close() on all tool executors."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a BashExecutor with subprocess terminal to avoid tmux issues
        bash_executor = BashExecutor(working_dir=temp_dir, terminal_type="subprocess")
        bash_executor.close = Mock()

        def _make_tool(conv_state, **params):
            tools = BashTool.create(conv_state)
            tool = tools[0]
            return [tool.model_copy(update={"executor": bash_executor})]

        register_tool("test_execute_bash", _make_tool)

        # Create agent and conversation
        agent = Agent(
            llm=mock_llm,
            tools=[Tool(name="test_execute_bash")],
        )
        conversation = Conversation(agent=agent, workspace=temp_dir)

        # Close the conversation
        conversation.close()

        # Verify that the executor's close method was called
        bash_executor.close.assert_called_once()


def test_conversation_del_calls_close(mock_llm):
    """Test that Conversation.__del__() calls close()."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a BashExecutor with subprocess terminal to avoid tmux issues
        bash_executor = BashExecutor(working_dir=temp_dir, terminal_type="subprocess")
        bash_executor.close = Mock()

        def _make_tool(conv_state, **params):
            tools = BashTool.create(conv_state)
            tool = tools[0]
            return [tool.model_copy(update={"executor": bash_executor})]

        register_tool("test_execute_bash", _make_tool)

        # Create agent and conversation
        agent = Agent(
            llm=mock_llm,
            tools=[Tool(name="test_execute_bash")],
        )
        conversation = Conversation(agent=agent, workspace=temp_dir)

        # Manually call __del__ to simulate garbage collection
        conversation.__del__()

        # Verify that the executor's close method was called
        bash_executor.close.assert_called_once()


def test_conversation_close_handles_executor_exceptions(mock_llm):
    """Test that Conversation.close() handles exceptions from executor.close()."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a mock LLM to avoid actual API calls

        # Create a BashExecutor with subprocess terminal and make its close method
        # raise an exception
        bash_executor = BashExecutor(working_dir=temp_dir, terminal_type="subprocess")
        bash_executor.close = Mock(side_effect=Exception("Test exception"))

        def _make_tool(conv_state, **params):
            tools = BashTool.create(conv_state)
            tool = tools[0]
            return [tool.model_copy(update={"executor": bash_executor})]

        register_tool("test_execute_bash", _make_tool)

        # Create agent and conversation
        agent = Agent(
            llm=mock_llm,
            tools=[Tool(name="test_execute_bash")],
        )
        conversation = Conversation(agent=agent, workspace=temp_dir)

        # Close should not raise an exception even if executor.close() fails
        # We can see from the captured stderr that the warning is logged correctly
        conversation.close()  # This should not raise an exception


def test_conversation_close_skips_none_executors(mock_llm):
    """Test that Conversation.close() skips tools with None executors."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a mock LLM to avoid actual API calls

        # Create a tool with no executor
        register_tool(
            "test_execute_bash",
            lambda conv_state, **params: [
                BashTool.create(conv_state)[0].model_copy(update={"executor": None})
            ],
        )

        # Create agent and conversation
        agent = Agent(
            llm=mock_llm,
            tools=[Tool(name="test_execute_bash")],
        )
        conversation = Conversation(agent=agent, workspace=temp_dir)

        # This should not raise an exception
        conversation.close()


def test_bash_executor_close_calls_session_close():
    """Test that BashExecutor.close() calls session.close()."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a BashExecutor with subprocess terminal
        bash_executor = BashExecutor(working_dir=temp_dir, terminal_type="subprocess")

        # Mock the session's close method
        bash_executor.session.close = Mock()

        # Call close on the executor
        bash_executor.close()

        # Verify that session.close() was called
        bash_executor.session.close.assert_called_once()


def test_bash_executor_close_handles_missing_session():
    """Test that BashExecutor.close() handles missing session attribute."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a BashExecutor with subprocess terminal
        bash_executor = BashExecutor(working_dir=temp_dir, terminal_type="subprocess")

        # Remove the session attribute
        delattr(bash_executor, "session")

        # This should not raise an exception
        bash_executor.close()
