"""Tool Handlers for MCP Server"""

from typing import Any, Dict, List
from mcp.types import Tool, TextContent


class ToolHandler:
    def __init__(self):
        self.tools = {
            "echo": self._echo_tool,
            "calculate": self._calculate_tool,
            "bus_route": self._bus_route_tool,
            "whatsapp_bus_query": self._whatsapp_bus_query_tool,
        }
        self._init_bus_data()

    def get_available_tools(self) -> List[Tool]:
        """Return list of available tools"""
        return [
            Tool(
                name="echo",
                description="Echo back the input text",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "Text to echo"}
                    },
                    "required": ["text"]
                }
            ),
            Tool(
                name="calculate",
                description="Perform basic arithmetic calculations",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "expression": {"type": "string", "description": "Math expression to evaluate"}
                    },
                    "required": ["expression"]
                }
            ),
            Tool(
                name="bus_route",
                description="Find bus routes between two locations",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "from_location": {"type": "string", "description": "Starting location"},
                        "to_location": {"type": "string", "description": "Destination location"}
                    },
                    "required": ["from_location", "to_location"]
                }
            ),
            Tool(
                name="whatsapp_bus_query",
                description="Parse WhatsApp message to find bus routes from natural language",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "description": "WhatsApp message asking for bus route"}
                    },
                    "required": ["message"]
                }
            )
        ]

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> List[TextContent]:
        """Call a specific tool"""
        if name not in self.tools:
            raise ValueError(f"Unknown tool: {name}")
        
        return await self.tools[name](arguments)

    async def _echo_tool(self, args: Dict[str, Any]) -> List[TextContent]:
        """Echo tool implementation"""
        text = args.get("text", "")
        return [TextContent(type="text", text=f"Echo: {text}")]

    async def _calculate_tool(self, args: Dict[str, Any]) -> List[TextContent]:
        """Calculate tool implementation"""
        expression = args.get("expression", "")
        try:
            result = eval(expression)  # Note: In production, use a safer eval
            return [TextContent(type="text", text=f"Result: {result}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]

    def _init_bus_data(self):
        """Initialize bus route data"""
self.bus_routes = {
    ("majestic", "kempegowda_airport"): {"bus": "KIA-8", "distance": "35 km", "time": "70 min", "cost": "$3.00", "start_stop": "Kempegowda Bus Station", "drop_stop": "Airport Terminal"},
    ("hebbal", "kempegowda_airport"): {"bus": "KIA-5", "distance": "30 km", "time": "60 min", "cost": "$2.80", "start_stop": "Hebbal Bus Stand", "drop_stop": "Airport Terminal"},
    ("yelahanka", "kempegowda_airport"): {"bus": "KIA-4", "distance": "20 km", "time": "45 min", "cost": "$2.00", "start_stop": "Yelahanka Old Town", "drop_stop": "Airport Terminal"},
    ("majestic", "whitefield"): {"bus": "335E", "distance": "20 km", "time": "65 min", "cost": "$1.50", "start_stop": "Kempegowda Bus Station", "drop_stop": "Vydehi Hospital"},
    ("majestic", "electronic_city"): {"bus": "356C", "distance": "18 km", "time": "60 min", "cost": "$1.20", "start_stop": "Kempegowda Bus Station", "drop_stop": "Infosys EC Phase 1"},
    ("koramangala", "kempegowda_airport"): {"bus": "KIA-6", "distance": "42 km", "time": "90 min", "cost": "$3.50", "start_stop": "Koramangala BDA Complex", "drop_stop": "Airport Terminal"},
    ("banashankari", "majestic"): {"bus": "210", "distance": "10 km", "time": "30 min", "cost": "$0.60", "start_stop": "Banashankari TTMC", "drop_stop": "Kempegowda Bus Station"},
    ("indiranagar", "whitefield"): {"bus": "500C", "distance": "16 km", "time": "50 min", "cost": "$1.00", "start_stop": "Indiranagar Police Station", "drop_stop": "ITPL Main Gate"},
    ("indiranagar", "majestic"): {"bus": "138", "distance": "6 km", "time": "25 min", "cost": "$0.50", "start_stop": "Indiranagar BDA Complex", "drop_stop": "Kempegowda Bus Station"},
    ("mg_road", "whitefield"): {"bus": "335E", "distance": "18 km", "time": "55 min", "cost": "$1.50", "start_stop": "MG Road Metro", "drop_stop": "Vydehi Hospital"},
    ("mg_road", "hebbal"): {"bus": "290", "distance": "14 km", "time": "45 min", "cost": "$1.00", "start_stop": "MG Road Metro", "drop_stop": "Hebbal Bus Stand"},
    ("btm_layout", "electronic_city"): {"bus": "356W", "distance": "10 km", "time": "35 min", "cost": "$0.80", "start_stop": "BTM Layout 16th Main", "drop_stop": "Infosys EC Phase 2"},
    ("hsr_layout", "whitefield"): {"bus": "500D", "distance": "15 km", "time": "50 min", "cost": "$1.00", "start_stop": "HSR BDA Complex", "drop_stop": "ITPL Main Gate"},
    ("banashankari", "hebbal"): {"bus": "500N", "distance": "20 km", "time": "65 min", "cost": "$1.50", "start_stop": "Banashankari TTMC", "drop_stop": "Hebbal Bus Stand"},
    ("kr_puram", "kempegowda_airport"): {"bus": "KIA-9", "distance": "32 km", "time": "70 min", "cost": "$2.80", "start_stop": "KR Puram Railway Station", "drop_stop": "Airport Terminal"},
    ("malleshwaram", "majestic"): {"bus": "66", "distance": "4 km", "time": "15 min", "cost": "$0.30", "start_stop": "Malleshwaram 18th Cross", "drop_stop": "Kempegowda Bus Station"},
    ("malleshwaram", "whitefield"): {"bus": "500K", "distance": "28 km", "time": "80 min", "cost": "$1.80", "start_stop": "Malleshwaram 18th Cross", "drop_stop": "Vydehi Hospital"},
    ("koramangala", "whitefield"): {"bus": "500C", "distance": "22 km", "time": "75 min", "cost": "$1.50", "start_stop": "Koramangala BDA Complex", "drop_stop": "ITPL Main Gate"},
    ("koramangala", "electronic_city"): {"bus": "356K", "distance": "12 km", "time": "40 min", "cost": "$0.80", "start_stop": "Koramangala BDA Complex", "drop_stop": "Infosys EC Phase 1"},
    ("silk_board", "whitefield"): {"bus": "500P", "distance": "20 km", "time": "65 min", "cost": "$1.40", "start_stop": "Silk Board Junction", "drop_stop": "ITPL Main Gate"},
    ("silk_board", "hebbal"): {"bus": "500N", "distance": "28 km", "time": "80 min", "cost": "$1.80", "start_stop": "Silk Board Junction", "drop_stop": "Hebbal Bus Stand"},
    ("silk_board", "kempegowda_airport"): {"bus": "KIA-7", "distance": "50 km", "time": "110 min", "cost": "$3.80", "start_stop": "Silk Board Junction", "drop_stop": "Airport Terminal"},
    ("kengeri", "majestic"): {"bus": "222", "distance": "15 km", "time": "50 min", "cost": "$1.00", "start_stop": "Kengeri TTMC", "drop_stop": "Kempegowda Bus Station"},
    ("kengeri", "whitefield"): {"bus": "500W", "distance": "35 km", "time": "100 min", "cost": "$2.00", "start_stop": "Kengeri TTMC", "drop_stop": "Vydehi Hospital"},
    ("rajajinagar", "majestic"): {"bus": "82", "distance": "5 km", "time": "20 min", "cost": "$0.40", "start_stop": "Rajajinagar ESI", "drop_stop": "Kempegowda Bus Station"},
    ("rajajinagar", "hebbal"): {"bus": "290", "distance": "12 km", "time": "40 min", "cost": "$0.80", "start_stop": "Rajajinagar ESI", "drop_stop": "Hebbal Bus Stand"},
    ("banaswadi", "whitefield"): {"bus": "500S", "distance": "15 km", "time": "55 min", "cost": "$1.00", "start_stop": "Banaswadi Railway Station", "drop_stop": "ITPL Main Gate"},
    ("banaswadi", "hebbal"): {"bus": "280", "distance": "8 km", "time": "25 min", "cost": "$0.60", "start_stop": "Banaswadi Railway Station", "drop_stop": "Hebbal Bus Stand"},
    ("jayanagar", "majestic"): {"bus": "210", "distance": "8 km", "time": "25 min", "cost": "$0.60", "start_stop": "Jayanagar 4th Block", "drop_stop": "Kempegowda Bus Station"},
    ("jayanagar", "whitefield"): {"bus": "500E", "distance": "25 km", "time": "85 min", "cost": "$1.60", "start_stop": "Jayanagar 4th Block", "drop_stop": "Vydehi Hospital"},
    ("marathahalli", "whitefield"): {"bus": "335E", "distance": "8 km", "time": "20 min", "cost": "$0.60", "start_stop": "Marathahalli Bridge", "drop_stop": "Vydehi Hospital"},
    ("marathahalli", "hebbal"): {"bus": "500D", "distance": "24 km", "time": "75 min", "cost": "$1.50", "start_stop": "Marathahalli Bridge", "drop_stop": "Hebbal Bus Stand"},
    ("whitefield", "hebbal"): {"bus": "500N", "distance": "26 km", "time": "85 min", "cost": "$1.60", "start_stop": "ITPL Main Gate", "drop_stop": "Hebbal Bus Stand"},
    ("whitefield", "kempegowda_airport"): {"bus": "KIA-8W", "distance": "45 km", "time": "100 min", "cost": "$3.20", "start_stop": "ITPL Main Gate", "drop_stop": "Airport Terminal"},
    ("itpl", "majestic"): {"bus": "335E", "distance": "22 km", "time": "75 min", "cost": "$1.50", "start_stop": "ITPL Main Gate", "drop_stop": "Kempegowda Bus Station"},
    ("itpl", "hebbal"): {"bus": "500N", "distance": "27 km", "time": "85 min", "cost": "$1.70", "start_stop": "ITPL Main Gate", "drop_stop": "Hebbal Bus Stand"},
    ("itpl", "electronic_city"): {"bus": "500K", "distance": "30 km", "time": "90 min", "cost": "$2.00", "start_stop": "ITPL Main Gate", "drop_stop": "Infosys EC Phase 1"},
    ("hebbal", "electronic_city"): {"bus": "500N", "distance": "30 km", "time": "95 min", "cost": "$2.00", "start_stop": "Hebbal Bus Stand", "drop_stop": "Infosys EC Phase 1"},
    ("hebbal", "btm_layout"): {"bus": "500L", "distance": "22 km", "time": "75 min", "cost": "$1.50", "start_stop": "Hebbal Bus Stand", "drop_stop": "BTM Layout 16th Main"},
    ("silk_board", "btm_layout"): {"bus": "356B", "distance": "3 km", "time": "10 min", "cost": "$0.20", "start_stop": "Silk Board Junction", "drop_stop": "BTM Layout 16th Main"},
    ("silk_board", "electronic_city"): {"bus": "356C", "distance": "10 km", "time": "30 min", "cost": "$0.70", "start_stop": "Silk Board Junction", "drop_stop": "Infosys EC Phase 1"},
    ("banashankari", "electronic_city"): {"bus": "356BN", "distance": "22 km", "time": "75 min", "cost": "$1.50", "start_stop": "Banashankari TTMC", "drop_stop": "Infosys EC Phase 1"},
    ("banashankari", "whitefield"): {"bus": "500BM", "distance": "28 km", "time": "90 min", "cost": "$1.80", "start_stop": "Banashankari TTMC", "drop_stop": "ITPL Main Gate"},
    ("majestic", "hsr_layout"): {"bus": "356HS", "distance": "14 km", "time": "50 min", "cost": "$1.00", "start_stop": "Kempegowda Bus Station", "drop_stop": "HSR BDA Complex"},
    ("hsr_layout", "kempegowda_airport"): {"bus": "KIA-12", "distance": "48 km", "time": "105 min", "cost": "$3.60", "start_stop": "HSR BDA Complex", "drop_stop": "Airport Terminal"},
    ("btm_layout", "kempegowda_airport"): {"bus": "KIA-10", "distance": "45 km", "time": "100 min", "cost": "$3.50", "start_stop": "BTM Layout 16th Main", "drop_stop": "Airport Terminal"}
}

    async def _bus_route_tool(self, args: Dict[str, Any]) -> List[TextContent]:
        """Bus route finder tool"""
        from_loc = args.get("from_location", "").lower().strip()
        to_loc = args.get("to_location", "").lower().strip()
        
        # Check direct route
        route_key = (from_loc, to_loc)
        reverse_key = (to_loc, from_loc)
        
        if route_key in self.bus_routes:
            route = self.bus_routes[route_key]
        elif reverse_key in self.bus_routes:
            route = self.bus_routes[reverse_key]
        else:
            return [TextContent(type="text", text=f"No direct bus route found from {from_loc} to {to_loc}. Please check available routes or contact local transport.")]
        
        response = f"{route['bus']} is the bus you have to take to reach {to_loc}. Distance: {route['distance']}. Estimated time: {route['time']}. Estimated cost: {route['cost']}"
        return [TextContent(type="text", text=response)]

    async def _whatsapp_bus_query_tool(self, args: Dict[str, Any]) -> List[TextContent]:
        """Parse WhatsApp message and find bus route"""
        from ..utils.whatsapp_parser import parse_bus_query, format_bus_response
        
        message = args.get("message", "")
        parsed = parse_bus_query(message)
        
        if not parsed:
            return [TextContent(type="text", text="I couldn't understand your request. Please ask like: 'I want to go from downtown to airport'")]
        
        # Use existing bus route logic
        route_result = await self._bus_route_tool(parsed)
        response = format_bus_response(route_result[0].text)
        
        return [TextContent(type="text", text=response)]