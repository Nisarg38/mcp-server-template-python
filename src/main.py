"""MCP Server entry point."""

import argparse
import asyncio
import logging
import math
import sys
from enum import Enum
from typing import Any, Dict, List, Optional

import uvicorn
from mcp.server.fastmcp import FastMCP

from src.config import config
from src.utils import get_version, setup_logging

# Configure logging
logger = logging.getLogger(__name__)

# Define transport enum
class Transport(Enum):
    """Transport options for the MCP server."""
    HTTP = "http"
    STDIO = "stdio"

# Create the MCP server
mcp = FastMCP(
    name=config.name,
    version=get_version(),
    description=config.description,
    icon="🚀",  # Optional server icon
    metadata=config.metadata,
)


# Define tools
@mcp.tool()
def add(a: float, b: float) -> Dict[str, Any]:
    """Add two numbers together."""
    result = a + b
    return {
        "result": result,
        "operation": "addition",
        "expression": f"{a} + {b} = {result}",
    }


# Define prompts
@mcp.prompt()
def math_problem(problem: str) -> str:
    """Create a prompt for solving a math problem."""
    return f"""Please solve this mathematical problem:

Problem: {problem}

Steps:
1. Understand what the problem is asking
2. Identify the mathematical concepts involved
3. Solve step-by-step
4. Verify your answer

Answer:"""


@mcp.prompt()
def language_comparison(languages: List[str]) -> str:
    """Create a prompt for comparing programming languages."""
    language_list = ", ".join(languages)
    return f"""Please compare the following programming languages: {language_list}

For each language, please discuss:
- Key features and strengths
- Common use cases
- Ecosystem and community
- Performance characteristics

Then provide a concise comparison highlighting when each would be the best choice for different scenarios."""


async def run_server(
    port: int = config.port,
    host: str = config.host,
    transport: Transport = Transport.HTTP,
    debug: bool = config.debug,
) -> None:
    """Run the MCP server.

    Args:
        port: The port to listen on for HTTP transport.
        host: The host to bind to for HTTP transport.
        transport: The transport type (HTTP or stdio).
        debug: Whether to enable debug mode.
    """
    # Run the server with the specified transport
    if transport == Transport.STDIO:
        logger.info("Starting MCP server with stdio transport")
        # Use asyncio.StreamReader/StreamWriter instead of stdin_stdout_transport
        # This is a placeholder - implement based on MCP library requirements
        raise NotImplementedError("stdio transport not implemented in this version")
    else:
        logger.info(f"Starting MCP server at http://{host}:{port}")
        # FastAPI app integration
        config_dict = uvicorn.Config(
            app=mcp.app,  # Use .app instead of get_app()
            host=host,
            port=port,
            log_level="debug" if debug else "info",
        )
        server = uvicorn.Server(config_dict)
        await server.serve()


def run_cli() -> None:
    """Run the server from the command line interface."""
    parser = argparse.ArgumentParser(description="MCP Server Template")
    parser.add_argument(
        "--port", type=int, default=config.port, help="HTTP server port (default: 8080)"
    )
    parser.add_argument(
        "--host",
        type=str,
        default=config.host,
        help="HTTP server host (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--transport",
        type=str,
        choices=["http", "stdio"],
        default="http",
        help="Transport type (default: http)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["debug", "info", "warning", "error", "critical"],
        default=config.log_level,
        help="Set logging level (default: info)",
    )
    parser.add_argument(
        "--version", action="store_true", help="Show version information and exit"
    )

    args = parser.parse_args()

    if args.version:
        print(f"{config.name} v{get_version()}")
        sys.exit(0)

    # Set up logging
    setup_logging(args.log_level)

    # Determine transport type
    transport_type = Transport.STDIO if args.transport == "stdio" else Transport.HTTP

    # Run the server
    try:
        asyncio.run(
            run_server(
                port=args.port,
                host=args.host,
                transport=transport_type,
                debug=args.debug,
            )
        )
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Error running server: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    run_cli()
