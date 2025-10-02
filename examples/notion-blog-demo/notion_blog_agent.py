#!/usr/bin/env python3
"""
Notion Blog Demo - OpenHands SDK + Notion MCP Integration

This demo showcases how to use the OpenHands SDK with Notion MCP to:
1. Fetch content from Notion pages/databases
2. Generate a simple HTML/CSS/JS blog site
3. Create new blog posts with matching styling

Meets hackathon requirements:
- Agent with LLM + multiple tools (BashTool, FileEditorTool)
- Working conversation flow
- Notion MCP integration with OAuth
- Clear documentation and setup instructions
"""

import os
from pathlib import Path
from typing import Any

from pydantic import SecretStr


# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    # dotenv not available, environment variables should be set manually
    pass

from openhands.sdk import (
    LLM,
    Agent,
    Conversation,
    Event,
    LLMConvertibleEvent,
    get_logger,
)
from openhands.sdk.tool import Tool, register_tool
from openhands.tools.execute_bash import BashTool
from openhands.tools.str_replace_editor import FileEditorTool


logger = get_logger(__name__)


class NotionBlogAgent:
    """Agent that converts Notion content to a blog site using OpenHands SDK."""

    def __init__(self, api_key: str, output_dir: str = "output"):
        """Initialize the Notion Blog Agent.

        Args:
            api_key: LiteLLM API key for the LLM
            output_dir: Directory to output the generated blog site
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Configure LLM
        self.llm = LLM(
            service_id="notion_blog_agent",
            model="litellm_proxy/anthropic/claude-sonnet-4-5-20250929",
            base_url="https://llm-proxy.eval.all-hands.dev",
            api_key=SecretStr(api_key),
        )

        # Register tools
        register_tool("BashTool", BashTool)
        register_tool("FileEditorTool", FileEditorTool)

        # Configure MCP with Notion
        mcp_config = {
            "mcpServers": {
                "notion": {"url": "https://mcp.notion.com/mcp", "auth": "oauth"},
                "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
            }
        }

        # Create agent with tools and MCP
        self.agent = Agent(
            llm=self.llm,
            tools=[
                Tool(name="BashTool"),
                Tool(name="FileEditorTool"),
            ],
            mcp_config=mcp_config,
        )

        # Track conversation messages
        self.llm_messages = []

    def _conversation_callback(self, event: Event):
        """Callback to track LLM messages."""
        if isinstance(event, LLMConvertibleEvent):
            self.llm_messages.append(event.to_llm_message())

    def create_blog_site(self, notion_page_url: str | None = None) -> None:
        """Create a blog site from Notion content.

        Args:
            notion_page_url: Optional URL to a specific Notion page to convert
        """
        logger.info("Starting Notion Blog conversion...")

        # Create conversation
        conversation = Conversation(
            agent=self.agent,
            callbacks=[self._conversation_callback],
            workspace=str(self.output_dir.absolute()),
        )

        # Initial setup message
        setup_message = (
            "I want you to help me create a simple blog website from Notion content. "
            "Here's what I need:\n\n"
            "1. **Setup the blog structure**: Create a basic HTML/CSS/JS blog site "
            "with:\n"
            "   - A clean, simple design (minimal CSS for fast rendering)\n"
            "   - An index.html page that lists blog posts\n"
            "   - A template for individual blog posts\n"
            "   - Basic navigation and styling\n\n"
            "2. **Notion Integration**:\n"
            "   - Use the Notion MCP to access my Notion workspace\n"
            "   - Search for pages that could be blog posts\n"
            "   - Extract the content, title, and any metadata\n\n"
            "3. **Content Migration**:\n"
            "   - Convert Notion content to HTML format\n"
            "   - Create individual blog post pages\n"
            "   - Update the index page with the new posts\n"
            "   - Maintain consistent styling across all pages\n\n"
            "4. **File Organization**:\n"
            f"   - Put all files in the current working directory: "
            f"{self.output_dir.absolute()}\n"
            "   - Create a clear folder structure (css/, js/, posts/, etc.)\n"
            "   - Generate clean, semantic HTML\n\n"
            "Please start by setting up the basic blog structure, then we'll work on "
            "the Notion integration."
        )

        if notion_page_url:
            setup_message += f"\n\nSpecific Notion page to convert: {notion_page_url}"

        conversation.send_message(setup_message)
        conversation.run()

        logger.info("Blog site creation completed!")

    def add_blog_post(self, notion_page_url: str) -> None:
        """Add a new blog post from a specific Notion page.

        Args:
            notion_page_url: URL to the Notion page to convert to a blog post
        """
        logger.info(f"Adding blog post from Notion page: {notion_page_url}")

        conversation = Conversation(
            agent=self.agent,
            callbacks=[self._conversation_callback],
            workspace=str(self.output_dir.absolute()),
        )

        message = (
            f"I want to add a new blog post to my existing blog site from this "
            f"Notion page: {notion_page_url}\n\n"
            "Please:\n"
            "1. Use the Notion MCP to fetch the content from this specific page\n"
            "2. Extract the title, content, and any metadata (date, tags, etc.)\n"
            "3. Convert the content to HTML format, preserving formatting\n"
            "4. Create a new blog post page using the existing template/styling\n"
            "5. Update the index.html page to include this new post\n"
            "6. Ensure the styling matches the existing blog design\n\n"
            "The blog site should already exist in the current directory. "
            "If it doesn't, please let me know."
        )

        conversation.send_message(message)
        conversation.run()

        logger.info("Blog post added successfully!")

    def get_conversation_summary(self) -> dict[str, Any]:
        """Get a summary of the conversation for debugging."""
        return {
            "total_messages": len(self.llm_messages),
            "output_directory": str(self.output_dir.absolute()),
            "files_created": list(self.output_dir.rglob("*"))
            if self.output_dir.exists()
            else [],
        }


def main():
    """Main function to run the Notion Blog Agent demo."""
    # Check for required environment variable
    api_key = os.getenv("LITELLM_API_KEY")
    if not api_key:
        print("❌ Error: LITELLM_API_KEY environment variable is not set.")
        print("Please set your OpenHands API key in one of these ways:")
        print("1. Create a .env file with: LITELLM_API_KEY=your-openhands-api-key")
        print(
            "2. Export environment variable: "
            "export LITELLM_API_KEY='your-openhands-api-key'"
        )
        print("3. Use direct provider keys: OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.")
        return

    print("🚀 Starting Notion Blog Demo")
    print("=" * 50)

    # Create agent
    agent = NotionBlogAgent(api_key=api_key, output_dir="output")

    # Interactive mode
    print("\nChoose an option:")
    print("1. Create a new blog site from Notion content")
    print("2. Add a specific Notion page as a blog post")
    print("3. Create a demo blog site (no Notion content)")

    try:
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            print("\n📝 Creating blog site from Notion content...")
            agent.create_blog_site()

        elif choice == "2":
            notion_url = input("Enter the Notion page URL: ").strip()
            if notion_url:
                print(f"\n📄 Adding blog post from: {notion_url}")
                agent.add_blog_post(notion_url)
            else:
                print("❌ No URL provided")
                return

        elif choice == "3":
            print("\n🎨 Creating demo blog site...")
            agent.create_blog_site()

        else:
            print("❌ Invalid choice")
            return

        # Show summary
        summary = agent.get_conversation_summary()
        print("\n✅ Demo completed!")
        print(f"📊 Total LLM messages: {summary['total_messages']}")
        print(f"📁 Output directory: {summary['output_directory']}")

        # List created files
        output_path = Path(summary["output_directory"])
        if output_path.exists():
            files = list(output_path.rglob("*"))
            if files:
                print(f"📄 Files created ({len(files)}):")
                for file in sorted(files)[:10]:  # Show first 10 files
                    if file.is_file():
                        print(f"   - {file.relative_to(output_path)}")
                if len(files) > 10:
                    print(f"   ... and {len(files) - 10} more files")

        print(f"\n🌐 Open {output_path}/index.html in your browser to view the blog!")

    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logger.error(f"Demo failed: {e}", exc_info=True)


if __name__ == "__main__":
    main()
