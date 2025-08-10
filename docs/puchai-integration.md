# PuchAI MCP Integration Guide

## Overview
This guide shows how to integrate your bus route MCP server with PuchAI's MCP client.

## Integration Steps

### 1. Server Configuration
Your MCP server is ready at:
```
Command: python -m src.mcp_server.server
Working Directory: e:/Dev_projects/Ai/puchAI-hackathon
```

### 2. Available Tools
- **whatsapp_bus_query**: Parse natural language bus queries
- **bus_route**: Direct route lookup
- **echo**: Test tool
- **calculate**: Math operations

### 3. PuchAI Configuration
Add this to PuchAI's MCP server registry:

```json
{
  "name": "bus-route-server",
  "description": "Bangalore Bus Route Finder",
  "command": ["python", "-m", "src.mcp_server.server"],
  "cwd": "e:/Dev_projects/Ai/puchAI-hackathon",
  "tools": [
    {
      "name": "whatsapp_bus_query",
      "description": "Find bus routes from WhatsApp-style messages",
      "example": "I want to go from majestic to whitefield"
    }
  ]
}
```

### 4. Test Integration
Run the integration test:
```bash
python puchai_integration.py
```

### 5. Usage Examples
Once integrated with PuchAI, users can ask:
- "I want to go from majestic to airport"
- "Bus route from indiranagar to whitefield"
- "How to reach electronic city from koramangala"

## Features
- ✅ 30+ Bangalore bus routes
- ✅ Natural language processing
- ✅ WhatsApp message parsing
- ✅ Cost, time, distance info
- ✅ Start/drop stop details

## Protocol Compliance
- JSON-RPC 2.0
- MCP Protocol 2024-11-05
- Proper initialization sequence
- Error handling