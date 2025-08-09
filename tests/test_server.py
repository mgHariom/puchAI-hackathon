"""Tests for MCP Server"""

import pytest
import asyncio
from src.mcp_server.handlers.tools import ToolHandler
from src.mcp_server.handlers.resources import ResourceHandler


@pytest.mark.asyncio
async def test_echo_tool():
    """Test echo tool functionality"""
    handler = ToolHandler()
    result = await handler.call_tool("echo", {"text": "Hello World"})
    assert len(result) == 1
    assert "Hello World" in result[0].text


@pytest.mark.asyncio
async def test_calculate_tool():
    """Test calculate tool functionality"""
    handler = ToolHandler()
    result = await handler.call_tool("calculate", {"expression": "2 + 2"})
    assert len(result) == 1
    assert "4" in result[0].text


@pytest.mark.asyncio
async def test_resource_handler():
    """Test resource handler functionality"""
    handler = ResourceHandler()
    result = await handler.read_resource("resource://status")
    assert len(result) == 1
    assert "running" in result[0].text