# Step 1: SKILL.md — Teach Claude One Repeatable Task

## What is a SKILL.md?

A SKILL.md is a file you place at `.claude/skills/<name>/SKILL.md`. It teaches Claude
HOW to do a specific task. Once created, you invoke it by typing `/<name>` in Claude Code.

Think of it as: **"Here's my checklist — follow it every time."**

## Anatomy of a SKILL.md

```markdown
---
name: my-skill-name
description: One-line summary of what this skill does
---

# Skill: My Skill Name

## When to use
- When the user asks for X
- When files matching Y are changed

## Instructions
1. Step one — do this first
2. Step two — then this
3. Step three — finally this

## Output format
- Always produce: [describe expected output]
```

## Your First Skill: `doc-reviewer`

Below is a complete, working skill. Let's create it together.

### Step 1: Create the skill file

Create this directory structure:
```
.claude/skills/doc-reviewer/
└── SKILL.md
```

### Step 2: Write the SKILL.md

Copy the content below into `.claude/skills/doc-reviewer/SKILL.md`:

---

```markdown
---
name: doc-reviewer
description: Review documentation files for clarity, completeness, and correctness
---

# Skill: Documentation Reviewer

## When to use
- User says "review this doc" or "check my documentation"
- User asks for feedback on README, docs, or markdown files
- User mentions `/doc-reviewer`

## Instructions

### 1. Read the document
Read the entire file the user points to (or ask which file if unclear).

### 2. Check these dimensions:
- **Clarity**: Is it written in plain language? Are sentences under 25 words?
- **Completeness**: Does it answer: What? Why? How? When to use?
- **Structure**: Does it have headings, bullet points, and code examples where needed?
- **Correctness**: Are commands, file paths, and code snippets accurate?
- **Audience**: Is it clear WHO this document is for?

### 3. Produce a review report:
```
## Doc Review: [filename]

### Score: X/5

### What's Good
- [at least 2 positive things]

### What to Improve
- [specific, actionable suggestions]

### Missing
- [anything the doc should cover but doesn't]
```
```

---

### Step 3: Try it out!

Once the file is created, type this in Claude Code:
```
/doc-reviewer Readme.md
```

Claude will follow the skill's instructions and produce a structured review.

## Key Insight

A SKILL.md **constrains Claude's behavior** — instead of Claude guessing how you want
something done, you encode your preferences once and reuse them forever.

### Real-world skill ideas:
- `/code-review` — your team's specific review checklist
- `/release-checklist` — steps before every release
- `/onboard-newbie` — explain the codebase to a new team member
- `/weekly-report` — generate your weekly status report from git history

## Exercise

1. Create `.claude/skills/doc-reviewer/SKILL.md` with the content above
2. Create a test file: `echo "# My Project\n\nThis is a test doc." > test-doc.md`
3. Run: `/doc-reviewer test-doc.md`
4. Observe how Claude follows your checklist exactly
