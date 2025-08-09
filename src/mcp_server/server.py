"""MCP Server Main Entry Point"""

import asyncio
import json
import sys
from typing import Any, Dict
from mcp.server import Server
from mcp.types import Tool, TextContent
from .handlers.tools import ToolHandler
from .handlers.resources import ResourceHandler


class MCPServer:
    def __init__(self):
        self.server = Server("hackathon-mcp-server")
        self.tool_handler = ToolHandler()
        self.resource_handler = ResourceHandler()
        self._setup_handlers()

    def _setup_handlers(self):
        """Setup MCP protocol handlers"""
        
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            return self.tool_handler.get_available_tools()

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> list[TextContent]:
            return await self.tool_handler.call_tool(name, arguments)

    async def run(self):
        """Run the MCP server"""
        async with self.server.run_stdio() as streams:
            await streams.read_loop()


async def main():
    """Main entry point"""
    server = MCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())