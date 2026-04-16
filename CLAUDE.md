# Claude Code Documentation Mirror + Knowledge Graph

Local mirror of Claude Code documentation with a graphify knowledge graph layer.
Docs are updated via GitHub Actions. The graph is rebuilt manually when needed.

## Navigation

1. **Graph overview** — `graphify-out/GRAPH_REPORT.md` (god nodes, communities)
2. **Wiki articles** — `graphify-out/wiki/index.md` (one article per topic cluster)
3. **Raw docs** — `docs/{topic}.md` (full documentation pages)

Use the lightest level that answers the question. Do not read raw docs when
the wiki article suffices.

## Rebuilding the graph

```bash
python scripts/preprocess-for-graphify.py
# Then run /graphify graphify-out/.preprocessed/ --mode deep --wiki
```

## Key files

@scripts/preprocess-for-graphify.py
@skills/claude-code-docs/SKILL.md
@install.sh
@.graphifyignore
