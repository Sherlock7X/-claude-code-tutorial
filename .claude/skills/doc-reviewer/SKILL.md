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
