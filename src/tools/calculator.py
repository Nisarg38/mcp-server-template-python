"""Calculator tool for MCP server."""

import math
from typing import Any, Dict, List, Optional, Union

# Remove ToolDef import as it doesn't exist
# from mcp.server.fastmcp import ToolDef


# Simple function-based tool to be registered with @server.tool() decorator
def calculator_add(a: float, b: float) -> Dict[str, Any]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Dictionary containing result and additional information
    """
    result = a + b
    return {
        "result": result,
        "operation": "addition",
        "expression": f"{a} + {b} = {result}",
    }


# Export the calculator function for registration
calculator_tool = calculator_add
