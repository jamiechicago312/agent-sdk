# 🚀 AI Agents Hackathon Demo: OpenHands SDK + MCP Integration

Welcome to the AI Agents Hackathon! This demo showcases powerful ways to integrate the OpenHands Agent SDK with Model Context Protocol (MCP) servers to create valuable AI agents that can interact with real-world systems and data sources.

## 🎯 Hackathon Context

This demo is designed for the [AI Agents Hackathon](https://luma.com/hackdogs?tk=f5jPY1) - a one-day event focused on building cutting-edge AI agents that push the limits of LLMs and AI applications. With $50k+ in prizes, this is your chance to create something extraordinary!

## 🧠 What is MCP (Model Context Protocol)?

Model Context Protocol (MCP) is an open standard that enables AI models to securely access external tools and data sources. Think of it as a bridge that connects your AI agent to the real world - databases, APIs, file systems, cloud services, and more.

## 🛠️ Integration Options

Here are compelling ways to integrate OpenHands SDK with MCP servers for your hackathon project:

### 1. 🏢 **Enterprise Productivity Agent**
**Use Case**: Create an AI agent that manages your entire work environment
**MCP Integrations**:
- **Slack MCP**: Send messages, create channels, manage team communications
- **Notion MCP**: Create and update documentation, manage project databases
- **GitHub MCP**: Review code, create issues, manage repositories
- **Google Calendar MCP**: Schedule meetings, manage time blocks

**Demo Idea**: "WorkflowGPT" - An agent that can:
- Analyze your GitHub commits and automatically update project status in Notion
- Schedule code review meetings based on PR activity
- Send daily standup summaries to Slack channels
- Create documentation from code comments

```python
mcp_config = {
    "mcpServers": {
        "slack": {"command": "npx", "args": ["-y", "mcp-server-slack"]},
        "notion": {"url": "https://mcp.notion.com/mcp", "auth": "oauth"},
        "github": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"]},
        "calendar": {"command": "npx", "args": ["-y", "mcp-server-google-calendar"]}
    }
}
```

### 2. 🔍 **Data Intelligence Agent**
**Use Case**: Build an agent that can analyze and act on data from multiple sources
**MCP Integrations**:
- **Database MCP** (PostgreSQL, MySQL, SQLite): Query and analyze data
- **Snowflake MCP**: Enterprise data warehouse operations
- **Firebase MCP**: Real-time database operations
- **CSV/Excel MCP**: Process spreadsheet data

**Demo Idea**: "DataDetective" - An agent that can:
- Connect to your database and identify data quality issues
- Generate automated reports and visualizations
- Suggest database optimizations
- Create data pipelines between different sources

```python
mcp_config = {
    "mcpServers": {
        "postgres": {"command": "npx", "args": ["-y", "mcp-server-postgres"]},
        "snowflake": {"command": "npx", "args": ["-y", "mcp-server-snowflake"]},
        "csv": {"command": "npx", "args": ["-y", "mcp-server-csv"]}
    }
}
```

### 3. 🌐 **Web Intelligence Agent**
**Use Case**: Create an agent that can browse, scrape, and interact with web content
**MCP Integrations**:
- **Browser MCP**: Automated web browsing and interaction
- **Fetch MCP**: HTTP requests and API interactions
- **Puppeteer MCP**: Advanced browser automation
- **FireCrawl MCP**: Web scraping and content extraction

**Demo Idea**: "WebScout" - An agent that can:
- Monitor competitor websites for changes
- Automatically fill out forms and submit applications
- Gather market research from multiple sources
- Create comprehensive web content summaries

```python
mcp_config = {
    "mcpServers": {
        "browser": {"command": "npx", "args": ["-y", "mcp-server-puppeteer"]},
        "fetch": {"command": "uvx", "args": ["mcp-server-fetch"]},
        "firecrawl": {"command": "npx", "args": ["-y", "mcp-server-firecrawl"]}
    }
}
```

### 4. 🎨 **Creative Content Agent**
**Use Case**: Build an agent that can create and manage multimedia content
**MCP Integrations**:
- **Blender MCP**: 3D modeling and animation
- **GIMP MCP**: Image editing and manipulation
- **FFmpeg MCP**: Video and audio processing
- **Canva MCP**: Design automation

**Demo Idea**: "ContentCreator" - An agent that can:
- Generate social media content with custom graphics
- Create product mockups and presentations
- Edit videos based on text descriptions
- Design marketing materials automatically

```python
mcp_config = {
    "mcpServers": {
        "blender": {"command": "npx", "args": ["-y", "mcp-server-blender"]},
        "gimp": {"command": "npx", "args": ["-y", "mcp-server-gimp"]},
        "ffmpeg": {"command": "npx", "args": ["-y", "mcp-server-ffmpeg"]}
    }
}
```

### 5. 🏠 **Smart Home/IoT Agent**
**Use Case**: Create an agent that can control and monitor IoT devices
**MCP Integrations**:
- **Home Assistant MCP**: Smart home device control
- **MQTT MCP**: IoT device communication
- **Arduino MCP**: Hardware interaction
- **Raspberry Pi MCP**: Edge computing control

**Demo Idea**: "HomeGPT" - An agent that can:
- Monitor home security and send alerts
- Optimize energy usage based on patterns
- Control lighting and temperature automatically
- Manage smart appliances and schedules

```python
mcp_config = {
    "mcpServers": {
        "homeassistant": {"command": "npx", "args": ["-y", "mcp-server-homeassistant"]},
        "mqtt": {"command": "npx", "args": ["-y", "mcp-server-mqtt"]},
        "arduino": {"command": "npx", "args": ["-y", "mcp-server-arduino"]}
    }
}
```

### 6. 💰 **Financial Intelligence Agent**
**Use Case**: Build an agent for financial analysis and trading
**MCP Integrations**:
- **Trading APIs MCP**: Stock market data and trading
- **Crypto MCP**: Cryptocurrency monitoring and trading
- **Banking MCP**: Account management and transactions
- **QuickBooks MCP**: Accounting and bookkeeping

**Demo Idea**: "FinanceGPT" - An agent that can:
- Analyze market trends and provide investment advice
- Monitor portfolio performance and rebalance automatically
- Generate financial reports and tax documents
- Detect fraudulent transactions and spending patterns

```python
mcp_config = {
    "mcpServers": {
        "trading": {"command": "npx", "args": ["-y", "mcp-server-alpaca"]},
        "crypto": {"command": "npx", "args": ["-y", "mcp-server-coinbase"]},
        "quickbooks": {"command": "npx", "args": ["-y", "mcp-server-quickbooks"]}
    }
}
```

### 7. 🎓 **Educational Assistant Agent**
**Use Case**: Create an agent that can help with learning and education
**MCP Integrations**:
- **Khan Academy MCP**: Educational content access
- **Wikipedia MCP**: Knowledge base queries
- **PDF MCP**: Document processing and analysis
- **Jupyter MCP**: Interactive coding environments

**Demo Idea**: "TutorGPT" - An agent that can:
- Create personalized learning plans
- Generate quizzes and assignments
- Provide code reviews and explanations
- Track learning progress and suggest improvements

```python
mcp_config = {
    "mcpServers": {
        "wikipedia": {"command": "npx", "args": ["-y", "mcp-server-wikipedia"]},
        "pdf": {"command": "npx", "args": ["-y", "mcp-server-pdf"]},
        "jupyter": {"command": "npx", "args": ["-y", "mcp-server-jupyter"]}
    }
}
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.12+
- Node.js (for MCP servers)
- OpenHands SDK installed (`make build`)

### Basic Setup

1. **Clone and Setup**:
```bash
git clone https://github.com/jamiechicago312/agent-sdk-demo.git
cd agent-sdk-demo
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

## 🏆 Hackathon Tips

### Judging Criteria (Based on typical hackathon standards):
1. **Innovation**: How creative and novel is your MCP integration?
2. **Technical Implementation**: Code quality and architecture
3. **Real-world Value**: Does it solve an actual problem?
4. **Demo Quality**: How well can you present your solution?

### Winning Strategies:
1. **Focus on a specific use case** - Don't try to integrate everything
2. **Show real value** - Demonstrate clear benefits over existing solutions
3. **Make it interactive** - Live demos are more impressive than slides
4. **Handle edge cases** - Robust error handling shows professionalism
5. **Think about scalability** - How would this work with 1000+ users?

### Popular MCP Server Combinations:
- **Productivity Stack**: Slack + Notion + GitHub + Calendar
- **Data Stack**: Database + Visualization + Reporting + Analytics
- **Content Stack**: Browser + Image Processing + Social Media + Storage
- **Development Stack**: GitHub + Docker + CI/CD + Monitoring

## 📚 Resources

### Official Documentation:
- [OpenHands SDK Documentation](https://github.com/All-Hands-AI/agent-sdk)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)

### Community Resources:
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers)
- [MCP Examples and Tutorials](https://modelcontextprotocol.io/examples)
- [OpenHands Community Discord](https://discord.gg/ESHStjSjD4)

### Example MCP Servers to Try:
- `mcp-server-fetch` - HTTP requests and web APIs
- `mcp-server-filesystem` - File system operations
- `mcp-server-sqlite` - SQLite database operations
- `mcp-server-git` - Git repository management
- `mcp-server-slack` - Slack workspace integration
- `@modelcontextprotocol/server-github` - GitHub API integration

## 🤝 Getting Help

- **Discord**: Join the OpenHands community for real-time help
- **GitHub Issues**: Report bugs or request features
- **Examples**: Check the `examples/` directory for working code
- **Documentation**: Comprehensive guides in the main README

## 🎉 Ready to Build?

Choose one of the integration options above, or create your own unique combination! The key is to solve a real problem that the judges can immediately understand and appreciate.

Remember: The best hackathon projects are those that work reliably and demonstrate clear value. Start simple, get it working, then add complexity.

**Good luck, and happy hacking! 🚀**

---

*This demo is part of the OpenHands Agent SDK project. For more information, see the main [README.md](./README.md).*