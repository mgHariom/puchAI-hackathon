"""Tests for Bus Route Tools"""

import pytest
from src.mcp_server.handlers.tools import ToolHandler
from src.mcp_server.utils.whatsapp_parser import parse_bus_query


@pytest.mark.asyncio
async def test_bus_route_tool():
    """Test bus route functionality"""
    handler = ToolHandler()
    result = await handler.call_tool("bus_route", {
        "from_location": "downtown",
        "to_location": "airport"
    })
    assert "A1/B2" in result[0].text
    assert "15 km" in result[0].text


@pytest.mark.asyncio
async def test_whatsapp_bus_query():
    """Test WhatsApp message parsing"""
    handler = ToolHandler()
    result = await handler.call_tool("whatsapp_bus_query", {
        "message": "I want to go from downtown to airport"
    })
    assert "A1/B2" in result[0].text


def test_parse_bus_query():
    """Test message parsing"""
    result = parse_bus_query("I want to go from downtown to airport")
    assert result["from_location"] == "downtown"
    assert result["to_location"] == "airport"