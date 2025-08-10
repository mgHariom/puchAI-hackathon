"""MCP Server Main Entry Point"""

import asyncio
from mcp.server.stdio import stdio_server
from mcp.server import Server
from mcp.types import Tool, TextContent
from .handlers.tools import ToolHandler
from .handlers.resources import ResourceHandler


app = Server("hackathon-mcp-server")
tool_handler = ToolHandler()
resource_handler = ResourceHandler()


@app.list_tools()
async def list_tools() -> list[Tool]:
    return tool_handler.get_available_tools()


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    return await tool_handler.call_tool(name, arguments)


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())