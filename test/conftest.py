"""Pytest configuration for MCP Server Template tests."""

import math
from typing import Any, Dict, List

import pytest
import pytest_asyncio
from mcp.server.fastmcp import FastMCP

from src.config import config

# Set the default fixture loop scope for the async fixtures
pytest_asyncio.default_fixture_loop_scope = "function"


@pytest_asyncio.fixture
async def mcp_server():
    """Create and configure a test MCP server instance."""
    # Create a new MCP server instance with metadata
    server = FastMCP(
        name=config.name,
        version="0.1.0-test",
        description=config.description,
        icon="🧪",  # Test icon
        metadata={"test": True},
    )

    # Define resources
    @server.resource("http://localhost/programming/languages")
    def languages_resource() -> Dict[str, Any]:
        """Get a list of programming languages."""
        return {
            "languages": [
                {
                    "name": "Python",
                    "creator": "Guido van Rossum",
                    "year": 1991,
                    "description": "Python is a high-level, general-purpose programming language.",
                },
                {
                    "name": "TypeScript",
                    "creator": "Microsoft",
                    "year": 2012,
                    "description": "TypeScript is a strongly typed programming language that builds on JavaScript.",
                },
                {
                    "name": "Rust",
                    "creator": "Graydon Hoare",
                    "year": 2010,
                    "description": "Rust is a multi-paradigm, high-level, general-purpose programming language.",
                },
            ]
        }

    @server.resource("http://localhost/programming/languages/{language_id}")
    def language_detail(language_id: str) -> Dict[str, Any]:
        """Get details for a specific programming language."""
        languages = {
            "python": {
                "name": "Python",
                "creator": "Guido van Rossum",
                "year": 1991,
                "paradigms": [
                    "object-oriented",
                    "imperative",
                    "functional",
                    "procedural",
                ],
                "description": "Python is a high-level, general-purpose programming language.",
            },
            "typescript": {
                "name": "TypeScript",
                "creator": "Microsoft",
                "year": 2012,
                "paradigms": ["object-oriented", "functional"],
                "description": "TypeScript is a strongly typed programming language that builds on JavaScript.",
            },
            "rust": {
                "name": "Rust",
                "creator": "Graydon Hoare",
                "year": 2010,
                "paradigms": ["concurrent", "functional", "imperative", "structured"],
                "description": "Rust is a multi-paradigm, high-level, general-purpose programming language.",
            },
        }

        language_id = language_id.lower()
        if language_id not in languages:
            return {"error": f"Language {language_id} not found"}

        return languages[language_id]

    # Define tools
    @server.tool()
    def add(a: float, b: float) -> Dict[str, Any]:
        """Add two numbers together."""
        result = a + b
        return {
            "result": result,
            "operation": "addition",
            "expression": f"{a} + {b} = {result}",
        }

    @server.tool()
    def subtract(a: float, b: float) -> Dict[str, Any]:
        """Subtract second number from first number."""
        result = a - b
        return {
            "result": result,
            "operation": "subtraction",
            "expression": f"{a} - {b} = {result}",
        }

    @server.tool()
    def multiply(a: float, b: float) -> Dict[str, Any]:
        """Multiply two numbers."""
        result = a * b
        return {
            "result": result,
            "operation": "multiplication",
            "expression": f"{a} × {b} = {result}",
        }

    @server.tool()
    def divide(a: float, b: float) -> Dict[str, Any]:
        """Divide first number by second number."""
        if b == 0:
            return {
                "error": "Division by zero is not allowed",
                "operation": "division",
                "expression": f"{a} ÷ {b} = undefined",
            }

        result = a / b
        return {
            "result": result,
            "operation": "division",
            "expression": f"{a} ÷ {b} = {result}",
        }

    # Define prompts
    @server.prompt()
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

    @server.prompt()
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

    return server
