"""Tests for the MCP Server Template."""

import json
import pytest
from mcp import ServerCapabilities
from typing import List


@pytest.mark.asyncio(loop_scope="function")
async def test_server_info(mcp_server):
    """Test that the MCP server is properly initialized with basic properties."""
    # Verify server has a name
    assert mcp_server.name == "MCP Server Template"
    
    # Verify server has metadata
    assert hasattr(mcp_server, "name")
    assert isinstance(mcp_server.name, str)


@pytest.mark.asyncio(loop_scope="function")
async def test_calculator_tools(mcp_server):
    """Test that calculator tools are properly registered and work."""
    # Check that tools are registered
    tools = await mcp_server.list_tools()
    
    # Tools are objects with properties
    tool_names = [tool.name for tool in tools]
    assert "add" in tool_names
    
    # Test add function
    add_result = await mcp_server.call_tool("add", {"a": 5, "b": 7})
    
    # Check that we got a response with TextContent
    assert len(add_result) > 0
    assert hasattr(add_result[0], 'text')
    
    # Parse the JSON response
    response_data = json.loads(add_result[0].text)
    assert response_data["result"] == 12
    assert response_data["operation"] == "addition"
    assert "5" in response_data["expression"] and "7" in response_data["expression"] and "12" in response_data["expression"]


@pytest.mark.asyncio(loop_scope="function")
async def test_language_resources(mcp_server):
    """Test that language resources are properly registered and accessible."""
    # List resources
    resources = await mcp_server.list_resources()
    
    # Resources are objects with uri property
    resource_uris = [str(resource.uri) for resource in resources]
    assert "http://localhost/programming/languages" in resource_uris
    
    # Verify we can access both the list and individual languages
    # Test languages list
    languages_response = await mcp_server.read_resource("http://localhost/programming/languages")
    
    # Check that we got a response with content
    assert len(languages_response) > 0
    assert hasattr(languages_response[0], 'content')
    
    # Parse the JSON response
    languages_data = json.loads(languages_response[0].content)
    assert "languages" in languages_data
    assert len(languages_data["languages"]) >= 3
    
    # Test specific language
    python_response = await mcp_server.read_resource("http://localhost/programming/languages/python")
    assert len(python_response) > 0
    assert hasattr(python_response[0], 'content')
    
    python_data = json.loads(python_response[0].content)
    assert python_data["name"] == "Python"
    assert python_data["creator"] == "Guido van Rossum"
    
    # Test non-existent language
    invalid_response = await mcp_server.read_resource("http://localhost/programming/languages/brainfuck")
    assert len(invalid_response) > 0
    assert hasattr(invalid_response[0], 'content')
    
    invalid_data = json.loads(invalid_response[0].content)
    assert "error" in invalid_data


@pytest.mark.asyncio(loop_scope="function")
async def test_prompts(mcp_server):
    """Test that prompt templates are properly registered."""
    # Check prompt templates are registered
    prompts = await mcp_server.list_prompts()
    
    # Prompts are objects with properties
    prompt_names = [prompt.name for prompt in prompts]
    assert "math_problem" in prompt_names
    assert "language_comparison" in prompt_names
    
    # Test math problem prompt
    math_prompt_response = await mcp_server.get_prompt("math_problem", {"problem": "Solve for x: 2x + 5 = 13"})
    
    # Check that we got a response with messages
    assert hasattr(math_prompt_response, 'messages')
    assert len(math_prompt_response.messages) > 0
    assert hasattr(math_prompt_response.messages[0], 'content')
    assert hasattr(math_prompt_response.messages[0].content, 'text')
    
    math_text = math_prompt_response.messages[0].content.text
    assert "Please solve this mathematical problem" in math_text
    assert "Solve for x: 2x + 5 = 13" in math_text
    
    # Test language comparison prompt
    lang_prompt_response = await mcp_server.get_prompt("language_comparison", {"languages": ["Python", "JavaScript", "Go"]})
    
    # Check that we got a response with messages
    assert hasattr(lang_prompt_response, 'messages')
    assert len(lang_prompt_response.messages) > 0
    assert hasattr(lang_prompt_response.messages[0], 'content')
    assert hasattr(lang_prompt_response.messages[0].content, 'text')
    
    lang_text = lang_prompt_response.messages[0].content.text
    assert "Please compare the following programming languages: Python, JavaScript, Go" in lang_text 