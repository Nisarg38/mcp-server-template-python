# MCP Server Template (Python)

A ready-to-use template for building Model Context Protocol (MCP) servers in Python.

## What is MCP?

The Model Context Protocol (MCP) enables seamless integration between LLM applications and external tools, data sources, and prompts. This template gives you everything you need to create your own MCP server.

## Quick Start

### Prerequisites

- Python 3.10+

### Setup in 3 Steps

1. **Install the package**:
   
   ```bash
   # Clone the repository
   git clone https://github.com/nisarg38/mcp-server-template-python.git my-mcp-server
   cd my-mcp-server
   
   # Install in development mode
   pip install -e ".[dev]"
   ```

2. **Run your server**:

   ```bash
   # Run with Python
   python -m src.main
   
   # Or use the CLI
   mcp-server-template
   ```

3. **Your server is now live!**
   
   Access your MCP server at:
   - HTTP: http://localhost:8080
   - Use the stdio transport: `mcp-server-template --transport stdio`

## Command Line Options

```bash
# Change port
mcp-server-template --port 9000

# Enable debug mode
mcp-server-template --debug

# Use stdio transport instead of HTTP
mcp-server-template --transport stdio

# Set logging level
mcp-server-template --log-level debug
```

## Adding Your Own Tools and Prompts

### Add a Tool

Edit `src/main.py` and add a new tool function:

```python
@mcp.tool()
def your_tool_name(param1: str, param2: int) -> Dict[str, Any]:
    """Your tool description."""
    # Your tool logic here
    return {"result": "your result"}
```

### Add a Prompt

Edit `src/main.py` and add a new prompt function:

```python
@mcp.prompt()
def your_prompt_name(param: str) -> str:
    """Your prompt description."""
    return f"""
    Your formatted prompt with {param} inserted
    """
```

## Project Structure

```
src/                      # Source code
├── main.py               # Server entry point with tools & prompts
├── config.py             # Configuration settings
├── utils/                # Utility functions
├── tools/                # Tools functions
└── resources/            # Resource definitions
test/                     # Tests directory
pyproject.toml            # Package configuration
Dockerfile                # Docker support
```

## Docker Deployment

```bash
# Build and run with Docker
docker build -t my-mcp-server .
docker run -p 8080:8080 my-mcp-server
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src test
isort src test
```

## Need Help?

- MCP Documentation: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- File an issue: [GitHub Issues](https://github.com/nisarg38/mcp-server-template-python/issues)
