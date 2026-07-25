# AgentLearn — Your Multi-Agent Tutorial

Hands-on guide to building AI agents that work for you. Each step has
**runnable examples** you can try right now in Claude Code.

## Quick Start

```bash
# Step 1 (5 min): Create your first skill
mkdir -p .claude/skills/doc-reviewer
cp tutorial/01-skill/SKILL.md .claude/skills/doc-reviewer/
# Then type: /doc-reviewer Readme.md

# Step 2 (10 min): Run parallel agents
# Type: "Use 3 agents in parallel to analyze this project"

# Step 3 (20 min): Build an MCP server
pip install mcp
# Follow tutorial/03-mcp-server/README.md

# Step 4 (15 min): Design agent contracts
# Follow tutorial/04-agent-contracts/README.md

# Step 5 (30 min): Orchestrate multiple agents
# Follow tutorial/05-orchestration/README.md
```

## The Progression

| Step | What You Learn | Time | File |
|------|---------------|------|------|
| 1 | **SKILL.md** — Teach Claude one repeatable task | 5 min | `tutorial/01-skill/` |
| 2 | **Agent Tool** — Fan out independent work in parallel | 10 min | `tutorial/02-agent-tool/` |
| 3 | **MCP Server** — Give agents custom tools | 20 min | `tutorial/03-mcp-server/` |
| 4 | **Agent Contracts** — Define agent behavior precisely | 15 min | `tutorial/04-agent-contracts/` |
| 5 | **Orchestration** — Coordinate many agents with dependencies | 30 min | `tutorial/05-orchestration/` |

## Why This Order?

```
SKILL.md         →  Encode ONE repeatable process
    │
    ▼
Agent Tool       →  Run MANY copies of that process in parallel
    │
    ▼
MCP Server       →  Give those agents CUSTOM capabilities
    │
    ▼
Agent Contracts  →  Make agent behavior PREDICTABLE and COMPOSABLE
    │
    ▼
Orchestration    →  Chain agents with DEPENDENCIES and SYNTHESIS
```

Each step solves a problem you'll hit at the previous level.

## One-Line Definitions

- **SKILL.md**: A file that says "when I ask for X, do Y checklist"
- **Agent Tool**: Spawn independent Claude instances that work in parallel
- **MCP Server**: A small program that gives Claude new tools (database, API, files)
- **Agent Contract**: A precise spec: role + tools + output format + stop condition
- **Orchestration**: A main agent that decomposes, dispatches, monitors, and synthesizes

## After This Tutorial

You'll be able to:
- [ ] Turn your team's repeatable processes into `/slash-commands`
- [ ] Run code reviews, research, and analysis 3-10x faster with parallel agents
- [ ] Connect Claude to your databases and APIs via MCP
- [ ] Design agents that behave predictably with contracts
- [ ] Build multi-agent pipelines that decompose complex work
