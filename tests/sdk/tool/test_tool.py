"""Test Tool class functionality."""

import pytest
from pydantic import ValidationError

from openhands.sdk.tool.spec import Tool


def test_tool_minimal():
    """Test creating Tool with minimal required fields."""
    tool = Tool(name="TestTool")

    assert tool.name == "TestTool"
    assert tool.params == {}


def test_tool_with_params():
    """Test creating Tool with parameters."""
    params = {"working_dir": "/workspace", "timeout": 30}
    tool = Tool(name="TestTool", params=params)

    assert tool.name == "TestTool"
    assert tool.params == params


def test_tool_complex_params():
    """Test creating Tool with complex parameters."""
    params = {
        "working_dir": "/workspace",
        "env_vars": {"PATH": "/usr/bin", "HOME": "/home/user"},
        "timeout": 60,
        "shell": "/bin/bash",
        "debug": True,
    }

    tool = Tool(name="TestTool", params=params)

    assert tool.name == "TestTool"
    assert tool.params == params
    assert tool.params["env_vars"]["PATH"] == "/usr/bin"
    assert tool.params["debug"] is True


def test_tool_serialization():
    """Test Tool serialization and deserialization."""
    params = {"working_dir": "/test", "timeout": 45}
    tool = Tool(name="TestTool", params=params)

    # Test model_dump
    tool_dict = tool.model_dump()
    assert tool_dict["name"] == "TestTool"
    assert tool_dict["params"] == params

    # Test model_dump_json
    tool_json = tool.model_dump_json()
    assert isinstance(tool_json, str)

    # Test deserialization
    tool_restored = Tool.model_validate_json(tool_json)
    assert tool_restored.name == "TestTool"
    assert tool_restored.params == params


def test_tool_validation_requires_name():
    """Test that Tool requires a name."""
    with pytest.raises(ValidationError):
        Tool()  # type: ignore


def test_tool_examples_from_docstring():
    """Test the examples provided in Tool docstring."""
    # Test the examples from the docstring
    examples = ["TestTool", "AnotherTool", "TaskTrackerTool"]

    for example_name in examples:
        spec = Tool(name=example_name)
        assert spec.name == example_name
        assert spec.params == {}

    # Test with params example
    spec_with_params = Tool(name="TestTool", params={"custom_param": "/workspace"})
    assert spec_with_params.name == "TestTool"
    assert spec_with_params.params == {"custom_param": "/workspace"}


def test_tool_different_tool_types():
    """Test creating Tool for different tool types."""
    # TestTool
    test_tool = Tool(
        name="TestTool", params={"custom_dir": "/workspace", "timeout": 30}
    )
    assert test_tool.name == "TestTool"
    assert test_tool.params["custom_dir"] == "/workspace"

    # AnotherTool
    another_tool = Tool(name="AnotherTool")
    assert another_tool.name == "AnotherTool"
    assert another_tool.params == {}

    # TaskTrackerTool
    tracker_tool = Tool(
        name="TaskTrackerTool", params={"save_dir": "/workspace/.openhands"}
    )
    assert tracker_tool.name == "TaskTrackerTool"
    assert tracker_tool.params["save_dir"] == "/workspace/.openhands"


def test_tool_nested_params():
    """Test Tool with nested parameter structures."""
    params = {
        "config": {
            "timeout": 30,
            "retries": 3,
            "options": {"verbose": True, "debug": False},
        },
        "paths": ["/usr/bin", "/usr/local/bin"],
        "env": {"LANG": "en_US.UTF-8"},
    }

    tool = Tool(name="ComplexTool", params=params)

    assert tool.name == "ComplexTool"
    assert tool.params["config"]["timeout"] == 30
    assert tool.params["config"]["options"]["verbose"] is True
    assert tool.params["paths"] == ["/usr/bin", "/usr/local/bin"]
    assert tool.params["env"]["LANG"] == "en_US.UTF-8"


def test_tool_field_descriptions():
    """Test that Tool fields have proper descriptions."""
    fields = Tool.model_fields

    assert "name" in fields
    assert fields["name"].description is not None
    assert "Name of the tool class" in fields["name"].description
    assert (
        "Import it from an `openhands.tools.<module>` subpackage."
        in fields["name"].description
    )

    assert "params" in fields
    assert fields["params"].description is not None
    assert "Parameters for the tool's .create() method" in fields["params"].description


def test_tool_default_params():
    """Test that Tool has correct default for params."""
    tool = Tool(name="TestTool")
    assert tool.params == {}


def test_tool_immutability():
    """Test that Tool behaves correctly with parameter modifications."""
    original_params = {"test_param": "/workspace"}
    tool = Tool(name="BashTool", params=original_params)

    # Modifying the original params should not affect the tool
    original_params["test_param"] = "/changed"
    assert tool.params["test_param"] == "/workspace"


def test_tool_validation_edge_cases():
    """Test Tool validation with edge cases."""
    # Empty string name should be invalid
    with pytest.raises(ValidationError):
        Tool(name="")

    # None params should use default empty dict (handled by validator)
    tool = Tool(name="TestTool")
    assert tool.params == {}


def test_tool_repr():
    """Test Tool string representation."""
    tool = Tool(name="BashTool", params={"test_param": "/test"})
    repr_str = repr(tool)

    assert "Tool" in repr_str
    assert "BashTool" in repr_str
