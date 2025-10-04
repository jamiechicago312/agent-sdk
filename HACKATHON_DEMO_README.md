# 🚀 AI Agents Hackathon Demo: OpenHands SDK + MCP Integration

Welcome to the AI Agents Hackathon! This demo showcases powerful ways to integrate the OpenHands Agent SDK with Model Context Protocol (MCP) servers to create valuable AI agents that can interact with real-world systems and data sources.

## 🎯 Hackathon Context

This demo is designed for the [AI Agents Hackathon](https://luma.com/hackdogs?tk=f5jPY1) - a one-day event focused on building cutting-edge AI agents that push the limits of LLMs and AI applications. With $50k+ in prizes, this is your chance to create something extraordinary!

## 🧠 What is MCP (Model Context Protocol)?

Model Context Protocol (MCP) is an open standard that enables AI models to securely access external tools and data sources. Think of it as a bridge that connects your AI agent to the real world - databases, APIs, file systems, cloud services, and more.

## 🛠️ Integration Options

**Start with these working examples:**
- **[Basic MCP Integration](https://github.com/All-Hands-AI/agent-sdk/blob/main/examples/07_mcp_integration.py)**: Fetch MCP + Repomix MCP for web content and code analysis
- **[OAuth MCP Integration](https://github.com/All-Hands-AI/agent-sdk/blob/main/examples/08_mcp_with_oauth.py)**: Notion MCP with OAuth authentication
- **[Notion Blog Demo](https://github.com/jamiechicago312/agent-sdk/tree/ai-agent-hackathon-demo/examples/notion-blog-demo)**: Complete hackathon demo showing Notion MCP integration for automated blog generation
- **[All Examples Directory](https://github.com/All-Hands-AI/agent-sdk/tree/main/examples)**: Complete collection of SDK usage patterns

Here are compelling ways to integrate OpenHands SDK with MCP servers for your hackathon project:

### 1. 🏢 **Enterprise Productivity Agent**
**Use Case**: Create an AI agent that manages your entire work environment
**MCP Integrations**:
- **[Slack MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)**: Send messages, create channels, manage team communications (requires bot token)
- **[Notion MCP](https://developers.notion.com/docs/mcp)**: Create and update documentation, manage project databases (requires OAuth)
- **[GitHub MCP](https://github.com/modelcontextprotocol/servers)**: Review code, create issues, manage repositories (requires auth for private repos)
- **[Google Workspace MCP](https://github.com/taylorwilsdon/google_workspace_mcp)**: Comprehensive Google services including Calendar, Gmail, Docs, Sheets (requires OAuth)
- **[Figma MCP](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)**: Access design files and components for design-to-code workflows (requires API key)

**Demo Idea**: "WorkflowGPT" - An agent that can:
- Analyze your GitHub commits and automatically update project status in Notion
- Schedule code review meetings based on PR activity
- Send daily standup summaries to Slack channels
- Create documentation from code comments
- Generate code from Figma designs

```python
mcp_config = {
    "mcpServers": {
        "slack": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-slack"]},
        "notion": {"url": "https://mcp.notion.com/mcp", "auth": "oauth"},
        "github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"]},
        "google_workspace": {"command": "uvx", "args": ["google-workspace-mcp"]},
        "figma": {"command": "npx", "args": ["-y", "figma-developer-mcp"]}
    }
}
```

### 2. 🔍 **Data Intelligence Agent**
**Use Case**: Build an agent that can analyze and act on data from multiple sources
**MCP Integrations**:
- **[PostgreSQL MCP](https://github.com/subnetmarco/pgmcp)**: Query and analyze PostgreSQL databases (uses database credentials)
- **[Snowflake MCP](https://github.com/Snowflake-Labs/mcp)**: Enterprise data warehouse operations with Cortex AI (uses Snowflake auth)
- **[SQLite MCP](https://github.com/modelcontextprotocol/servers)**: Local database operations (no auth required)
- **[Context7 MCP](https://github.com/upstash/context7)**: Up-to-date documentation and code examples (HTTP-based, no OAuth)

**Demo Idea**: "DataDetective" - An agent that can:
- Connect to your database and identify data quality issues
- Generate automated reports and visualizations
- Suggest database optimizations
- Create data pipelines between different sources
- Access up-to-date documentation for data tools

```python
mcp_config = {
    "mcpServers": {
        "postgres": {"command": "uvx", "args": ["pgmcp"]},
        "snowflake": {"command": "uvx", "args": ["snowflake-mcp-server"]},
        "sqlite": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-sqlite"]},
        "context7": {"url": "https://context7.upstash.com/mcp"}
    }
}
```

### 3. 🌐 **Web Intelligence Agent**
**Use Case**: Create an agent that can browse, scrape, and interact with web content
**MCP Integrations**:
- **[Fetch MCP](https://github.com/ExactDoug/mcp-fetch)**: HTTP requests and web content fetching (no auth required)
- **[Puppeteer MCP](https://github.com/modelcontextprotocol/servers)**: Advanced browser automation (no auth required)
- **[Browser Use MCP](https://github.com/modelcontextprotocol/servers)**: Automated web browsing and interaction (no auth required)

**Demo Idea**: "WebScout" - An agent that can:
- Monitor competitor websites for changes
- Automatically fill out forms and submit applications
- Gather market research from multiple sources
- Create comprehensive web content summaries

```python
mcp_config = {
    "mcpServers": {
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "puppeteer": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-puppeteer"]},
        "browser": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-browser"]}
    }
}
```

### 4. 🎨 **Creative Content Agent**
**Use Case**: Build an agent that can create and manage multimedia content
**MCP Integrations**:
- **[Figma MCP](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)**: Design file access and design-to-code workflows (requires API key)
- **[File System MCP](https://github.com/modelcontextprotocol/servers)**: File operations for content management (no auth required)
- **[Git MCP](https://github.com/modelcontextprotocol/servers)**: Version control for creative projects (no auth required)

**Demo Idea**: "ContentCreator" - An agent that can:
- Generate code from Figma designs
- Create and manage design system components
- Version control design assets and code
- Automate design-to-development workflows

```python
mcp_config = {
    "mcpServers": {
        "figma": {"command": "npx", "args": ["-y", "figma-developer-mcp"]},
        "filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem"]},
        "git": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-git"]}
    }
}
```

### 5. 🏠 **Smart Home/IoT Agent**
**Use Case**: Create an agent that can control and monitor IoT devices
**MCP Integrations**:
- **[Serial MCP](https://github.com/modelcontextprotocol/servers)**: Hardware communication via serial ports (no auth required)
- **[File System MCP](https://github.com/modelcontextprotocol/servers)**: Monitor system files and logs (no auth required)
- **[Fetch MCP](https://github.com/ExactDoug/mcp-fetch)**: HTTP requests to IoT device APIs (no auth required)

**Demo Idea**: "HomeGPT" - An agent that can:
- Monitor system logs and device status
- Communicate with IoT devices via HTTP APIs
- Read sensor data from serial connections
- Automate device control based on patterns

```python
mcp_config = {
    "mcpServers": {
        "serial": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-serial"]},
        "filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem"]},
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]}
    }
}
```

### 6. 💰 **Financial Intelligence Agent**
**Use Case**: Build an agent for financial analysis and trading
**MCP Integrations**:
- **[Fetch MCP](https://github.com/ExactDoug/mcp-fetch)**: HTTP requests to financial APIs (no auth required for public data)
- **[SQLite MCP](https://github.com/modelcontextprotocol/servers)**: Local financial data storage and analysis (no auth required)
- **[File System MCP](https://github.com/modelcontextprotocol/servers)**: Process financial documents and reports (no auth required)

**Demo Idea**: "FinanceGPT" - An agent that can:
- Fetch public market data and financial news
- Analyze financial documents and reports
- Store and query financial data locally
- Generate investment analysis and reports

```python
mcp_config = {
    "mcpServers": {
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "sqlite": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-sqlite"]},
        "filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem"]}
    }
}
```

### 7. 🎓 **Educational Assistant Agent**
**Use Case**: Create an agent that can help with learning and education
**MCP Integrations**:
- **[Context7 MCP](https://github.com/upstash/context7)**: Up-to-date documentation and code examples (HTTP-based, no OAuth)
- **[Fetch MCP](https://github.com/ExactDoug/mcp-fetch)**: Access educational content and APIs (no auth required)
- **[File System MCP](https://github.com/modelcontextprotocol/servers)**: Process educational documents and materials (no auth required)
- **[Git MCP](https://github.com/modelcontextprotocol/servers)**: Version control for educational projects (no auth required)

**Demo Idea**: "TutorGPT" - An agent that can:
- Access up-to-date documentation for any programming library
- Fetch educational content from various sources
- Process and analyze educational documents
- Manage code examples and learning projects

```python
mcp_config = {
    "mcpServers": {
        "context7": {"url": "https://context7.upstash.com/mcp"},
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "filesystem": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem"]},
        "git": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-git"]}
    }
}
```


## 🏆 Popular MCP Server Combinations:
- **Productivity Stack**: Slack + Notion + GitHub + Calendar
- **Data Stack**: Database + Visualization + Reporting + Analytics
- **Content Stack**: Browser + Image Processing + Social Media + Storage
- **Development Stack**: GitHub + Docker + CI/CD + Monitoring
## 🚀 Quick Start Guide

### Prerequisites
- Python 3.12+
- Node.js (for MCP servers)
- OpenHands SDK installed (`make build`)

### Basic Setup

1. **Clone and Setup**:
```bash
git clone https://github.com/All-Hands-AI/agent-sdk.git
cd agent-sdk
make build
```

2. **Configure Environment**:
```bash
export LITELLM_API_KEY="your-api-key"
# Add other API keys as needed for MCP servers
```

3. **Run a Demo**:
```bash
# Try the basic MCP integration example
uv run python examples/07_mcp_integration.py

# Or the OAuth example with Notion
uv run python examples/08_mcp_with_oauth.py
```

For more examples, check out the [examples directory](https://github.com/All-Hands-AI/agent-sdk/tree/main/examples) which contains comprehensive usage examples covering all major features.

### Creating Your Own Agent

```python
import os
from pydantic import SecretStr
from openhands.sdk import LLM, Agent, Conversation
from openhands.sdk.tool import ToolSpec, register_tool
from openhands.tools.execute_bash import BashTool
from openhands.tools.str_replace_editor import FileEditorTool

# Configure LLM
llm = LLM(
    model="litellm_proxy/anthropic/claude-sonnet-4-5-20250929",
    base_url="https://llm-proxy.eval.all-hands.dev",
    api_key=SecretStr(os.getenv("LITELLM_API_KEY")),
)

# Register tools
register_tool("BashTool", BashTool)
register_tool("FileEditorTool", FileEditorTool)

# Configure MCP servers (choose your integration!)
mcp_config = {
    "mcpServers": {
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "notion": {"url": "https://mcp.notion.com/mcp", "auth": "oauth"},
        # Add more MCP servers based on your chosen demo idea
    }
}

# Create agent
agent = Agent(
    llm=llm,
    tools=[
        ToolSpec(name="BashTool"),
        ToolSpec(name="FileEditorTool"),
    ],
    mcp_config=mcp_config,
)

# Start conversation
conversation = Conversation(agent=agent)
conversation.send_message("Your hackathon idea here!")
conversation.run()
```

## 📚 Resources

### Official Documentation:
- [OpenHands SDK Documentation](https://github.com/All-Hands-AI/agent-sdk)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)

### Community Resources:
- [Awesome OpenHands Agent SDK Projects](./awesome-list.md) - Showcase of hackathon and community projects
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers)
- [MCP Examples and Tutorials](https://modelcontextprotocol.io/examples)
- [Notion Blog Demo](https://github.com/jamiechicago312/agent-sdk/tree/ai-agent-hackathon-demo/examples/notion-blog-demo) - Complete hackathon example with setup guide
- [OpenHands Community Slack](https://all-hands.dev/joinslack)

### Example MCP Servers to Try:
- `mcp-server-fetch` - HTTP requests and web APIs
- `mcp-server-filesystem` - File system operations
- `mcp-server-sqlite` - SQLite database operations
- `mcp-server-git` - Git repository management
- `mcp-server-slack` - Slack workspace integration
- `@modelcontextprotocol/server-github` - GitHub API integration

## 🏆 Hackathon Prize & Judging

We now have **two exciting prize tiers** for this hackathon:

### 🥇 **Grand Prize - Top 3 Teams**
**$100 Gift Card** (Amazon or Newegg) for **three lucky teams** who demonstrate exceptional, above-and-beyond SDK/MCP integrations! These teams will showcase innovative use cases, creative combinations of multiple MCP servers, and outstanding implementation quality.

### 🥈 **Participation Prize - All Qualifying Teams**  
**$60 OpenHands Cloud Credits OR 3-Month Pro Subscription** (both $60 value) for **anyone who meets the minimum requirements** below.

Meet the **minimum requirements** below to qualify for the participation prize, and go above and beyond for a chance at the grand prize!

### 🌟 Required: Awesome List Submission

**All hackathon projects must be added to our [Awesome OpenHands Agent SDK Projects](./awesome-list.md) list to qualify for any prize tier!**

This helps showcase the amazing work from our community and makes it easier for others to discover and learn from your project. See the [Contributing section](./awesome-list.md#contributing) in the awesome list for submission guidelines.

### 📊 SDK Requirements

| Component | Description | Minimum | Nice to Haves |
|-----------|-------------|---------------------|---------------|
| **Agent Setup** | Core agent configuration | Agent with LLM + at least 1 tool | Multiple tools, custom configuration |
| **Conversation** | Basic interaction pattern | Working conversation flow | Callbacks, persistence, error handling |
| **Tools** | Tool integration | 1 built-in tool (BashTool/FileEditorTool) | Multiple tools, custom tools |
| **Code Quality** | Implementation standards | Code runs without errors | Clean structure, documentation, tests |

### 📊 MCP Requirements

| Component | Description | Minimum | Nice to Haves |
|-----------|-------------|---------------------|---------------|
| **MCP Integration** | External service connection | 1 working MCP server | Multiple MCPs, OAuth + HTTP mix |
| **Configuration** | MCP setup | Valid mcp_config with working server | Error handling, fallback strategies |
| **Functionality** | Actual usage | MCP tools called successfully | Creative combinations, workflows |
| **Documentation** | Setup instructions | Clear README with setup steps | Demo video, architecture explanation |
| **Awesome List** | Community showcase | Project added to [awesome-list.md](./awesome-list.md) | Detailed description, demo links |

### 🏅 Grand Prize Judging Criteria

The **top 3 teams** will be selected based on exceptional implementation that goes above and beyond the minimum requirements. While we don't have an exact rubric, OpenHands will help determine winners based on:

- **Innovation**: Creative and unique use cases that showcase the power of SDK + MCP integration
- **Technical Excellence**: Multiple MCP servers, complex workflows, robust error handling
- **Real-World Value**: Solutions that solve actual problems and demonstrate clear utility
- **Implementation Quality**: Clean code, comprehensive documentation, and reliable functionality
- **Community Impact**: Projects that could inspire others and contribute meaningfully to the ecosystem

*The judging process will be collaborative with the OpenHands team to ensure fair evaluation.*

## 🤝 Getting Help

- **[Slack](https://all-hands.dev/joinslack)**: Join the OpenHands community for real-time help
- **[GitHub Issues](https://github.com/All-Hands-AI/agent-sdk/issues)**: Report bugs or request features
- **[Examples](https://github.com/All-Hands-AI/agent-sdk/tree/main/examples)**: Check the examples directory for working code
- **[Documentation](https://github.com/All-Hands-AI/agent-sdk/blob/main/README.md)**: Comprehensive guides in the main README

## 🎉 Ready to Build?

Choose one of the integration options above, or create your own unique combination! The key is to solve a real problem that the judges can immediately understand and appreciate.

Remember: The best hackathon projects are those that work reliably and demonstrate clear value. Start simple, get it working, then add complexity.

**Good luck, and happy hacking! 🚀**

---

*This demo is part of the OpenHands Agent SDK project. For more information, see the main [README.md](https://github.com/All-Hands-AI/agent-sdk/blob/main/README.md).*
