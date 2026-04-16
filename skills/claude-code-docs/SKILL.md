---
name: claude-code-docs
description: Query the Claude Code documentation knowledge graph. Use when asked about Claude Code features, configuration, hooks, permissions, settings, SDK, or best practices.
when_to_use: When the user asks how Claude Code works, how to configure it, what features exist, or references official documentation.
disable-model-invocation: false
allowed-tools: Read Bash Grep Glob
---

# Claude Code Documentation

Navigate the official Claude Code documentation via a knowledge graph
at `~/.claude-code-docs/graphify-out/`.

## When invoked with a question: `/claude-code-docs <question>`

Follow this exact sequence. Do not skip levels.

### Step 1 — Read the graph report

```bash
cat ~/.claude-code-docs/graphify-out/GRAPH_REPORT.md
```

Identify which **god nodes** and **communities** are relevant to the question.

### Step 2 — Read the wiki article for the relevant community

```bash
cat ~/.claude-code-docs/graphify-out/wiki/index.md
```

Pick the community article that matches. Read it:

```bash
cat ~/.claude-code-docs/graphify-out/wiki/<Community_Name>.md
```

### Step 3 — Answer from graph + wiki

Answer the question using what you found in Steps 1-2.
Cite the community and god nodes you used.

### Step 4 — Read raw docs only if needed

If the wiki article lacks a specific detail (exact JSON schema, config example,
CLI flag syntax), read the raw doc:

```bash
cat ~/.claude-code-docs/docs/<topic>.md
```

The graph node's `source_file` field tells you which doc to read.
Read only the section you need, not the whole file.

## When invoked without arguments: `/claude-code-docs`

List available topics:

```bash
cat ~/.claude-code-docs/graphify-out/wiki/index.md
```

## Graph query (advanced)

For traversal queries like "what connects hooks to permissions":

```bash
graphify query "$ARGUMENTS" --graph ~/.claude-code-docs/graphify-out/graph.json
```

Or for shortest path between two concepts:

```bash
graphify path "hooks" "permissions" --graph ~/.claude-code-docs/graphify-out/graph.json
```

Requires `graphify` CLI installed (`pip install graphifyy`).
