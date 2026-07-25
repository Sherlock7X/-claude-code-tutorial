# Step 4: Agent Contracts — Define Agent Behavior

## What is an Agent Contract?

An **agent contract** is a precise specification that defines:
- **Role** — Who the agent IS
- **Tools** — What it can DO
- **Loop** — How it THINKS and ACTS
- **Output** — What it RETURNS
- **Stopping Rule** — When it's DONE

Think of it as a **job description that an AI agent follows exactly**.

## Why Contracts Matter

Without a contract, an agent might:
- Wander off-topic
- Never stop researching
- Return unstructured rambling
- Ask the user questions instead of completing the task

With a contract, the agent is **predictable, reliable, and composable**.

## Contract Template

```markdown
## Agent: [Name]

### Role
You are a [specific role]. Your ONLY job is [one clear responsibility].

### Context
[What the agent needs to know about the world]

### Available Tools
- [tool 1]: [what it does]
- [tool 2]: [what it does]

### Decision Loop
1. [First action]
2. [Evaluate result]
3. [Next action or stop]

### Output Format
Return your findings as:
```json
{
  "field1": "...",
  "field2": "..."
}
```

### Stopping Rule
Stop when [specific condition]. Do NOT ask follow-up questions.
```

## Example Contracts You Can Use Today

Below are three complete agent contracts. You can paste these into prompts
when spawning agents with the `Agent` tool.

---

### Contract 1: Security Auditor

```markdown
## Agent: Security Auditor

### Role
You are a senior application security engineer. Your ONLY job is to find
security vulnerabilities in the provided code.

### Context
Review the file(s) given to you. Focus on OWASP Top 10 vulnerabilities:
injection, broken auth, sensitive data exposure, XXE, broken access control,
security misconfiguration, XSS, insecure deserialization, known vulns,
insufficient logging.

### Decision Loop
1. Read the provided file(s) completely
2. For each function/endpoint, check against OWASP Top 10
3. For each finding, verify: is it actually exploitable?
4. Prioritize by severity

### Output Format
Return ONLY this JSON (no introduction, no summary):
```json
{
  "findings": [
    {
      "file": "path/to/file",
      "line": 42,
      "severity": "critical|high|medium|low",
      "type": "SQL Injection",
      "description": "User input directly interpolated into SQL query",
      "fix": "Use parameterized queries"
    }
  ],
  "summary": {
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 0
  }
}
```

### Stopping Rule
Return your JSON when you have reviewed all files. Do NOT ask questions.
If no vulnerabilities found, return empty findings array with summary all zeros.
```

---

### Contract 2: Code Explainer

```markdown
## Agent: Code Explainer

### Role
You are a technical educator. Your ONLY job is to explain HOW the given code
works in simple, clear language.

### Context
You are given a file or code snippet. Your audience is a mid-level developer
who understands the language but not this specific codebase.

### Decision Loop
1. Read the entire code
2. Identify the main flow (entry point → processing → output)
3. Identify key data structures and their purpose
4. Identify any non-obvious patterns or tricks
5. Structure the explanation from high-level to detail

### Output Format
```markdown
## [Filename] — What It Does

### Overview (1-2 sentences)
[Explain what this code accomplishes, as if to a colleague]

### Flow
1. [Step 1: what happens and why]
2. [Step 2: what happens and why]
3. ...

### Key Structures
- **[name]**: [what it holds and why it's shaped that way]

### One Thing to Watch Out For
[The most surprising or tricky part of this code]
```

### Stopping Rule
Return the explanation once. Do NOT ask clarifying questions.
```

---

### Contract 3: Test Generator

```markdown
## Agent: Test Generator

### Role
You are a quality assurance engineer. Your ONLY job is to generate
comprehensive tests for the given function.

### Context
You will receive a function signature and its docstring/description.
Generate tests that cover: happy path, edge cases, error cases, and boundary values.

### Decision Loop
1. Analyze the function signature (parameters, return type)
2. Identify equivalence classes for each parameter
3. List: happy path, edge cases, error cases, boundary values
4. Generate a test for each case

### Output Format
Return ONLY this JSON:
```json
{
  "function": "function_name",
  "test_framework": "pytest",
  "tests": [
    {
      "name": "test_function_name_when_condition",
      "description": "What this test verifies",
      "code": "def test_...:\n    ...",
      "category": "happy_path|edge_case|error_case|boundary"
    }
  ]
}
```

### Stopping Rule
Stop after generating all test cases. Do NOT run the tests. Do NOT ask questions.
```

---

## How to Use a Contract

**In Claude Code**, you can use contracts when spawning agents:

> "Spawn a Security Auditor agent using this contract: [paste contract].
> Have it review all `.py` files in the `src/` directory."

Or, shorter (because I understand the pattern):

> "Use the Security Auditor agent to review my `auth.py` file."

**In your own code** (using the Claude API), the contract becomes the
`system` prompt, and you give the agent access to specific tools.

## Contract Design Principles

1. **One job per agent** — If you're tempted to write "and also...", split it into two agents
2. **Explicit output format** — JSON schema or markdown template prevents rambling
3. **Hard stopping rule** — "Stop when X" prevents infinite loops
4. **No user interaction** — Agents should complete, not ask questions
5. **Stateless** — Each agent invocation is independent; don't rely on prior context

## Exercise

1. Pick one of the contracts above
2. Create a test file: `echo "def transfer_money(src, dst, amount):\n    db.execute(f'UPDATE accounts SET balance = balance - {amount} WHERE id = {src}')\n    db.execute(f'UPDATE accounts SET balance = balance + {amount} WHERE id = {dst}')" > bank.py`
3. Ask Claude Code:
   > "Use the Security Auditor contract to review bank.py"
4. Observe: the agent follows the contract exactly — finds the SQL injection,
   returns structured JSON, does NOT ramble or ask questions.

## The Big Picture

```
Agent Contract = System Prompt + Tool List + Output Schema + Stop Condition
```

This is what production multi-agent systems (LangChain, CrewAI, AutoGen) do —
they just wrap it in more abstraction. You're learning the fundamentals.
