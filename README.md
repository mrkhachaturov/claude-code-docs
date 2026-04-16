# Claude Code Documentation + Knowledge Graph

[![Last Update](https://img.shields.io/github/last-commit/mrkhachaturov/claude-code-docs/main.svg?label=docs%20updated)](https://github.com/mrkhachaturov/claude-code-docs/commits/main)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue)](https://github.com/mrkhachaturov/claude-code-docs)

Local mirror of [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/) with a [graphify](https://github.com/safishamsi/graphify) knowledge graph layer. Docs update automatically via GitHub Actions. The graph provides structured navigation so Claude can answer documentation questions from graph traversal instead of reading raw files.

Based on [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs).

## What this adds over the original

| Feature | Original (`/docs`) | This fork |
| ------- | ------------------- | --------- |
| Read a doc | Dumps full doc into context | Same, via `/docs` |
| Find relevant docs | Grep or guess | Graph traversal via `/claude-code-docs` |
| Always-on awareness | Dead PreToolUse hook | User-level rule (loads every session, ~20 lines) |
| Navigation | Flat file list | 3-level: graph report, wiki articles, raw docs |
| Cross-doc relationships | None | 409 edges, 24 hyperedges, 11 communities |

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/install.sh | bash
```

This installs to `~/.claude-code-docs` and sets up:

- `~/.claude/rules/claude-code-docs.md` -- always-on graph awareness (every session)
- `~/.claude/skills/claude-code-docs/SKILL.md` -- deep query via `/claude-code-docs`
- `~/.claude/commands/docs.md` -- direct doc reading via `/docs`

### Prerequisites

- git, jq, curl
- Claude Code
- [graphify](https://github.com/safishamsi/graphify) (optional, for rebuilding the graph): `pip install graphifyy && graphify install`

## Usage

### Graph-first query (recommended)

```text
/claude-code-docs how do hooks interact with permissions?
/claude-code-docs what are the security layers?
/claude-code-docs explain the settings hierarchy
```

Claude reads the graph report, picks the relevant wiki article, and answers from structure. Only reads raw docs when exact syntax or schemas are needed.

### Direct doc reading

```text
/docs hooks        # Read hooks.md directly
/docs mcp          # Read mcp.md directly
/docs what's new   # Recent documentation changes
/docs changelog    # Claude Code release notes
/docs -t           # Check sync status with GitHub
```

### Always-on (no command needed)

The installed rule means Claude automatically knows about the graph in every session. Ask any Claude Code question and it will consult the graph before searching raw files.

## How the graph works

110 doc files are preprocessed (JSX/HTML noise stripped, 1,928 cross-references converted to clean markdown links), then graphify extracts a knowledge graph with deep mode.

```text
graphify-out/
  GRAPH_REPORT.md    -- god nodes, communities, surprising connections (11k words)
  wiki/index.md      -- entry point to 21 topic articles (~2k words each)
  graph.json         -- queryable graph (117 nodes, 409 edges)
  graph.html         -- interactive browser visualization
```

### Three navigation levels

1. **Graph report** (`GRAPH_REPORT.md`) -- overview: which concepts are hubs, how topics cluster
2. **Wiki articles** (`wiki/`) -- one article per community with key facts extracted
3. **Raw docs** (`docs/`) -- full documentation pages, only when exact details are needed

### Rebuilding the graph

When docs change significantly:

```bash
python scripts/preprocess-for-graphify.py
# Then in Claude Code:
/graphify graphify-out/.preprocessed/ --mode deep --wiki
```

Requires `pip install graphifyy`.

## Updating

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/install.sh | bash
```

Or manually: `cd ~/.claude-code-docs && git pull`

## Uninstalling

```bash
~/.claude-code-docs/uninstall.sh
```

Also remove:

- `~/.claude/rules/claude-code-docs.md`
- `~/.claude/skills/claude-code-docs/`

## License

Documentation content belongs to Anthropic.
Knowledge graph tooling is open source.
