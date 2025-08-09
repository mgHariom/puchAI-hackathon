"""Helper Utility Functions"""

import json
from typing import Any, Dict


def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """Basic JSON schema validation"""
    # Minimal implementation - extend as needed
    if "required" in schema:
        for field in schema["required"]:
            if field not in data:
                return False
    return True


def format_error_response(error_code: int, message: str, request_id: str = None) -> Dict[str, Any]:
    """Format JSON-RPC error response"""
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": error_code,
            "message": message
        }
    }