"""Test that an agent can write a git commit message and commit changes."""

import os
import subprocess

from openhands.sdk import get_logger
from openhands.sdk.tool import Tool, register_tool
from openhands.tools.execute_bash import BashTool
from openhands.tools.str_replace_editor import FileEditorTool
from tests.integration.base import BaseIntegrationTest, TestResult


INSTRUCTION = (
    "Write a git commit message for the current staging area and commit the changes."
)


logger = get_logger(__name__)


class GitStagingTest(BaseIntegrationTest):
    """Test that an agent can write a git commit message and commit changes."""

    INSTRUCTION = INSTRUCTION

    @property
    def tools(self) -> list[Tool]:
        """List of tools available to the agent."""
        if self.cwd is None:
            raise ValueError("CWD must be set before accessing tools")
        register_tool("BashTool", BashTool)
        register_tool("FileEditorTool", FileEditorTool)
        return [
            Tool(name="BashTool"),
            Tool(name="FileEditorTool"),
        ]

    def setup(self) -> None:
        """Set up git repository with staged changes."""
        if self.cwd is None:
            raise ValueError("CWD must be set before setup")

        try:
            # Initialize git repository
            subprocess.run(
                ["git", "init"], cwd=self.cwd, check=True, capture_output=True
            )

            # Configure git user (required for commits)
            subprocess.run(
                ["git", "config", "user.name", "Test User"],
                cwd=self.cwd,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "config", "user.email", "test@example.com"],
                cwd=self.cwd,
                check=True,
                capture_output=True,
            )

            # Create a Python file
            hello_py_path = os.path.join(self.cwd, "hello.py")
            with open(hello_py_path, "w") as f:
                f.write('print("hello world")\n')

            # Stage the file
            subprocess.run(
                ["git", "add", "hello.py"],
                cwd=self.cwd,
                check=True,
                capture_output=True,
            )

            logger.info("Set up git repository with staged hello.py file")

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to set up git repository: {e}")

    def verify_result(self) -> TestResult:
        """Verify that the agent successfully committed the staged changes."""
        if self.cwd is None:
            return TestResult(success=False, reason="CWD not set")

        try:
            # Check git status to see if there are any staged changes left
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.cwd,
                capture_output=True,
                text=True,
                check=True,
            )

            # If there are still staged changes, the commit didn't happen
            if status_result.stdout.strip():
                return TestResult(
                    success=False,
                    reason=f"Staged changes still exist: {status_result.stdout}",
                )

            # Check if there are any commits
            log_result = subprocess.run(
                ["git", "log", "--oneline"],
                cwd=self.cwd,
                capture_output=True,
                text=True,
                check=True,
            )

            if not log_result.stdout.strip():
                return TestResult(
                    success=False, reason="No commits found in repository"
                )

            # Get the latest commit message
            commit_msg_result = subprocess.run(
                ["git", "log", "-1", "--pretty=format:%s"],
                cwd=self.cwd,
                capture_output=True,
                text=True,
                check=True,
            )

            commit_message = commit_msg_result.stdout.strip()

            # Verify the commit contains the hello.py file
            show_result = subprocess.run(
                ["git", "show", "--name-only", "--pretty=format:"],
                cwd=self.cwd,
                capture_output=True,
                text=True,
                check=True,
            )

            if "hello.py" not in show_result.stdout:
                return TestResult(
                    success=False,
                    reason="hello.py not found in the committed changes",
                )

            return TestResult(
                success=True,
                reason=(
                    f"Successfully committed changes with message: '{commit_message}'"
                ),
            )

        except subprocess.CalledProcessError as e:
            return TestResult(success=False, reason=f"Git command failed: {e}")

    def teardown(self):
        """Clean up test resources."""
        # Note: In this implementation, cwd is managed externally
        # so we don't need to clean it up here
        pass
