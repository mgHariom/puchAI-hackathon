# MCP Server Development Guide

## Architecture Overview

The MCP server follows a modular architecture:

```
src/mcp_server/
├── __init__.py          # Package initialization
├── server.py            # Main server entry point
├── handlers/            # MCP protocol handlers
│   ├── __init__.py
│   ├── tools.py         # Tool handlers
│   └── resources.py     # Resource handlers
└── utils/               # Utility functions
    ├── __init__.py
    └── helpers.py
```

## Key Components

### 1. Server Core (`server.py`)
- Handles MCP protocol communication
- Manages client connections
- Routes requests to appropriate handlers

### 2. Handlers
- **Tools**: Implement custom tools/functions
- **Resources**: Manage data resources and contexts

### 3. Protocol Implementation
- JSON-RPC 2.0 based communication
- Standard MCP message types
- Error handling and validation

## Development Workflow

1. **Add New Tools**: Create handlers in `handlers/tools.py`
2. **Add Resources**: Implement in `handlers/resources.py`
3. **Test**: Use the test framework in `tests/`
4. **Document**: Update API docs in `docs/api.md`

## Coding Standards
- Follow PEP 8
- Use type hints
- Add docstrings for all functions
- Keep functions minimal and focused