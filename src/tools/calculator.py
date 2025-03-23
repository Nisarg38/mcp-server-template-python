"""Calculator tool for MCP server."""

import math
from typing import Any, Dict, List, Optional, Union

from mcp.server.fastmcp.tools.base import Tool, ToolParameter, register_tool


class CalculatorTool(Tool):
    """A simple calculator tool that can perform basic math operations."""

    def __init__(self) -> None:
        """Initialize the calculator tool."""
        super().__init__(
            tool_id="calculator",
            name="Calculator",
            description="Perform basic mathematical operations",
        )

    @register_tool(
        description="Add two numbers together",
        parameters=[
            ToolParameter(
                name="a", description="First number", type="number", required=True
            ),
            ToolParameter(
                name="b", description="Second number", type="number", required=True
            ),
        ],
    )
    async def add(self, a: float, b: float) -> Dict[str, Any]:
        """Add two numbers."""
        result = a + b
        return {
            "result": result,
            "operation": "addition",
            "expression": f"{a} + {b} = {result}",
        }
