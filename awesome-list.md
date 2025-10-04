# Awesome OpenHands Agent SDK Projects [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome projects built with the OpenHands Agent SDK and MCP (Model Context Protocol) integration.

The [OpenHands Agent SDK](https://github.com/All-Hands-AI/agent-sdk) enables developers to create powerful AI agents that can interact with real-world systems through MCP servers. This list showcases innovative projects from our hackathon community and beyond.

## Contents

- [Hackathon Projects](#hackathon-projects)
- [Community Projects](#community-projects)
- [Tools & Utilities](#tools--utilities)
- [Educational Resources](#educational-resources)
- [Contributing](#contributing)

## Hackathon Projects

*Projects from the AI Agents Hackathon - showcasing creative uses of OpenHands SDK + MCP integration*

### 🎯 Featured Project

- **[Notion Blog Demo](https://github.com/jamiechicago312/agent-sdk/tree/ai-agent-hackathon-demo/examples/notion-blog-demo)** - Automated blog generation system that connects to Notion via MCP OAuth, extracts content from pages/databases, and generates a complete HTML/CSS/JS blog site. Demonstrates full workflow from content creation to web publishing. [Repository](https://github.com/jamiechicago312/agent-sdk/tree/ai-agent-hackathon-demo/examples/notion-blog-demo)

### Enterprise & Productivity

- **SlackFlow Agent** - AI agent that integrates Slack, GitHub, and Google Calendar MCP servers to automate project updates, schedule meetings based on code commits, and generate team status reports.

- **DataSync Pro** - Database intelligence agent using PostgreSQL and SQLite MCP servers to synchronize data across systems, detect inconsistencies, and generate automated reports.

### Web & Content

- **WebHarvester** - Content aggregation agent using Fetch and Puppeteer MCP servers to monitor competitor websites, extract pricing data, and generate market intelligence reports.

- **SEO Optimizer** - Website analysis agent that crawls sites using Browser MCP, analyzes content structure, and generates SEO improvement recommendations with automated fixes.

### Development & DevOps

- **GitFlow Assistant** - Development workflow agent integrating GitHub MCP to automate code reviews, manage pull requests, and maintain coding standards across repositories.

- **Deploy Commander** - CI/CD automation agent using SSH and Docker MCP servers to manage deployment pipelines, monitor system health, and handle automated rollbacks.

### Finance & Analytics

- **Market Intelligence** - Financial analysis agent using public API MCP servers to fetch market data, analyze trends, and generate investment research reports with risk assessments.

- **Expense Tracker Pro** - Personal finance agent that connects to banking APIs via MCP to categorize transactions, track budgets, and generate spending insights.

### IoT & Smart Systems

- **Smart Home Hub** - Home automation agent using MQTT and Home Assistant MCP servers to control IoT devices, monitor energy usage, and automate routines based on occupancy patterns.

- **Industrial Monitor** - Manufacturing oversight agent that processes sensor data via MCP, detects equipment anomalies, and triggers predictive maintenance workflows.

### Education & Learning

- **Code Mentor** - Educational assistant agent that accesses documentation via MCP, reviews student code, provides personalized feedback, and tracks learning progress across programming languages.

- **Research Assistant** - Academic support agent using web search and document MCP servers to gather research materials, summarize papers, and generate bibliographies for students.

## Community Projects

*Open source projects and contributions from the OpenHands community*

### Frameworks & Libraries

- **Multi-Agent Orchestrator** - Framework for coordinating multiple OpenHands agents in complex workflows with shared context and task delegation.
- **MCP Server Toolkit** - Development toolkit for building custom MCP servers with TypeScript/Python templates and testing utilities.

### Integrations

- **OpenHands-LangChain Bridge** - Integration layer that allows OpenHands agents to use LangChain tools and vice versa, enabling hybrid workflows.
- **AutoGen Connector** - Multi-agent conversation framework that orchestrates OpenHands agents alongside AutoGen agents for complex problem-solving.

## Tools & Utilities

### Development Tools

- **Agent Inspector** - Visual debugging tool for OpenHands agent conversations, tool calls, and MCP interactions with step-by-step execution traces.
- **MCP Server Validator** - Testing framework for validating MCP server implementations, checking protocol compliance, and performance benchmarking.
- **Conversation Flow Analyzer** - Tool for analyzing agent conversation patterns, identifying bottlenecks, and optimizing prompt strategies.

### Monitoring & Analytics

- **Agent Performance Dashboard** - Real-time monitoring dashboard for tracking agent execution times, token usage, costs, and success rates across multiple deployments.
- **Usage Pattern Tracker** - Analytics tool for understanding agent usage patterns, identifying popular workflows, and discovering optimization opportunities.

## Educational Resources

### Tutorials & Guides

- **OpenHands SDK Cookbook** - Comprehensive collection of code recipes, patterns, and best practices for common agent development scenarios and MCP integrations.
- **MCP Integration Patterns** - Detailed guide covering authentication flows, error handling, and optimization strategies for various MCP server types.
- **Agent Architecture Guide** - Design patterns and architectural principles for building scalable, maintainable agent systems with proper separation of concerns.

### Video Content

- **Agent Development Masterclass** - Video series covering advanced techniques for building production-ready agents, debugging strategies, and performance optimization.
- **MCP Protocol Deep Dive** - Technical walkthrough of Model Context Protocol implementation, custom server development, and security considerations.

## Contributing

We welcome contributions to this awesome list! Here's how you can add your project:

### Requirements for Hackathon Projects

To qualify for the **$60 OpenHands Cloud Credits OR 3-Month Pro Subscription**, your project must:

#### SDK Requirements
- ✅ Agent with LLM + at least 1 tool
- ✅ Working conversation flow
- ✅ 1 built-in tool (BashTool/FileEditorTool)
- ✅ Code runs without errors

#### MCP Requirements
- ✅ 1 working MCP server integration
- ✅ Valid mcp_config with working server
- ✅ MCP tools called successfully
- ✅ Clear README with setup steps

#### Awesome List Requirement
- ✅ **Project must be added to this awesome list** (new requirement!)

### How to Add Your Project

1. **Fork this repository**
2. **Add your project** to the appropriate section with:
   - Project name and brief description
   - Key features and MCP integrations used
   - Link to your repository
   - Demo video or screenshots (optional but recommended)
3. **Follow the format**:
   ```markdown
   - **ProjectName** - Brief description of what it does and which MCP servers it uses. [Repository](https://github.com/username/repo) | [Demo](https://demo-link.com)
   ```
4. **Submit a pull request** with a clear description of your project

### Guidelines

- Only include projects that actually work and demonstrate clear value
- Provide accurate descriptions and working links
- Follow the existing format and style
- Projects should use OpenHands SDK with at least one MCP integration
- Include setup instructions in your project's README

## Community

- **[OpenHands Community Slack](https://all-hands.dev/joinslack)** - Join our community for support and discussions
- **[GitHub Discussions](https://github.com/All-Hands-AI/agent-sdk/discussions)** - Ask questions and share ideas
- **[Documentation](https://docs.all-hands.dev)** - Official OpenHands documentation
- **[Examples](https://github.com/All-Hands-AI/agent-sdk/tree/main/examples)** - Official SDK examples

## Related Resources

- **[OpenHands Main Repository](https://github.com/All-Hands-AI/OpenHands)** - The main OpenHands platform
- **[Model Context Protocol](https://modelcontextprotocol.io/)** - Official MCP specification
- **[MCP Server Registry](https://github.com/modelcontextprotocol/servers)** - Official MCP servers
- **[Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers)** - Community MCP server list

---

**Built with ❤️ by the OpenHands community**

*This awesome list is part of the [OpenHands Agent SDK](https://github.com/All-Hands-AI/agent-sdk) project. For more information about OpenHands, visit [all-hands.dev](https://all-hands.dev).*