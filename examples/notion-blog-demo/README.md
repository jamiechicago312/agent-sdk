# 🚀 Notion Blog Demo - OpenHands SDK + Notion MCP Integration

A hackathon demo that showcases the power of combining the OpenHands Agent SDK with Notion's Model Context Protocol (MCP) to create an automated blog generation system.

## 🎯 What This Demo Does

This project demonstrates how to:

1. **Connect to Notion** via MCP OAuth integration
2. **Extract content** from Notion pages and databases
3. **Generate a blog site** with clean HTML, CSS, and JavaScript
4. **Automate content migration** from Notion to web format
5. **Maintain consistent styling** across all generated pages

## 🏆 Hackathon Requirements Met

### ✅ SDK Requirements
- **Agent Setup**: ✅ Agent with LLM + multiple tools (BashTool, FileEditorTool)
- **Conversation**: ✅ Working conversation flow with callbacks
- **Tools**: ✅ Multiple built-in tools integrated
- **Code Quality**: ✅ Clean structure, error handling, documentation

### ✅ MCP Requirements  
- **MCP Integration**: ✅ Notion MCP with OAuth authentication
- **Configuration**: ✅ Valid mcp_config with working server
- **Functionality**: ✅ MCP tools called successfully for content fetching
- **Documentation**: ✅ Comprehensive setup instructions and demo

## 🛠️ Architecture

```
Notion Page/Database → Notion MCP → OpenHands Agent → HTML/CSS/JS Blog
                                         ↓
                              BashTool + FileEditorTool
                                         ↓
                                  Generated Website
```

## 📋 Prerequisites

Before running this demo, you'll need:

1. **Python 3.12+** installed
2. **Node.js** (for MCP servers)
3. **OpenHands SDK** built (`make build` in the root directory)
4. **API Keys** (see setup section below)

## 🚀 Quick Start

### 1. Clone and Build

```bash
git clone https://github.com/All-Hands-AI/agent-sdk.git
cd agent-sdk
make build
```

### 2. Set Up Environment Variables

```bash
# Required: LiteLLM API key for the language model
export LITELLM_API_KEY="your-litellm-api-key"

# The Notion MCP will handle OAuth authentication interactively
# No additional Notion API keys needed!
```

### 3. Navigate to Demo Directory

```bash
cd examples/notion-blog-demo
```

### 4. Run the Demo

```bash
# Interactive mode - choose your workflow
uv run python notion_blog_agent.py
```

You'll see a menu with options:
1. **Create a new blog site from Notion content** - Full workflow
2. **Add a specific Notion page as a blog post** - Single page conversion  
3. **Create a demo blog site** - Demo without Notion content

### 5. View Your Blog

After the agent completes, open `output/index.html` in your browser to see your generated blog!

## 🔧 How It Works

### The Agent Workflow

1. **Initialization**: Sets up OpenHands agent with LLM, tools, and MCP configuration
2. **Notion Connection**: Uses OAuth flow to authenticate with your Notion workspace
3. **Content Discovery**: Searches for pages/databases that could become blog posts
4. **Content Extraction**: Fetches page content, titles, metadata using Notion MCP
5. **HTML Generation**: Converts Notion content to clean HTML with consistent styling
6. **Site Assembly**: Creates index page, individual post pages, and navigation

### Key Components

- **`notion_blog_agent.py`**: Main agent orchestrating the entire workflow
- **`templates/`**: HTML/CSS/JS templates for the blog structure
- **`output/`**: Generated blog site (created during execution)

### MCP Integration Details

```python
mcp_config = {
    "mcpServers": {
        "notion": {
            "url": "https://mcp.notion.com/mcp", 
            "auth": "oauth"  # Handles authentication automatically
        },
        "fetch": {
            "command": "uvx", 
            "args": ["mcp-server-fetch"]  # For additional web requests
        }
    }
}
```

## 🎨 Customization

### Styling
- Edit `templates/style.css` to customize the blog appearance
- The CSS is designed for fast rendering with minimal complexity
- Responsive design works on desktop and mobile

### Templates
- `templates/index.html`: Main blog listing page
- `templates/post.html`: Individual blog post template
- `templates/main.js`: Interactive features and enhancements

### Agent Behavior
- Modify `notion_blog_agent.py` to change how content is processed
- Add custom prompts for different content types
- Extend with additional MCP servers for more functionality

## 🔐 Authentication Setup

### Notion OAuth (Automatic)
The Notion MCP handles OAuth authentication automatically:
1. When you first run the demo, it will open a browser window
2. Log in to your Notion account and authorize the application
3. The MCP will store the credentials securely for future use

### LiteLLM API Key
Get your API key from the LiteLLM service:
1. Sign up at the LiteLLM platform
2. Generate an API key
3. Set the `LITELLM_API_KEY` environment variable

## 📁 Project Structure

```
notion-blog-demo/
├── notion_blog_agent.py    # Main agent script
├── templates/              # Blog templates
│   ├── index.html         # Main page template
│   ├── post.html          # Blog post template
│   ├── style.css          # Styling
│   └── main.js            # JavaScript features
├── output/                # Generated blog (created at runtime)
└── README.md              # This file
```

## 🐛 Troubleshooting

### Common Issues

**"LITELLM_API_KEY not set"**
- Make sure you've exported the environment variable
- Check that the key is valid and has sufficient credits

**"Notion MCP connection failed"**
- Ensure you have internet connectivity
- Try clearing browser cookies and re-authenticating
- Check that Node.js is installed for MCP servers

**"No content found in Notion"**
- Make sure you have pages in your Notion workspace
- Check that the pages are accessible (not in trash)
- Try creating a test page with some content

**"Generated site looks broken"**
- Check the `output/` directory for generated files
- Ensure CSS and JS files were created properly
- Open browser developer tools to check for errors

### Debug Mode

Add debug logging by setting:
```bash
export OPENHANDS_LOG_LEVEL=DEBUG
```

## 🎯 Demo Scenarios

### Scenario 1: Personal Blog Migration
- Have existing content in Notion? Perfect!
- The agent will discover your pages and convert them to a blog
- Great for migrating from Notion to a static site

### Scenario 2: Content Publishing Workflow  
- Create new content in Notion (easy editing)
- Run the agent to publish to your blog (automated formatting)
- Ideal for regular content creators

### Scenario 3: Team Documentation Site
- Use Notion for collaborative writing
- Generate a public documentation site
- Keep internal editing separate from public presentation

## 🚀 Next Steps

Want to extend this demo? Try:

1. **Add more MCP servers**: Integrate GitHub, Slack, or other services
2. **Enhanced styling**: Create themes or add interactive features
3. **Deployment automation**: Add CI/CD to publish the blog automatically
4. **Content scheduling**: Add date-based publishing logic
5. **SEO optimization**: Generate meta tags, sitemaps, etc.

## 🤝 Contributing

This demo is part of the OpenHands Agent SDK project. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the same terms as the OpenHands Agent SDK.

## 🙏 Acknowledgments

- **OpenHands Team** for the amazing Agent SDK
- **Notion** for the MCP integration
- **Model Context Protocol** for the standardized interface
- **Hackathon participants** for pushing the boundaries of AI agents

---

**Happy hacking! 🚀**

*Built with ❤️ using OpenHands SDK and Notion MCP*