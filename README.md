# MCP Server Template (Python)

A complete boilerplate for creating Model Context Protocol (MCP) servers in Python.

## Features

- **Ready-to-use template**: Just clone, customize, and deploy.
- **MCP SDK integration**: Built on the official Python SDK for Model Context Protocol.
- **Example resources**: Includes sample tools, resources, and prompts.
- **Docker support**: Containerized deployment with a pre-configured Dockerfile.
- **Best practices**: Follows Python packaging standards and MCP server patterns.

## Getting Started

### Prerequisites

- Python 3.10 or later

### Installation

1. **Clone and customize**:
   
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/mcp-server-template-python.git your-project-name
   cd your-project-name
   
   # Install in development mode
   pip install -e ".[dev]"
   ```

2. **Run your server**:

   ```bash
   # Run directly with Python
   python -m src.main

   # Or use the installed CLI
   mcp-server-template
   ```

3. **Connect to your server**:
   
   Your MCP server will be available at:
   - HTTP: http://localhost:8080
   - Stdio/CLI: `mcp-server-template --transport stdio`

## Project Structure

```
mcp-server-template-python/
├── src/                      # Source code
│   ├── __init__.py           # Package marker
│   ├── main.py               # Server entry point
│   ├── config.py             # Configuration
│   ├── resources/            # MCP resources
│   │   ├── __init__.py
│   │   └── example.py        # Example resource
│   ├── tools/                # MCP tools
│   │   ├── __init__.py
│   │   └── calculator.py     # Example tool
│   └── utils/                # Utility functions
│       ├── __init__.py
│       └── helpers.py        # Helper functions
├── test/                     # Test directory
│   ├── __init__.py
│   ├── conftest.py           # Pytest configuration
│   └── test_server.py        # Server tests
├── pyproject.toml            # Package configuration
├── Dockerfile                # Docker configuration
├── .github/                  # GitHub Actions
│   └── workflows/
│       └── tests.yml         # CI workflow
├── .gitignore                # Git ignore file
└── README.md                 # This README
```

## Customization

1. **Change the server name**:
   - Update `name` in `pyproject.toml`
   - Rename the entry point in `[project.scripts]`
   - Update imports in your code

2. **Add your resources**:
   - Add new modules in `src/resources/`
   - Register them in `src/main.py`

3. **Add your tools**:
   - Add new tool modules in `src/tools/`
   - Register them in `src/main.py`

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src tests
isort src tests

# Type checking
mypy src
```

## Docker Deployment

```bash
# Build the Docker image
docker build -t your-mcp-server .

# Run the container
docker run -p 8080:8080 your-mcp-server
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## About MCP

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Learn more at [modelcontextprotocol.io](https://modelcontextprotocol.io).
