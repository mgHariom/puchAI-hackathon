"""HTTP wrapper for MCP server"""

import asyncio
import json
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class MCPHTTPWrapper:
    def __init__(self):
        self.process = None
        self.initialized = False
    
    def start_mcp_server(self):
        if not self.process:
            self.process = subprocess.Popen(
                ["python", "-m", "src.mcp_server.server"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self._initialize()
    
    def _initialize(self):
        init_request = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "http-wrapper", "version": "1.0.0"}
            }
        }
        
        self.process.stdin.write(json.dumps(init_request) + "\n")
        self.process.stdin.flush()
        self.process.stdout.readline()  # Read init response
        
        initialized = {"jsonrpc": "2.0", "method": "notifications/initialized"}
        self.process.stdin.write(json.dumps(initialized) + "\n")
        self.process.stdin.flush()
        
        self.initialized = True
    
    def send_request(self, method, params=None):
        if not self.initialized:
            self.start_mcp_server()
        
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params or {}
        }
        
        self.process.stdin.write(json.dumps(request) + "\n")
        self.process.stdin.flush()
        
        response = self.process.stdout.readline()
        return json.loads(response)

wrapper = MCPHTTPWrapper()

@app.route('/bus-route', methods=['POST'])
def bus_route():
    data = request.json
    message = data.get('message', '')
    
    response = wrapper.send_request(
        "tools/call",
        {
            "name": "whatsapp_bus_query",
            "arguments": {"message": message}
        }
    )
    
    return jsonify(response)

@app.route('/tools', methods=['GET'])
def list_tools():
    response = wrapper.send_request("tools/list")
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)