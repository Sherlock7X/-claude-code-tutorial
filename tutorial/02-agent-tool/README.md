# Step 2: The Agent Tool — Fan Out Independent Work

## What is the Agent Tool?

Claude Code has a built-in `Agent` tool that spawns **independent sub-agents**.
Each sub-agent is a separate Claude instance with its own context window.
They run in parallel and return their results to you (the main agent).

## When to Use It

| Scenario | Solo Claude | With Agent Tool |
|----------|-------------|-----------------|
| Review 5 files for bugs | Read one by one (slow) | 5 agents review in parallel (fast) |
| Research 3 topics | Search sequentially | 3 agents search simultaneously |
| Code + Tests + Docs | Write one at a time | All three in parallel |

## How It Works (Mental Model)

```
┌─────────────────────────────────────┐
│         YOU (Main Agent)            │
│                                     │
│  "Analyze this project"             │
│                                     │
│    ┌──────────┐  ┌──────────┐      │
│    │ Agent 1  │  │ Agent 2  │      │
│    │ Review   │  │ Review   │      │
│    │ Security │  │ Perf     │      │
│    └────┬─────┘  └────┬─────┘      │
│         │              │            │
│         ▼              ▼            │
│    "3 vulns"     "2 slow queries"   │
│         │              │            │
│         └──────┬───────┘            │
│                ▼                    │
│         Synthesize results          │
└─────────────────────────────────────┘
```

## Practical Example: Parallel Code Analysis

Instead of telling you about it, let's DO it. Here are prompts you can type
RIGHT NOW in Claude Code to see the Agent tool in action:

### Example 1: Parallel File Analysis

**You type:**
> "Use 3 agents to analyze this project: one reviews the Readme.md for clarity,
> one checks for security issues, and one suggests performance improvements.
> Run them all in parallel."

**What happens:**
Claude spawns 3 sub-agents simultaneously — each gets its own context and
focuses on ONE dimension. Results come back ~3x faster than doing it sequentially.

### Example 2: Research Multiple Topics

**You type:**
> "Spawn 3 research agents in parallel:
> 1. Research best practices for Python async/await
> 2. Research common SQL injection patterns in 2024-2025
> 3. Research Docker multi-stage build optimization
> After all return, synthesize the findings into one summary."

### Example 3: Multi-Perspective Code Review

**You type:**
> "Review app.py from 4 perspectives in parallel:
> - Security reviewer: look for vulnerabilities
> - Performance reviewer: find bottlenecks
> - Readability reviewer: suggest cleaner code
> - Bug hunter: find logic errors"

### Example 4: Competitive Analysis (Web Research)

**You type:**
> "Use 3 web-search agents in parallel to research:
> - Agent 1: How does LangChain handle multi-agent orchestration?
> - Agent 2: How does CrewAI handle multi-agent orchestration?
> - Agent 3: How does AutoGen handle multi-agent orchestration?
> Then compare their approaches in a table."

## The Key Pattern

The pattern is always the same:

```
1. DECOMPOSE — Break your task into independent sub-tasks
2. DISPATCH  — Send each sub-task to its own agent (they run in parallel)
3. SYNTHESIZE — Combine the results into one coherent output
```

## What Makes a Good Agent Prompt?

A good agent prompt has:
1. **Clear role** — "You are a security reviewer..."
2. **Specific scope** — "Review ONLY the authentication logic in auth.py"
3. **Expected output** — "Return a list of vulnerabilities with severity levels"
4. **Stopping rule** — "Return your findings, do not ask follow-up questions"

### Bad prompt:
> "Look at the code and tell me what you think"

### Good prompt:
> "Review auth.py for OWASP Top 10 vulnerabilities. For each finding, report:
> the vulnerable line number, the risk type, severity (low/medium/high/critical),
> and a one-sentence fix. Return ONLY findings — no introduction or summary."

## The Agent Types Available

When using the Agent tool, you can specify agent types:

| Agent Type | Best For |
|------------|----------|
| `general-purpose` | Complex multi-step tasks |
| `Explore` | Read-only file search & discovery |
| `Plan` | Designing implementation approaches |
| `claude-code-guide` | Questions about Claude Code itself |

## Exercise: Try It Now

1. Create a dummy project with a few files:
```bash
mkdir test-project
echo "def login(user, pw): return db.query(f\"SELECT * FROM users WHERE name='{user}'\")" > test-project/app.py
echo "def process(data): return [x*2 for x in data]" > test-project/utils.py
echo "# My App\n\nA simple app." > test-project/README.md
```

2. Then type in Claude Code:
> "Use 3 agents in parallel to review the files in test-project/:
> one for security, one for performance, one for documentation quality"

3. Watch them run simultaneously and see the synthesized results!

## Pro Tip: You Can Ask Me to Use Agents

Any time you have independent tasks, just ask:
> "Use agents to do X, Y, and Z in parallel"

I'll automatically decompose, dispatch, and synthesize for you.
