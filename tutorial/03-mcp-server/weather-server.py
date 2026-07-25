"""
My First MCP Server — three tools backed by real I/O.

  get_weather  — live data from Open-Meteo (free, no API key)
  calculate    — safe AST-based math evaluator (no eval())
  save_note /
  get_note     — reads/writes a real notes.json on disk

Run:
    pip install mcp httpx
    python weather-server.py

Then add to .claude/settings.json and restart Claude Code.
"""

import asyncio
import json
from pathlib import Path

import httpx
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationCapabilities
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("my-first-mcp")

NOTES_FILE = Path(__file__).parent / "notes.json"

# WMO weather-code → human label
_WMO = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Icy fog",
    51: "Light drizzle", 53: "Drizzle", 55: "Heavy drizzle",
    61: "Light rain", 63: "Rain", 65: "Heavy rain",
    71: "Light snow", 73: "Snow", 75: "Heavy snow",
    80: "Rain showers", 81: "Moderate showers", 82: "Violent showers",
    95: "Thunderstorm", 96: "Thunderstorm + hail",
}


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_weather",
            description=(
                "Get LIVE current weather for any city. "
                "Uses Open-Meteo (free, no API key needed). "
                "Returns temperature in °F, conditions, and wind speed."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name, e.g. 'Tokyo' or 'São Paulo'",
                    }
                },
                "required": ["city"],
            },
        ),
        Tool(
            name="calculate",
            description=(
                "Safely evaluate a math expression using Python's AST parser. "
                "Supports +, -, *, /, ** and parentheses. No eval() is used."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression, e.g. '(3 + 4) ** 2 / 2'",
                    }
                },
                "required": ["expression"],
            },
        ),
        Tool(
            name="save_note",
            description=(
                "Save a named note to notes.json on disk. "
                "Notes survive between Claude sessions — real persistent memory."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Note name"},
                    "value": {"type": "string", "description": "Note content"},
                },
                "required": ["key", "value"],
            },
        ),
        Tool(
            name="get_note",
            description="Read a previously saved note from notes.json.",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Note name to retrieve"}
                },
                "required": ["key"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:

    # ── Tool 1: real weather via Open-Meteo ───────────────────────
    if name == "get_weather":
        city = arguments["city"]
        async with httpx.AsyncClient() as client:
            # Step 1: city name → latitude/longitude
            geo_resp = await client.get(
                "https://geocoding-api.open-meteo.com/v1/search",
                params={"name": city, "count": 1, "language": "en", "format": "json"},
                timeout=10,
            )
            geo_resp.raise_for_status()
            results = geo_resp.json().get("results")
            if not results:
                return [TextContent(type="text", text=f"City not found: {city!r}")]

            lat = results[0]["latitude"]
            lon = results[0]["longitude"]
            canonical = results[0]["name"]
            country = results[0].get("country", "")

            # Step 2: coordinates → current weather
            wx_resp = await client.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "current_weather": True,
                    "temperature_unit": "fahrenheit",
                    "wind_speed_unit": "mph",
                },
                timeout=10,
            )
            wx_resp.raise_for_status()
            cw = wx_resp.json()["current_weather"]

        condition = _WMO.get(int(cw["weathercode"]), f"Code {cw['weathercode']}")
        return [TextContent(
            type="text",
            text=(
                f"{canonical}, {country}: {cw['temperature']}°F, "
                f"{condition}, wind {cw['windspeed']} mph  "
                f"[live — Open-Meteo]"
            ),
        )]

    # ── Tool 2: safe AST evaluator ─────────────────────────────────
    elif name == "calculate":
        import ast
        import operator as op

        _ops = {
            ast.Add: op.add,
            ast.Sub: op.sub,
            ast.Mult: op.mul,
            ast.Div: op.truediv,
            ast.Pow: op.pow,
            ast.USub: op.neg,
        }

        def _eval(node):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                return node.value
            if isinstance(node, ast.BinOp) and type(node.op) in _ops:
                return _ops[type(node.op)](_eval(node.left), _eval(node.right))
            if isinstance(node, ast.UnaryOp) and type(node.op) in _ops:
                return _ops[type(node.op)](_eval(node.operand))
            raise ValueError(f"Unsupported expression node: {type(node).__name__}")

        expression = arguments["expression"]
        try:
            tree = ast.parse(expression, mode="eval")
            result = _eval(tree.body)
            return [TextContent(type="text", text=f"{expression} = {result}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e}")]

    # ── Tool 3 & 4: real file-backed notes ────────────────────────
    elif name == "save_note":
        notes = json.loads(NOTES_FILE.read_text()) if NOTES_FILE.exists() else {}
        notes[arguments["key"]] = arguments["value"]
        NOTES_FILE.write_text(json.dumps(notes, indent=2))
        return [TextContent(type="text", text=f"Saved note '{arguments['key']}' to {NOTES_FILE.name}")]

    elif name == "get_note":
        if not NOTES_FILE.exists():
            return [TextContent(type="text", text="No notes saved yet.")]
        notes = json.loads(NOTES_FILE.read_text())
        key = arguments["key"]
        if key in notes:
            return [TextContent(type="text", text=f"{key}: {notes[key]}")]
        available = list(notes.keys())
        return [TextContent(type="text", text=f"Note '{key}' not found. Saved notes: {available}")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


# ── Start the server ───────────────────────────────────────────────
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationCapabilities(
                sampling={},
                experimental={},
                roots={},
            ),
            NotificationOptions(),
        )


if __name__ == "__main__":
    asyncio.run(main())
