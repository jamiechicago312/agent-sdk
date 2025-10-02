# OpenHands Agent SDK Hackathon - Judging Guide

**Prize**: $60 OpenHands Cloud Credits OR 3-Month Pro Subscription

This guide helps evaluate hackathon submissions for the $60 prize. Projects must meet **ALL** bare minimum requirements in both SDK and MCP sections to qualify.

## 🔍 Quick Evaluation Checklist

### ✅ SDK Requirements (All Required)

- [ ] **Agent Setup**: Project creates an Agent with LLM configuration and at least 1 tool
- [ ] **Conversation**: Has working conversation flow that processes messages
- [ ] **Tools**: Uses at least 1 built-in tool (BashTool or FileEditorTool)
- [ ] **Code Quality**: Code runs without errors when following setup instructions

### ✅ MCP Requirements (All Required)

- [ ] **MCP Integration**: Has at least 1 working MCP server configured
- [ ] **Configuration**: Valid `mcp_config` dictionary with proper server setup
- [ ] **Functionality**: MCP tools are actually called and used in the conversation
- [ ] **Documentation**: Clear README with setup instructions

## 📋 Detailed Evaluation Process

### Step 1: Repository Review (5 minutes)

**Check for basic structure:**
```
✅ README.md with setup instructions
✅ Python files with Agent SDK imports
✅ Requirements/dependencies listed
✅ MCP configuration visible in code
```

**Red flags (immediate disqualification):**
- No setup instructions
- Code doesn't import OpenHands SDK
- No MCP configuration found
- Repository is just copied examples without modification

### Step 2: Code Analysis (10 minutes)

**SDK Usage Verification:**
```python
# Look for these patterns:
from openhands.sdk import Agent, Conversation, LLM
from openhands.tools import BashTool, FileEditorTool

# Agent creation with tools
agent = Agent(
    llm=llm,
    tools=[...],  # At least 1 tool
    mcp_config={...}  # MCP configuration
)

# Conversation usage
conversation = Conversation(agent=agent)
conversation.send_message("...")
conversation.run()
```

**MCP Configuration Check:**
```python
# Valid MCP config examples:
mcp_config = {
    "mcpServers": {
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        # OR
        "notion": {"url": "https://mcp.notion.com/mcp", "auth": "oauth"},
        # OR any other valid MCP server
    }
}
```

### Step 3: Functionality Test (15 minutes)

**Setup and Run:**
1. Follow the project's setup instructions
2. Install dependencies as specified
3. Set required environment variables
4. Run the main script/demo

**Pass Criteria:**
- [ ] Code executes without Python errors
- [ ] Agent successfully initializes
- [ ] Conversation processes at least one message
- [ ] MCP server connects and tools are available
- [ ] At least one MCP tool is called during execution

**Common Issues to Check:**
- Missing API keys (should be documented)
- MCP server installation problems
- Import errors
- Configuration mistakes

### Step 4: Documentation Review (5 minutes)

**Required Documentation:**
- [ ] Clear setup instructions
- [ ] List of required dependencies/API keys
- [ ] How to run the project
- [ ] What the project does (brief description)

**Bonus Points (not required for prize):**
- Demo video or screenshots
- Architecture explanation
- Creative use cases
- Multiple MCP integrations

## 🎯 Common Qualifying Projects

**✅ PASS Examples:**
- Agent that fetches web content and saves to files using Fetch + FileSystem MCPs
- Slack bot that responds to messages and manages files using Slack + FileSystem MCPs
- Code analyzer that reads repositories and stores results using Git + SQLite MCPs
- Simple workflow automation with any working MCP integration

**❌ FAIL Examples:**
- Just copied example code without modification
- Code doesn't run due to errors
- No MCP integration or non-functional MCP setup
- Missing setup instructions or dependencies
- Only uses SDK without any MCP servers

## 📊 Evaluation Template

**Project**: [Repository URL]
**Evaluated by**: [Your name]
**Date**: [Date]

### SDK Requirements
- [ ] Agent Setup: ✅/❌ - [Notes]
- [ ] Conversation: ✅/❌ - [Notes]
- [ ] Tools: ✅/❌ - [Notes]
- [ ] Code Quality: ✅/❌ - [Notes]

### MCP Requirements
- [ ] MCP Integration: ✅/❌ - [Notes]
- [ ] Configuration: ✅/❌ - [Notes]
- [ ] Functionality: ✅/❌ - [Notes]
- [ ] Documentation: ✅/❌ - [Notes]

### Overall Result
- [ ] **QUALIFIED** - Meets all bare minimum requirements
- [ ] **NOT QUALIFIED** - Missing: [list requirements not met]

### Notes
[Additional observations, creative aspects, or feedback]

---

## 🚀 Bonus Evaluation (Optional)

For projects that exceed bare minimum, note these impressive features:

**SDK Depth:**
- Multiple tool types (built-in + MCP + custom)
- Conversation callbacks or persistence
- Security analyzers or advanced features
- Error handling and edge cases

**MCP Sophistication:**
- Multiple MCP servers working together
- OAuth and HTTP-only MCP combinations
- Creative workflows between different MCPs
- Proper error handling for MCP failures

**Innovation:**
- Solves a real, compelling problem
- Creative use of AI agent capabilities
- Clean, well-structured code
- Comprehensive documentation

These bonus features don't affect prize eligibility but help identify standout projects for potential recognition or future collaboration.