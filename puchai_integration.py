"""PuchAI MCP Integration Script"""

import json
import os
import subprocess
import sys

def setup_puchai_integration():
    """Setup integration with PuchAI MCP server"""
    
    # Configuration for PuchAI
    config = {
        "server_name": "bus-route-server",
        "description": "Bangalore Bus Route Finder with WhatsApp Integration",
        "tools": [
            {
                "name": "whatsapp_bus_query",
                "description": "Find bus routes from WhatsApp messages",
                "example": "I want to go from majestic to whitefield"
            },
            {
                "name": "bus_route", 
                "description": "Direct bus route lookup",
                "example": "from_location: majestic, to_location: whitefield"
            }
        ],
        "command": ["python", "-m", "src.mcp_server.server"],
        "working_directory": os.getcwd()
    }
    
    print("🚌 Bus Route MCP Server Configuration:")
    print(json.dumps(config, indent=2))
    
    return config

def test_puchai_connection():
    """Test connection to PuchAI MCP server"""
    
    print("\n🔧 Testing MCP server...")
    
    # Start our MCP server
    process = subprocess.Popen(
        [sys.executable, "-m", "src.mcp_server.server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Initialize
    init_request = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "puchai-client", "version": "1.0.0"}
        }
    }
    
    process.stdin.write(json.dumps(init_request) + "\n")
    process.stdin.flush()
    
    # Read response
    response = process.stdout.readline()
    print("✅ Server initialized successfully")
    
    # Test bus route
    bus_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "whatsapp_bus_query",
            "arguments": {
                "message": "I want to go from majestic to kempegowda airport"
            }
        }
    }
    
    process.stdin.write(json.dumps(bus_request) + "\n")
    process.stdin.flush()
    
    response = process.stdout.readline()
    result = json.loads(response)
    
    if "result" in result:
        print("✅ Bus route query successful:")
        print(f"   {result['result'][0]['text']}")
    
    process.terminate()
    print("\n🎉 Ready for PuchAI integration!")

if __name__ == "__main__":
    config = setup_puchai_integration()
    test_puchai_connection()