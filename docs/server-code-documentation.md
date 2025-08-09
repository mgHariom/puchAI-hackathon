# Server.py Code Documentation

## Overview
The `server.py` file is the main entry point for the MCP (Model Context Protocol) server. It handles client communication, request routing, and protocol compliance.

## Architecture Diagram

```
┌─────────────────┐    JSON-RPC     ┌─────────────────┐
│   MCP Client    │◄──────────────► │   MCP Server    │
│  (Claude, etc)  │     (stdio)     │ (server.py)     │
└─────────────────┘                 └─────────────────┘
                                             │
                                             ▼
                                    ┌─────────────────┐
                                    │   MCPServer     │
                                    │     Class       │
                                    └─────────────────┘
                                             │
                                    ┌────────┴────────┐
                                    ▼                 ▼
                            ┌─────────────┐   ┌─────────────┐
                            │ ToolHandler │   │ResourceHandler│
                            │             │   │             │
                            │ • echo      │   │ • config    │
                            │ • calculate │   │ • status    │
                            └─────────────┘   └─────────────┘
```

## Request Flow Diagram

```
1. Client Request:
   ┌─────────────┐
   │ "list_tools"│ ──────┐
   └─────────────┘       │
                         ▼
2. Server Processing:    ┌─────────────────┐
   ┌─────────────────────│ @server.list_   │
   │                     │ tools() decorator│
   │                     └─────────────────┘
   ▼                              │
3. Handler Call:                  ▼
   ┌─────────────────┐    ┌─────────────────┐
   │ ToolHandler     │◄───│ list_tools()    │
   │.get_available_  │    │ function        │
   │ tools()         │    └─────────────────┘
   └─────────────────┘
           │
           ▼
4. Response:
   ┌─────────────────┐
   │ [Tool objects]  │ ──────► Client
   └─────────────────┘
```

## Communication Protocol

```
Client ──► Server: {"method": "tools/list", "id": 1}
Server ──► Client: {"result": [{"name": "echo", ...}], "id": 1}

Client ──► Server: {"method": "tools/call", "params": {"name": "echo", "arguments": {"text": "hi"}}}
Server ──► Client: {"result": [{"type": "text", "text": "Echo: hi"}]}
```

## Code Structure

### Imports
```python
import asyncio          # Async programming support
import json            # JSON handling (unused but available)
import sys             # System utilities (unused but available)
from typing import Any, Dict  # Type hints
from mcp.server import Server  # MCP server core
from mcp.types import Tool, TextContent  # MCP data types
```

### MCPServer Class

#### `__init__(self)`
- Creates MCP server instance with name "hackathon-mcp-server"
- Initializes tool and resource handlers
- Calls `_setup_handlers()` to register protocol endpoints

#### `_setup_handlers(self)`
Sets up MCP protocol handlers using decorators:

**@self.server.list_tools()**
- Registers handler for "tools/list" requests
- Returns available tools from ToolHandler
- Client uses this to discover what tools are available

**@self.server.call_tool()**
- Registers handler for "tools/call" requests  
- Routes tool execution to ToolHandler
- Takes tool name and arguments, returns results

#### `async run(self)`
- Starts the server using stdio communication
- Creates bidirectional streams for JSON-RPC
- Runs read loop to process incoming requests

### Main Function
```python
async def main():
    server = MCPServer()
    await server.run()
```
- Creates server instance
- Starts the async server loop

### Entry Point
```python
if __name__ == "__main__":
    asyncio.run(main())
```
- Runs the server when script is executed directly
- Uses asyncio to handle async operations

## Communication Flow

1. **Client Connection**: Client connects via stdio
2. **Request Processing**: Server receives JSON-RPC requests
3. **Handler Routing**: Requests routed to registered handlers
4. **Response**: Results sent back to client as JSON-RPC responses

## Protocol Handlers

| Handler | Purpose | Returns |
|---------|---------|---------|
| `list_tools()` | List available tools | Array of Tool objects |
| `call_tool()` | Execute a specific tool | Array of TextContent |

## Error Handling
- MCP library handles protocol-level errors
- Tool-specific errors handled in ToolHandler
- Server crashes bubble up to main()

## Extension Points
- Add new handlers in `_setup_handlers()`
- Extend ToolHandler for new tools
- Add ResourceHandler integration for resources