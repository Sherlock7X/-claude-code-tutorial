# Step 5: Orchestration — The Main Agent Pattern

## What is Orchestration?

Orchestration is when a **main agent** (the "orchestrator") dispatches work to
specialized sub-agents, monitors their progress, and synthesizes their results.

```
                         ┌──────────────┐
                         │  ORCHESTRATOR │  "Analyze this codebase"
                         │  (Main Agent) │
                         └──────┬───────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
        ┌───────▼──────┐ ┌─────▼──────┐ ┌──────▼──────┐
        │  SECURITY    │ │  PERF      │ │  DOCS       │
        │  AUDITOR     │ │  ANALYZER  │ │  REVIEWER   │
        │  (Agent 1)   │ │  (Agent 2) │ │  (Agent 3)  │
        └───────┬──────┘ └─────┬──────┘ └──────┬──────┘
                │               │               │
                └───────────────┼───────────────┘
                                │
                        ┌───────▼───────┐
                        │   SYNTHESIS   │  Combined report
                        │   (Main Agent)│
                        └───────────────┘
```

## Three Orchestration Patterns

### Pattern 1: Parallel Fan-Out (Simplest)

All agents work independently. Orchestrator just collects and merges results.

**When to use:** Tasks that don't depend on each other.

```python
# Pseudocode for what happens when you ask Claude:
# "Review my project for security, performance, and docs quality"

# Claude (the orchestrator) spawns:
agents = [
    Agent("Review all .py files for security vulnerabilities"),
    Agent("Review all .py files for performance issues"),
    Agent("Review all .md files for documentation quality"),
]

# All three run IN PARALLEL
results = await asyncio.gather(*agents)

# Claude synthesizes the results into one report
```

**Try it:**
> "Use 3 agents in parallel: one audits security, one checks performance,
> one reviews docs. Then give me a single combined report."

---

### Pattern 2: Pipeline (Sequential Dependencies)

Each agent's output feeds into the next agent.

**When to use:** Tasks that build on each other.

```
Research ──► Design ──► Implement ──► Review
```

**Try it:**
> "I need a function that validates email addresses.
> Step 1: Agent 1 — Research best practices for email validation
> Step 2: Agent 2 — Design the function API and test cases (based on Agent 1's research)
> Step 3: Agent 3 — Write the implementation (based on Agent 2's design)
> Step 4: Agent 4 — Review the code for bugs (check Agent 3's work)"

---

### Pattern 3: Debate / Judge Panel (Adversarial)

Multiple agents tackle the SAME problem from different angles, then a
judge agent picks the best approach or synthesizes them.

**When to use:** High-stakes decisions, creative work, complex analysis.

```
Agent 1: "Build with approach A (microservices)"
Agent 2: "Build with approach B (monolith)"
Agent 3: "Build with approach C (serverless)"
         │               │               │
         └───────────────┼───────────────┘
                         │
                  ┌──────▼──────┐
                  │    JUDGE    │
                  │  (Agent 4)  │
                  └──────┬──────┘
                         │
                  Final recommendation
                  with pros/cons of each
```

**Try it:**
> "I need to design a user authentication system. Spawn 3 agents to propose
> different approaches (JWT, session-based, OAuth-only). Then spawn a 4th
> agent to compare them and recommend the best approach for a startup with
> 1000 users."

---

## The Orchestrator's Job

A good orchestrator agent does these 5 things:

```
1. DECOMPOSE    Break the goal into independent sub-tasks
2. CONTRACT     Assign each sub-task to a specialized agent with a clear contract
3. DISPATCH     Launch agents in parallel where possible
4. MONITOR      Check for failures, timeouts, or incomplete results
5. SYNTHESIZE   Merge results, resolve conflicts, produce final output
```

## Real Orchestration in Claude Code

Claude Code has a built-in **Workflow** tool for complex orchestration.
Here's what a workflow script looks like:

```javascript
export const meta = {
  name: 'codebase-audit',
  description: 'Full audit: security, perf, docs, and architecture',
  phases: [
    { title: 'Audit' },
    { title: 'Verify' },
    { title: 'Report' }
  ]
}

// Phase 1: Parallel audit
phase('Audit')
const dimensions = ['security', 'performance', 'docs', 'architecture']
const findings = await pipeline(
  dimensions,
  dim => agent(`Review the codebase for ${dim} issues`, {
    label: `audit:${dim}`,
    phase: 'Audit'
  })
)

// Phase 2: Verify each finding
phase('Verify')
const verified = await pipeline(
  findings.flat(),
  finding => agent(`Verify this finding: ${finding}`, {
    label: `verify:${finding.title}`,
    phase: 'Verify'
  })
)

// Phase 3: Synthesize
phase('Report')
const report = await agent(
  `Synthesize these verified findings into an executive summary`,
  { phase: 'Report' }
)
```

To run a workflow, save it as `.claude/workflows/audit.js` and type:
> `/workflows run audit`

Or even simpler — just ask Claude:
> "Run a full audit of this project. Use multiple agents in parallel, then
> verify each finding, and give me a final report."

## Common Orchestration Mistakes

| Mistake | Fix |
|---------|-----|
| Agents depend on each other but run in parallel | Use pipeline pattern |
| Agents have no output format | Use contracts (Step 4) |
| Orchestrator doesn't handle failures | Add: "If agent fails, note it and continue" |
| Too many agents (100+) | Batch into groups of 5-10 |
| Agents ask questions instead of completing | Add hard stopping rules (Step 4) |
| No synthesis step | Always end with "combine these results into..." |

## Exercise: Build Your First Orchestration

1. Create a small project with 3-5 files (mix of .py and .md)
2. Ask Claude Code:
   > "Orchestrate a full project review:
   > - Phase 1: 3 agents review security, performance, and docs in parallel
   > - Phase 2: 1 agent verifies all findings from Phase 1
   > - Phase 3: 1 agent synthesizes everything into an executive summary
   > Report any agent failures but continue with remaining agents."

3. Observe how:
   - Phase 1 agents run simultaneously
   - Phase 2 waits for all Phase 1 results
   - Phase 3 produces the final polished output
   - Failures in one agent don't block others

## The Full Picture

```
SKILL.md          teaches ONE agent ONE repeatable task
    │
    ▼
Agent Tool        spawns MANY agents for parallel work
    │
    ▼
MCP Server        gives agents CUSTOM TOOLS (database, API, etc.)
    │
    ▼
Agent Contracts   defines agent BEHAVIOR precisely
    │
    ▼
Orchestration     coordinates MANY agents with complex DEPENDENCIES
```

You've now learned all five levels. Start simple (SKILL.md), use it daily,
then climb the ladder as your needs grow.
