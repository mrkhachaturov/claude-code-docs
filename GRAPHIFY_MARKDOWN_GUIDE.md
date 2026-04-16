# Building High-Quality Graphify Graphs on Markdown Docs

Lessons from building a 797-node graph on 110 markdown files (Anthropic's
Claude Code documentation). This guide captures the pitfalls and the fixes,
so the next markdown-heavy project doesn't repeat them.

## TL;DR

```
1. Preprocess first    → strip JSX/HTML/identical headers, convert cross-refs
2. Chunk semantically  → related docs together, not alphabetical
3. Extract concepts    → NOT one node per file — 15-30 concepts per dense doc
4. Add cross-chunk pass → second subagent densifies the graph with SDK↔CLI
                         mirror edges, settings↔feature edges, etc.
5. Fix confidence labels → subagents write "high"/"medium"; must be
                           EXTRACTED/INFERRED/AMBIGUOUS
```

## Why markdown graphs are tricky

Code corpora extract well automatically: tree-sitter AST gives you classes,
functions, imports, call graphs for free. No LLM cost, no ambiguity.

Markdown corpora depend entirely on semantic extraction via LLM subagents.
Quality is a function of **how you prompt those subagents**, not of graphify
itself. Default prompts produce one fat node per file — useless.

## The phases

### Phase 1 — Preprocess

Most markdown corpora have two categories of noise that destroy graph quality:

**Identical headers** — doc sites often stamp every page with a 3-line
"Documentation Index" blockquote or similar. Strip it. Otherwise every file
shares identical tokens and creates false similarity signals.

**JSX/MDX components** — `<Tip>`, `<Warning>`, `<Note>`, `<Steps>`, `<Tab>`,
`<Frame>`, `<CodeGroup>`, `<Card>`. Strip the tags, keep the content. Strip
embedded React (`export const` blocks, `useState`, `useEffect`) — they're
presentation noise.

**CDN image URLs** — long hashes waste subagent tokens. Replace `<img alt="X"/>`
with `[Image: X]`.

**Cross-references** — this is the most important transformation. Site-local
links like `/en/docs/hooks` or `../guides/permissions` should convert to clean
markdown: `[text](hooks.md)` or `[text](permissions.md)`. Subagents parse these
as EXTRACTED edges. Without conversion, the subagent treats them as URLs and
ignores them.

See [scripts/preprocess-for-graphify.py](scripts/preprocess-for-graphify.py)
for a full implementation. For your own corpus, adapt the tag lists and URL
patterns.

Write preprocessed copies to `graphify-out/.preprocessed/` so the originals
stay untouched (CI can still update them independently).

### Phase 2 — Detect

Run graphify's detect on the preprocessed directory, not raw:

```python
from graphify.detect import detect
from pathlib import Path
result = detect(Path("graphify-out/.preprocessed"))
```

Verify word count dropped ~15% after preprocessing. If not, your regex missed
something. Spot-check 3-4 cleaned files — look for leftover JSX.

### Phase 3 — Chunking (the most overlooked step)

Default chunking is alphabetical and stupid. You want **semantic chunks** so
each subagent sees a coherent subsystem and can extract cross-doc edges within
its chunk.

Group files by what they're about, not what they're named:

| Chunk | Files | Why together |
|-------|-------|-------------|
| SDK core | overview, python, typescript, sessions, streaming | Same API surface |
| SDK features | hooks, permissions, MCP, plugins, skills, subagents | Same mental model |
| Security | hooks, permissions, sandboxing, security, auth | Same threat model |
| Configuration | settings, env-vars, model-config, claude-directory | Same concept (config) |
| Extensions | mcp, plugins, skills, sub-agents, commands, memory | Cross-cutting layer |
| Platforms | vs-code, jetbrains, desktop, chrome, cloud providers | Same user choice |
| Getting started | overview, quickstart, setup, common-workflows | Same onboarding journey |
| Operations | costs, monitoring, troubleshooting, CI/CD | Same ops concern |

Aim for **8-10 chunks of 10-15 files each**. Too many small chunks = no
cross-doc edges found. Too few large chunks = subagent context overflows.

### Phase 4 — Concept-level extraction (the critical fix)

**The single biggest quality lever.** The default graphify prompt says "extract
named concepts, entities, citations" — but subagents will default to one node
per file unless you're explicit.

Bad prompt (one node per doc):
```
Read the files. Extract a knowledge graph. Output JSON with nodes and edges.
```

Good prompt (concepts within each doc):
```
Each document contains MULTIPLE concepts. Extract each concept as its own node.
A document like hooks.md (15k words) should produce 20+ nodes, NOT 1.

Examples of concepts to extract as separate nodes:
- Each hook event: PreToolUse, PostToolUse, SessionStart, Stop, etc.
- Each permission mode: default, acceptEdits, auto, dontAsk, bypassPermissions
- Each settings scope: managed, user, project, local
- Each env var: CLAUDE_CODE_USE_BEDROCK, ANTHROPIC_API_KEY, etc.

Node ID format: filestem_conceptname (e.g., hooks_pretooluse_event)
```

Give the subagent concrete examples from the files it's processing. Without
examples, it will still collapse docs into single nodes.

For each chunk, tell the subagent:
1. The files it's reading
2. Example concepts to extract from those specific files
3. The node ID format (`filestem_conceptname` — matches graphify's
   expected `id` pattern)
4. What edges to add (references for explicit markdown links,
   conceptually_related_to for inferred links)

Dispatch ALL chunks **in parallel in a single message** — multiple Agent tool
calls in one response. Subagent type must be `general-purpose` (not Explore —
Explore is read-only, cannot write chunk files to disk, silently drops results).

### Phase 5 — The cross-chunk edge pass (non-obvious but critical)

After Phase 4, your graph will have dense intra-chunk edges but sparse
cross-chunk edges. Subagent A doesn't know that Subagent B created a node
named `hooks_pretooluse` — so no edge between `agent_sdk__hooks_pretooluse`
(chunk 2) and `hooks_pretooluse` (chunk 3) even though they're semantically
identical.

Fix: dispatch ONE follow-up subagent with access to all node IDs. It reads
the full node index (grouped by source file) and adds 300-500 cross-file edges.

```python
import json
from collections import defaultdict
from pathlib import Path

data = json.loads(Path("graphify-out/.graphify_extract.json").read_text())
by_file = defaultdict(list)
for n in data["nodes"]:
    by_file[n["source_file"]].append({"id": n["id"], "label": n["label"]})

Path("graphify-out/.node_index.json").write_text(json.dumps(
    [{"file": f, "nodes": nodes} for f, nodes in by_file.items()]
))
```

Then dispatch a subagent with explicit instructions to ONLY use existing node
IDs and ONLY cross-file edges. Common cross-file patterns:

- **SDK ↔ CLI mirror pairs** — `agent_sdk__hooks_pretooluse` ↔ `hooks_pretooluse`
  (relation: `semantically_similar_to`, confidence: INFERRED)
- **Settings keys → feature docs** — `settings_hooks_key` ↔ `hooks_lifecycle`
- **Env vars → providers** — `env_vars_claude_code_use_bedrock` ↔
  `amazon_bedrock_setup`
- **Commands → features** — `commands_permissions_slash` ↔
  `permissions_mode_default`

This single pass typically adds more edges than the entire first phase.

### Phase 6 — Fix confidence labels (gotcha)

Subagents frequently write `"confidence": "high"` or `"medium"` instead of
`EXTRACTED`/`INFERRED`/`AMBIGUOUS`. Graphify silently drops those edges. You
can lose 30-60% of edges to this bug and not notice.

Fix: post-process using `confidence_score` to infer the correct label:

```python
for e in data["edges"]:
    if e.get("confidence") not in ("EXTRACTED", "INFERRED", "AMBIGUOUS"):
        score = e.get("confidence_score", 0.5)
        if score >= 0.9:
            e["confidence"] = "EXTRACTED"
        elif score >= 0.4:
            e["confidence"] = "INFERRED"
        else:
            e["confidence"] = "AMBIGUOUS"
```

You can also strengthen the subagent prompt ("NEVER use 'high' or 'medium';
use only EXTRACTED/INFERRED/AMBIGUOUS"), but the post-process is belt-and-
braces.

### Phase 7 — Build, cluster, validate

Standard graphify pipeline: `build_from_json` → `cluster` → `analyze` →
`generate` → `to_json` → `to_html` → `to_wiki`.

Then **validate quality**:

```python
from collections import Counter
degrees = [d for _, d in G.degree()]
dcounts = Counter(degrees)
isolated = dcounts.get(0, 0) + dcounts.get(1, 0)
print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
print(f"Isolated (degree<=1): {isolated} ({isolated*100//G.number_of_nodes()}%)")
print(f"Edges per node: {G.number_of_edges()/G.number_of_nodes():.2f}")
```

**Quality thresholds:**
- Edges per node: **> 1.5** (aim for 2+). Below 1 means the graph is a
  forest, not a graph.
- Isolated nodes (degree ≤ 1): **< 25%**. Above 40% means extraction was
  too shallow or cross-chunk pass was missing.
- Nodes per file: **3-10+ for dense docs**. A 15k-word doc should have ≥15
  nodes. A 2k-word doc might reasonably have 3-5.

If any threshold fails, go back to Phase 4 or 5.

## What a good graph looks like

For a 110-doc, 318k-word markdown corpus, aim for:
- 500-1000 concept nodes (not 100 file nodes)
- 1000-2000 edges (at least 1.5 per node)
- 20-50 communities (Leiden will over-cluster if edges are sparse)
- < 25% isolated nodes

For our Claude Code docs corpus:
- 797 nodes · 1241 edges · 59 communities · 23% isolated

## Common pitfalls ranked by severity

| # | Pitfall | Symptom | Fix |
|---|---------|---------|-----|
| 1 | One node per file | 100 docs → ~100 nodes | Concept-level prompts with examples |
| 2 | No cross-chunk edges | High intra-community cohesion, no connections | Cross-chunk edge pass |
| 3 | Invalid confidence labels | Phantom edge loss | Post-process `confidence_score` → label |
| 4 | Alphabetical chunking | Related docs in different chunks | Group chunks by semantic topic |
| 5 | Missed preprocessing | False similarity from boilerplate headers | Strip identical per-file headers |
| 6 | Using Explore subagent | Chunk files silently missing | Use `general-purpose` subagent type |
| 7 | Sequential dispatch | Takes 5× longer | All Agent calls in single message |

## Template: extraction prompt that works

```
You are a graphify extraction subagent. Read the files listed and extract
a knowledge graph fragment. Output ONLY valid JSON — no explanation, no
markdown fences.

Files (chunk N of M - {topic name}):
  graphify-out/.preprocessed/foo.md
  graphify-out/.preprocessed/bar.md
  ...

CRITICAL — CONCEPT-LEVEL EXTRACTION:
Each document contains MULTIPLE concepts. Extract each concept as its own node.
Do NOT create one node per document.

Examples of concepts to extract from these specific files:
- foo.md: concept_a, concept_b, concept_c (list 8-15 concrete examples)
- bar.md: concept_x, concept_y, concept_z

Node ID format: filestem_conceptname (e.g., foo_concept_a)

Rules:
- EXTRACTED: explicit in source (markdown link, direct reference, "see X")
- INFERRED: reasonable inference (shared pattern, implied dependency)
- AMBIGUOUS: uncertain — flag, don't omit

Confidence labels MUST be one of: EXTRACTED, INFERRED, AMBIGUOUS.
NEVER use "high" or "medium".

confidence_score REQUIRED on every edge:
- EXTRACTED: 1.0
- INFERRED: 0.6-0.9
- AMBIGUOUS: 0.1-0.3

Markdown links [text](other-doc.md) are EXTRACTED edges. "See also" sections
are goldmines — extract every link as an EXTRACTED edge.

Semantic similarity: if two concepts solve the same problem without structural
link, add `semantically_similar_to` INFERRED edge.

Hyperedges: up to 5 per chunk for 3+ nodes participating in a shared
concept/flow/pattern.

After extracting, write the JSON result to graphify-out/.graphify_chunk_NN.json
using the Write tool.

Schema: {
  "nodes": [{"id": "str", "label": "str", "file_type": "document",
             "source_file": "str", "source_location": "str"}],
  "edges": [{"source": "str", "target": "str",
             "relation": "references|conceptually_related_to|
                          semantically_similar_to|rationale_for|
                          implements|contains",
             "confidence": "EXTRACTED|INFERRED|AMBIGUOUS",
             "confidence_score": 1.0, "source_file": "str"}],
  "hyperedges": [{"id": "str", "label": "str", "nodes": ["str"],
                  "relation": "participate_in|implement|form",
                  "confidence": "str", "confidence_score": 0.85}],
  "input_tokens": 0, "output_tokens": 0
}
```

## Template: cross-chunk edge prompt that works

```
You are a graphify cross-chunk edge extraction subagent.

The knowledge graph has N nodes across M files but only E edges — mostly
intra-file. We need to add CROSS-FILE edges between existing nodes.

INPUT: Read graphify-out/.node_index.json — it lists all node IDs grouped
by source file.

CRITICAL RULES:
1. ONLY create edges between node IDs that ACTUALLY EXIST in the index.
   Do not invent nodes.
2. Focus on CROSS-FILE edges — source_file of source MUST differ from
   source_file of target.
3. Target 300-500 new edges.
4. Confidence labels: EXTRACTED (1.0), INFERRED (0.6-0.9), AMBIGUOUS (0.1-0.3).
   NEVER use "high" or "medium".
5. Prefer `semantically_similar_to` for mirror pairs, `conceptually_related_to`
   for broader links, `references` only when one doc explicitly links another.

Common patterns to find (adapt to your corpus):
- SDK ↔ CLI mirror pairs
- Config keys ↔ feature docs they control
- Overview/quickstart concepts ↔ detailed feature docs
- Env vars ↔ features they configure
- Commands ↔ features they trigger

OUTPUT: Write ONLY new edges (not existing ones) to
graphify-out/.graphify_cross_edges.json
```

## When to rebuild the graph

Rebuild when:
- Source docs change significantly (quarterly or after major releases)
- You notice graph queries returning stale information
- You added new docs and want them integrated

Do NOT rebuild on every doc update — the graph building costs real tokens,
and the structure is stable even if individual doc text changes. Our docs
update every 3 hours via CI; the graph rebuilds maybe once a month.

## See also

- [scripts/preprocess-for-graphify.py](scripts/preprocess-for-graphify.py) —
  reference preprocessing script
- [.graphifyignore](.graphifyignore) — exclude non-doc files and noise
- [graphify skill](https://github.com/safishamsi/graphify) — the underlying
  tool
