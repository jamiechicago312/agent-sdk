"""Tests for MCP tool functionality with new simplified implementation."""

from unittest.mock import MagicMock

import mcp.types

from openhands.sdk.llm import TextContent
from openhands.sdk.mcp.client import MCPClient
from openhands.sdk.mcp.definition import MCPToolObservation
from openhands.sdk.mcp.tool import MCPToolDefinition, MCPToolExecutor
from openhands.sdk.tool import ToolAnnotations


class MockMCPClient(MCPClient):
    """Mock MCPClient for testing that bypasses the complex constructor."""

    def __init__(self):
        # Skip the parent constructor to avoid needing transport
        pass


class TestMCPToolObservation:
    """Test MCPToolObservation functionality."""

    def test_from_call_tool_result_success(self):
        """Test creating observation from successful MCP result."""
        # Create mock MCP result
        result = MagicMock(spec=mcp.types.CallToolResult)
        result.content = [
            mcp.types.TextContent(type="text", text="Operation completed successfully")
        ]
        result.isError = False

        observation = MCPToolObservation.from_call_tool_result(
            tool_name="test_tool", result=result
        )

        assert observation.tool_name == "test_tool"
        assert len(observation.content) == 1
        assert isinstance(observation.content[0], TextContent)
        assert observation.content[0].text == "Operation completed successfully"
        assert observation.is_error is False

    def test_from_call_tool_result_error(self):
        """Test creating observation from error MCP result."""
        # Create mock MCP result
        result = MagicMock(spec=mcp.types.CallToolResult)
        result.content = [mcp.types.TextContent(type="text", text="Operation failed")]
        result.isError = True

        observation = MCPToolObservation.from_call_tool_result(
            tool_name="test_tool", result=result
        )

        assert observation.tool_name == "test_tool"
        assert len(observation.content) == 1
        assert isinstance(observation.content[0], TextContent)
        assert observation.content[0].text == "Operation failed"
        assert observation.is_error is True

    def test_from_call_tool_result_with_image(self):
        """Test creating observation from MCP result with image content."""
        # Create mock MCP result with image
        result = MagicMock(spec=mcp.types.CallToolResult)
        result.content = [
            mcp.types.TextContent(type="text", text="Here's the image:"),
            mcp.types.ImageContent(
                type="image", data="base64data", mimeType="image/png"
            ),
        ]
        result.isError = False

        observation = MCPToolObservation.from_call_tool_result(
            tool_name="test_tool", result=result
        )

        assert observation.tool_name == "test_tool"
        assert len(observation.content) == 2
        assert isinstance(observation.content[0], TextContent)
        assert observation.content[0].text == "Here's the image:"
        # Second content should be ImageContent
        assert hasattr(observation.content[1], "image_urls")
        assert observation.is_error is False

    def test_to_llm_content_success(self):
        """Test agent observation formatting for success."""
        observation = MCPToolObservation(
            tool_name="test_tool",
            content=[TextContent(text="Success result")],
            is_error=False,
        )

        agent_obs = observation.to_llm_content
        assert len(agent_obs) == 2
        assert isinstance(agent_obs[0], TextContent)
        assert "[Tool 'test_tool' executed.]" in agent_obs[0].text
        assert "[An error occurred during execution.]" not in agent_obs[0].text
        assert isinstance(agent_obs[1], TextContent)
        assert agent_obs[1].text == "Success result"

    def test_to_llm_content_error(self):
        """Test agent observation formatting for error."""
        observation = MCPToolObservation(
            tool_name="test_tool",
            content=[TextContent(text="Error occurred")],
            is_error=True,
        )

        agent_obs = observation.to_llm_content
        assert len(agent_obs) == 2
        assert isinstance(agent_obs[0], TextContent)
        assert isinstance(agent_obs[1], TextContent)
        assert "[Tool 'test_tool' executed.]" in agent_obs[0].text
        assert "[An error occurred during execution.]" in agent_obs[0].text
        assert agent_obs[1].text == "Error occurred"


class TestMCPToolExecutor:
    """Test MCPToolExecutor functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_client = MagicMock()
        self.executor = MCPToolExecutor(tool_name="test_tool", client=self.mock_client)

    def test_call_tool_success(self):
        """Test successful tool execution."""
        # Mock successful MCP call
        mock_result = MagicMock(spec=mcp.types.CallToolResult)
        mock_result.content = [
            mcp.types.TextContent(type="text", text="Success result")
        ]
        mock_result.isError = False

        # Mock action
        mock_action = MagicMock()
        mock_action.model_dump.return_value = {"param": "value"}

        # Mock call_async_from_sync to return the expected observation
        def mock_call_async_from_sync(coro_func, **kwargs):
            return MCPToolObservation.from_call_tool_result(
                tool_name="test_tool", result=mock_result
            )

        self.mock_client.call_async_from_sync = mock_call_async_from_sync

        observation = self.executor(mock_action)

        assert isinstance(observation, MCPToolObservation)
        assert observation.tool_name == "test_tool"
        assert observation.is_error is False

    def test_call_tool_error(self):
        """Test tool execution with error."""
        # Mock error MCP call
        mock_result = MagicMock(spec=mcp.types.CallToolResult)
        mock_result.content = [
            mcp.types.TextContent(type="text", text="Error occurred")
        ]
        mock_result.isError = True

        # Mock action
        mock_action = MagicMock()
        mock_action.model_dump.return_value = {"param": "value"}

        # Mock call_async_from_sync to return the expected observation
        def mock_call_async_from_sync(coro_func, **kwargs):
            return MCPToolObservation.from_call_tool_result(
                tool_name="test_tool", result=mock_result
            )

        self.mock_client.call_async_from_sync = mock_call_async_from_sync

        observation = self.executor(mock_action)

        assert isinstance(observation, MCPToolObservation)
        assert observation.tool_name == "test_tool"
        assert observation.is_error is True

    def test_call_tool_exception(self):
        """Test tool execution with exception."""
        # Mock action
        mock_action = MagicMock()
        mock_action.model_dump.return_value = {"param": "value"}

        # Mock call_async_from_sync to return an error observation
        def mock_call_async_from_sync(coro_func, **kwargs):
            return MCPToolObservation(
                content=[
                    TextContent(
                        text="Error calling MCP tool test_tool: Connection failed"
                    )
                ],
                is_error=True,
                tool_name="test_tool",
            )

        self.mock_client.call_async_from_sync = mock_call_async_from_sync

        observation = self.executor(mock_action)

        assert isinstance(observation, MCPToolObservation)
        assert isinstance(observation.content[0], TextContent)
        assert observation.tool_name == "test_tool"
        assert observation.is_error is True
        assert "Connection failed" in observation.content[0].text


class TestMCPTool:
    """Test MCPTool functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_client = MockMCPClient()

        # Create mock MCP tool
        self.mock_mcp_tool = MagicMock(spec=mcp.types.Tool)
        self.mock_mcp_tool.name = "test_tool"
        self.mock_mcp_tool.description = "A test tool"
        self.mock_mcp_tool.inputSchema = {
            "type": "object",
            "properties": {"param": {"type": "string"}},
        }
        self.mock_mcp_tool.annotations = None
        self.mock_mcp_tool.meta = None

        tools = MCPToolDefinition.create(
            mcp_tool=self.mock_mcp_tool, mcp_client=self.mock_client
        )
        self.tool = tools[0]  # Extract single tool from sequence

    def test_mcp_tool_creation(self):
        """Test creating an MCP tool."""
        assert self.tool.name == "test_tool"
        assert self.tool.description == "A test tool"

        # Get the schema from the OpenAI tool since MCPToolAction now uses dynamic
        # schema
        openai_tool = self.tool.to_openai_tool()
        function_def = openai_tool["function"]
        assert "parameters" in function_def
        input_schema = function_def["parameters"]

        # Since security_risk was removed from Action, it should not be in schema
        assert len(input_schema["properties"]) == 1
        assert "security_risk" not in input_schema["properties"]

        assert input_schema == {
            "type": "object",
            "properties": {"param": {"type": "string"}},
        }

    def test_mcp_tool_with_annotations(self):
        """Test creating an MCP tool with annotations."""
        # Mock tool with annotations
        mock_tool_with_annotations = MagicMock(spec=mcp.types.Tool)
        mock_tool_with_annotations.name = "annotated_tool"
        mock_tool_with_annotations.description = "Tool with annotations"
        mock_tool_with_annotations.inputSchema = {"type": "object"}
        mock_tool_with_annotations.annotations = ToolAnnotations(title="Annotated Tool")
        mock_tool_with_annotations.meta = {"version": "1.0"}

        tools = MCPToolDefinition.create(
            mcp_tool=mock_tool_with_annotations, mcp_client=self.mock_client
        )
        tool = tools[0]  # Extract single tool from sequence

        assert tool.name == "annotated_tool"
        assert tool.description == "Tool with annotations"
        assert tool.annotations is not None

    def test_mcp_tool_no_description(self):
        """Test creating an MCP tool without description."""
        # Mock tool without description
        mock_tool_no_desc = MagicMock(spec=mcp.types.Tool)
        mock_tool_no_desc.name = "no_desc_tool"
        mock_tool_no_desc.description = None
        mock_tool_no_desc.inputSchema = {"type": "object"}
        mock_tool_no_desc.annotations = None
        mock_tool_no_desc.meta = None

        tools = MCPToolDefinition.create(
            mcp_tool=mock_tool_no_desc, mcp_client=self.mock_client
        )
        tool = tools[0]  # Extract single tool from sequence

        assert tool.name == "no_desc_tool"
        assert tool.description == "No description provided"

    def test_executor_assignment(self):
        """Test that the tool has the correct executor."""
        assert isinstance(self.tool.executor, MCPToolExecutor)
        assert self.tool.executor.tool_name == "test_tool"
        assert self.tool.executor.client == self.mock_client
