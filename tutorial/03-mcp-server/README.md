# Step 3: MCP Server — Give Agents Custom Tools

## What is MCP?

**Model Context Protocol (MCP)** is how you give Claude (and its sub-agents)
access to external tools — databases, APIs, file systems, internal services.

```
┌──────────────┐     MCP Protocol      ┌──────────────────┐
│  Claude Code │ ◄──────────────────► │  Your MCP Server  │
│  (or Agent)  │   JSON-RPC over stdio │  (custom tools)   │
└──────────────┘                       └────────┬─────────┘
                                                 │
                                          ┌──────▼──────┐
                                          │  Database   │
                                          │  API        │
                                          │  Filesystem │
                                          │  Your App   │
                                          └─────────────┘
```

## Why Build an MCP Server?

Without MCP, agents can only: read files, search code, run bash commands.
With MCP, agents can: query your database, call your API, access your SaaS tools,
interact with your custom business logic.

## What's in `weather-server.py`

This tutorial server has **three real tools** — no fake data, no hardcoded dicts:

| Tool | What it actually does |
|------|-----------------------|
| `get_weather(city)` | Two live HTTP calls to Open-Meteo (free, no API key) |
| `calculate(expression)` | Safe AST-based evaluator — no `eval()` |
| `save_note(key, value)` | Writes a real `notes.json` file on disk |
| `get_note(key)` | Reads that file back — persistent across sessions |

## Step 1: Install dependencies

```bash
pip install mcp httpx
```

`mcp` is the protocol SDK. `httpx` is an async HTTP client used by `get_weather`.

## Step 2: Register the server in Claude Code

Add this to your project's `.claude/settings.json`:

```json
{
  "mcpServers": {
    "my-first-mcp": {
      "command": "python",
      "args": ["D:/codeproj/agentlearn/tutorial/03-mcp-server/weather-server.py"]
    }
  }
}
```

> **Note:** Use forward slashes even on Windows. Adjust the path if your repo is elsewhere.

## Step 3: Restart Claude Code

MCP servers are launched once at startup. After editing `settings.json`,
quit and reopen Claude Code (or run `/mcp` to check server status).

## Step 4: Try it

Ask Claude:

> "What's the current weather in Tokyo, London, and São Paulo?"

Claude calls `get_weather` three times (or in parallel via sub-agents) and returns
**live data** from the Open-Meteo API — temperatures, conditions, wind speed.

> "Calculate (2 ** 10) + (15 * 3 - 7)"

Claude calls `calculate`. The expression is parsed by Python's `ast` module —
no `eval()`, no code injection risk.

> "Save a note called 'reminder' that says 'check the deployment logs'"
> (later) "What was my reminder note?"

Claude calls `save_note` then `get_note`. Open `notes.json` in your editor —
the data is really there and survives between Claude sessions.

## How `get_weather` works under the hood

The tool makes two sequential HTTP requests to Open-Meteo's free APIs:

```
1. Geocoding API
   GET https://geocoding-api.open-meteo.com/v1/search?name=Tokyo&count=1
   → { latitude: 35.69, longitude: 139.69, name: "Tokyo", country: "Japan" }

2. Weather API
   GET https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69
                                              &current_weather=true
                                              &temperature_unit=fahrenheit
   → { current_weather: { temperature: 84.2, windspeed: 5.1, weathercode: 0 } }
```

WMO weather codes (integers) are mapped to human labels (`0 → "Clear sky"`, etc.).
This is the same pattern you'd use to wrap any REST API as an MCP tool.

## How `calculate` works under the hood

Instead of `eval(expression)` (which can execute arbitrary Python), the tool:

1. Parses the expression string into an **AST** (abstract syntax tree)
2. Recursively walks only `Constant`, `BinOp`, and `UnaryOp` nodes
3. Rejects anything else (function calls, attributes, imports, etc.)

This is the correct pattern for user-provided math expressions.

## How agents use MCP tools

Sub-agents you spawn also have access to your MCP tools:

```
Main Agent: "Get weather for 5 cities"
    │
    ├──► Agent 1: get_weather("Tokyo")   ──► real API call
    ├──► Agent 2: get_weather("London")  ──► real API call
    ├──► Agent 3: get_weather("NYC")     ──► real API call
    ├──► Agent 4: get_weather("Paris")   ──► real API call
    └──► Agent 5: get_weather("Sydney")  ──► real API call
```

## Real MCP Server Ideas

| Tool | What Agents Can Do |
|------|-------------------|
| Database query | Agent checks if a user exists, runs reports |
| Jira/Linear API | Agent creates tickets, checks sprint status |
| Slack/Discord | Agent sends notifications, reads channel history |
| Internal API | Agent queries your product's data |
| File converter | Agent converts images, PDFs, etc. |
| Git operations | Agent creates branches, reads PR status |

## Exercise

1. Install dependencies: `pip install mcp httpx`
2. Add the server to `.claude/settings.json` (see Step 2 above)
3. Restart Claude Code
4. Ask: "What's the weather in Tokyo and London right now?"
5. Verify the temperatures look realistic (not hardcoded!)
6. Ask Claude to save a note, restart Claude Code, and ask it to retrieve the note

**Stretch goal:** Add a `list_notes` tool that returns all saved note keys —
a one-liner change to `get_note` that shows how easy it is to extend an MCP server.
