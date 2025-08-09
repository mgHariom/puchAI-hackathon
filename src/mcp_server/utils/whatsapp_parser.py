"""WhatsApp Message Parser for Bus Route Queries"""

import re
from typing import Dict, Optional


def parse_bus_query(message: str) -> Optional[Dict[str, str]]:
    """Parse WhatsApp message to extract from/to locations"""
    
    # Pattern: "I want to go from X to Y"
    pattern1 = r"(?:i want to go|going|travel)\s+from\s+(.+?)\s+to\s+(.+?)(?:\.|$|\?)"
    
    # Pattern: "from X to Y bus"
    pattern2 = r"from\s+(.+?)\s+to\s+(.+?)\s+(?:bus|route)"
    
    # Pattern: "X to Y bus route"
    pattern3 = r"(.+?)\s+to\s+(.+?)\s+(?:bus|route)"
    
    message_lower = message.lower().strip()
    
    for pattern in [pattern1, pattern2, pattern3]:
        match = re.search(pattern, message_lower)
        if match:
            from_loc = match.group(1).strip()
            to_loc = match.group(2).strip()
            
            # Clean up common words
            from_loc = re.sub(r'\b(place|area|location)\b', '', from_loc).strip()
            to_loc = re.sub(r'\b(place|area|location)\b', '', to_loc).strip()
            
            return {
                "from_location": from_loc,
                "to_location": to_loc
            }
    
    return None


def format_bus_response(bus_info: str) -> str:
    """Format response for WhatsApp"""
    return f"🚌 {bus_info}"