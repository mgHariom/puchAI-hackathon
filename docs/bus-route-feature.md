# Bus Route Feature Documentation

## Overview
Added WhatsApp-compatible bus route finder that parses natural language queries and provides route information.

## Features Added

### 1. Bus Route Tool (`bus_route`)
- **Purpose**: Find direct bus routes between locations
- **Input**: `from_location`, `to_location`
- **Output**: Bus number, distance, time, cost

### 2. WhatsApp Bus Query Tool (`whatsapp_bus_query`)
- **Purpose**: Parse natural language WhatsApp messages
- **Input**: Raw WhatsApp message text
- **Output**: Formatted bus route response

### 3. Message Parser (`whatsapp_parser.py`)
- Extracts locations from natural language
- Supports patterns like:
  - "I want to go from X to Y"
  - "from X to Y bus route"
  - "X to Y bus"

## Sample Data
Current routes available:
- Downtown ↔ Airport: A1/B2 (15km, 45min, $3.50)
- Mall ↔ University: C3/D4 (8km, 25min, $2.00)
- Station ↔ Hospital: E5 (12km, 35min, $2.75)

## Usage Examples

### Direct Tool Call:
```json
{
  "method": "tools/call",
  "params": {
    "name": "bus_route",
    "arguments": {
      "from_location": "downtown",
      "to_location": "airport"
    }
  }
}
```

### WhatsApp Message:
```json
{
  "method": "tools/call",
  "params": {
    "name": "whatsapp_bus_query",
    "arguments": {
      "message": "I want to go from downtown to airport"
    }
  }
}
```

### Response:
```
🚌 A1/B2 is the bus you have to take to reach airport. Distance: 15 km. Estimated time: 45 min. Estimated cost: $3.50
```

## Integration Points
- Can be connected to WhatsApp Business API
- Compatible with any MCP client
- Extensible route database