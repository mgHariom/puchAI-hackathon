# MCP Server Setup Guide

## Project Overview
This hackathon project builds a Python-based Model Context Protocol (MCP) server to extend MCP client functionalities.

## Installation Steps

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python -m src.mcp_server.server
```

## Project Structure Created
- `src/mcp_server/` - Main server code
- `docs/` - Documentation
- `tests/` - Test files
- `requirements.txt` - Python dependencies
- `pyproject.toml` - Project configuration

## Next Steps
1. Review the development guide in `docs/development.md`
2. Check the API documentation in `docs/api.md`
3. Start implementing your MCP server handlers