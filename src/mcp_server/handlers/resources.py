"""Resource Handlers for MCP Server"""

from typing import Any, Dict, List
from mcp.types import Resource, TextContent


class ResourceHandler:
    def __init__(self):
        self.resources = {
            "config": {"data": "Server configuration data"},
            "status": {"data": "Server is running"}
        }

    def get_available_resources(self) -> List[Resource]:
        """Return list of available resources"""
        return [
            Resource(
                uri="resource://config",
                name="Configuration",
                description="Server configuration data"
            ),
            Resource(
                uri="resource://status",
                name="Status",
                description="Current server status"
            )
        ]

    async def read_resource(self, uri: str) -> List[TextContent]:
        """Read a specific resource"""
        resource_name = uri.replace("resource://", "")
        
        if resource_name not in self.resources:
            raise ValueError(f"Unknown resource: {resource_name}")
        
        data = self.resources[resource_name]["data"]
        return [TextContent(type="text", text=data)]