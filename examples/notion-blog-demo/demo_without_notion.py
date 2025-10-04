#!/usr/bin/env python3
"""
Demo Blog Generator - Works without Notion for testing

This script demonstrates the blog generation capabilities without requiring
Notion authentication. Perfect for testing the core functionality.
"""

import os
from pathlib import Path

from pydantic import SecretStr

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


def create_demo_blog():
    """Create a demo blog site without Notion integration."""

    # Check for API key
    api_key = os.getenv("LITELLM_API_KEY")
    if not api_key:
        print("❌ Error: LITELLM_API_KEY environment variable is not set.")
        return

    # Setup output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Configure LLM
    llm = LLM(
        service_id="demo_blog_agent",
        model="litellm_proxy/anthropic/claude-sonnet-4-5-20250929",
        base_url="https://llm-proxy.eval.all-hands.dev",
        api_key=SecretStr(api_key),
    )

    # Register tools
    register_tool("BashTool", BashTool)
    register_tool("FileEditorTool", FileEditorTool)

    # Create agent (no MCP for this demo)
    agent = Agent(
        llm=llm,
        tools=[
            Tool(name="BashTool"),
            Tool(name="FileEditorTool"),
        ],
    )

    # Track messages
    llm_messages = []

    def conversation_callback(event: Event):
        if isinstance(event, LLMConvertibleEvent):
            llm_messages.append(event.to_llm_message())

    # Create conversation
    conversation = Conversation(
        agent=agent,
        callbacks=[conversation_callback],
        workspace=str(output_dir.absolute()),
    )

    print("🚀 Creating demo blog site...")

    # Send message to create the blog
    message = """
I want you to create a simple, clean blog website. Here's what I need:

1. **Create the basic structure**:
   - index.html (main page listing blog posts)
   - css/style.css (clean, minimal styling for fast rendering)
   - js/main.js (basic interactive features)
   - posts/ directory for individual blog posts

2. **Create sample blog posts**:
   - Create 3-4 sample blog posts in HTML format
   - Topics can be: "Welcome to My Blog", "Getting Started with AI Agents",
     "Building with OpenHands SDK", "The Future of AI Development"
   - Each post should have a title, date, and content with proper HTML formatting

3. **Styling requirements**:
   - Clean, minimal design
   - Responsive layout (works on mobile and desktop)
   - Fast loading (minimal CSS, no external dependencies)
   - Professional appearance

4. **Features to include**:
   - Navigation between posts
   - Post listing on the main page
   - Reading time estimation
   - Clean typography and spacing

5. **File organization**:
   - Put CSS in css/ directory
   - Put JavaScript in js/ directory
   - Put blog posts in posts/ directory
   - Make sure all links work correctly

Please create a complete, working blog site that I can open in a browser.
Focus on clean, semantic HTML and efficient CSS.
"""

    conversation.send_message(message)
    conversation.run()

    print("✅ Demo blog created!")
    print(f"📁 Files created in: {output_dir.absolute()}")
    print(f"🌐 Open {output_dir}/index.html in your browser to view the blog!")

    # List created files
    files = list(output_dir.rglob("*"))
    if files:
        print(f"\n📄 Created files ({len(files)}):")
        for file in sorted(files):
            if file.is_file():
                print(f"   - {file.relative_to(output_dir)}")

    return len(llm_messages)


if __name__ == "__main__":
    try:
        message_count = create_demo_blog()
        print(f"\n📊 Total LLM messages: {message_count}")
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logger.error(f"Demo failed: {e}", exc_info=True)
