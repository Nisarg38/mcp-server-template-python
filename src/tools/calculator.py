"""Calculator tool for MCP server."""

import math
from typing import Any, Dict, List, Optional, Union

from mcp.server.fastmcp import ToolDef

# Simple function-based tool instead of class-based
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

# Define tool metadata
calculator_tool = ToolDef(
    id="calculator",
    name="Calculator",
    description="Perform basic mathematical operations",
    function=calculator_add,
)
