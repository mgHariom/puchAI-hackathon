"""Simple test client for MCP server"""

import json
import subprocess
import sys

def test_mcp_server():
    # Start the MCP server
    process = subprocess.Popen(
        [sys.executable, "-m", "src.mcp_server.server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Initialize the server first
    init_request = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    process.stdin.write(json.dumps(init_request) + "\n")
    process.stdin.flush()
    
    # Read init response
    init_response = process.stdout.readline()
    print("Init response:", init_response)
    
    # Send initialized notification
    initialized = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    }
    
    process.stdin.write(json.dumps(initialized) + "\n")
    process.stdin.flush()
    
    # Test list_tools request
    # request = {
    #     "jsonrpc": "2.0",
    #     "id": 1,
    #     "method": "tools/list"
    # }
    
    # Send request
    # process.stdin.write(json.dumps(request) + "\n")
    # process.stdin.flush()
    
    # # Read response
    # response = process.stdout.readline()
    # print("Tools response:", response)
    
    # Test bus route tool
    bus_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "whatsapp_bus_query",
            "arguments": {
                "message": "I want to go from majestic to whitefield. What is the bus route?",
            }
        }
    }
    
    process.stdin.write(json.dumps(bus_request) + "\n")
    process.stdin.flush()
    
    response2 = process.stdout.readline()
    print("Bus route response:", response2)
    
    process.terminate()

if __name__ == "__main__":
    test_mcp_server()