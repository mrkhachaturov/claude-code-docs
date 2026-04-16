---
name: claude-code-docs
description: Query the Claude Code documentation knowledge graph. Use when asked about Claude Code features, configuration, hooks, permissions, settings, SDK, or best practices.
when_to_use: When the user asks how Claude Code works, how to configure it, what features exist, or references official documentation.
disable-model-invocation: false
allowed-tools: Read Bash Grep Glob
---

# Claude Code Documentation

Query the official Claude Code documentation via a knowledge graph
at `~/.claude-code-docs/graphify-out/`.

**Graph, not files.** The primary tool is graph traversal on `graph.json` using
NetworkX. Do NOT just read wiki articles or raw docs — that defeats the purpose.

## Python interpreter

```bash
GRAPHIFY_PYTHON=$(cat ~/.claude-code-docs/graphify-out/.graphify_python 2>/dev/null || echo "python3")
```

Use `$GRAPHIFY_PYTHON` in all subsequent bash blocks.

## When invoked with a question: `/claude-code-docs <question>`

### Step 1 — Graph query (BFS traversal)

```bash
$(cat ~/.claude-code-docs/graphify-out/.graphify_python) -c "
import sys, json
from networkx.readwrite import json_graph
import networkx as nx
from pathlib import Path

data = json.loads(Path('$HOME/.claude-code-docs/graphify-out/graph.json').read_text())
G = json_graph.node_link_graph(data, edges='links')

question = 'QUESTION'
terms = [t.lower() for t in question.split() if len(t) > 3]

# Find best-matching start nodes
scored = []
for nid, ndata in G.nodes(data=True):
    label = ndata.get('label', '').lower()
    score = sum(1 for t in terms if t in label)
    if score > 0:
        scored.append((score, nid))
scored.sort(reverse=True)
start_nodes = [nid for _, nid in scored[:3]]

if not start_nodes:
    print('No matching nodes found for query terms:', terms)
    sys.exit(0)

# BFS: explore all neighbors layer by layer up to depth 2
frontier = set(start_nodes)
subgraph_nodes = set(start_nodes)
subgraph_edges = []
for _ in range(2):
    next_frontier = set()
    for n in frontier:
        for neighbor in G.neighbors(n):
            if neighbor not in subgraph_nodes:
                next_frontier.add(neighbor)
                subgraph_edges.append((n, neighbor))
    subgraph_nodes.update(next_frontier)
    frontier = next_frontier

# Output ranked by relevance
def relevance(nid):
    label = G.nodes[nid].get('label', '').lower()
    return sum(1 for t in terms if t in label)

ranked = sorted(subgraph_nodes, key=relevance, reverse=True)

print(f'Traversal: BFS | Start: {[G.nodes[n].get(\"label\",n) for n in start_nodes]} | {len(subgraph_nodes)} nodes')
for nid in ranked:
    d = G.nodes[nid]
    print(f'  NODE {d.get(\"label\", nid)} [src={d.get(\"source_file\",\"\")}]')
for u, v in subgraph_edges:
    if u in subgraph_nodes and v in subgraph_nodes:
        d = G.edges[u, v]
        print(f'  EDGE {G.nodes[u].get(\"label\",u)} --{d.get(\"relation\",\"\")} [{d.get(\"confidence\",\"\")}]--> {G.nodes[v].get(\"label\",v)}')
"
```

Replace `QUESTION` with the user's actual question.

### Step 2 — Answer from the subgraph

Answer using **only** what the graph traversal returned. Cite node labels and
edge relations. The `source_file` field on each node tells you which raw doc
it came from if you need to verify a detail.

### Step 3 — Read raw doc only if graph lacks a specific detail

If the user asks for exact syntax, JSON schema, or config examples that the
graph traversal didn't include, read the specific section from the raw doc:

```bash
cat ~/.claude-code-docs/docs/{source_file}
```

Read only the section you need, not the whole file.

## For path queries: `/claude-code-docs path "A" "B"`

Find the shortest path between two concepts:

```bash
$(cat ~/.claude-code-docs/graphify-out/.graphify_python) -c "
import json, sys
import networkx as nx
from networkx.readwrite import json_graph
from pathlib import Path

data = json.loads(Path('$HOME/.claude-code-docs/graphify-out/graph.json').read_text())
G = json_graph.node_link_graph(data, edges='links')

def find_node(term):
    term = term.lower()
    scored = sorted(
        [(sum(1 for w in term.split() if w in G.nodes[n].get('label','').lower()), n)
         for n in G.nodes()],
        reverse=True
    )
    return scored[0][1] if scored and scored[0][0] > 0 else None

src = find_node('NODE_A')
tgt = find_node('NODE_B')

if not src or not tgt:
    print(f'Could not find nodes matching the terms')
    sys.exit(0)

try:
    path = nx.shortest_path(G, src, tgt)
    print(f'Shortest path ({len(path)-1} hops):')
    for i, nid in enumerate(path):
        label = G.nodes[nid].get('label', nid)
        if i < len(path) - 1:
            edge = G.edges[nid, path[i+1]]
            print(f'  {label} --{edge.get(\"relation\",\"\")}--> [{edge.get(\"confidence\",\"\")}]')
        else:
            print(f'  {label}')
except nx.NetworkXNoPath:
    print('No path found')
"
```

Replace `NODE_A` and `NODE_B` with the actual concept names.

## For node explain: `/claude-code-docs explain "X"`

Show everything connected to a single concept:

```bash
$(cat ~/.claude-code-docs/graphify-out/.graphify_python) -c "
import json
import networkx as nx
from networkx.readwrite import json_graph
from pathlib import Path

data = json.loads(Path('$HOME/.claude-code-docs/graphify-out/graph.json').read_text())
G = json_graph.node_link_graph(data, edges='links')

term = 'NODE_NAME'.lower()
scored = sorted(
    [(sum(1 for w in term.split() if w in G.nodes[n].get('label','').lower()), n)
     for n in G.nodes()],
    reverse=True
)
if not scored or scored[0][0] == 0:
    print(f'No node matching: {term}')
else:
    nid = scored[0][1]
    d = G.nodes[nid]
    print(f'NODE: {d.get(\"label\", nid)} [src={d.get(\"source_file\",\"\")} degree={G.degree(nid)}]')
    for neighbor in G.neighbors(nid):
        edge = G.edges[nid, neighbor]
        nlabel = G.nodes[neighbor].get('label', neighbor)
        print(f'  --{edge.get(\"relation\",\"\")}--> {nlabel} [{edge.get(\"confidence\",\"\")}]')
"
```

Replace `NODE_NAME` with the concept.

## When invoked without arguments: `/claude-code-docs`

Show the graph summary:

```bash
$(cat ~/.claude-code-docs/graphify-out/.graphify_python) -c "
import json
from networkx.readwrite import json_graph
import networkx as nx
from pathlib import Path

data = json.loads(Path('$HOME/.claude-code-docs/graphify-out/graph.json').read_text())
G = json_graph.node_link_graph(data, edges='links')

gods = sorted(G.nodes(data=True), key=lambda x: G.degree(x[0]), reverse=True)[:10]
print(f'Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges')
print()
print('God nodes (most connected):')
for nid, d in gods:
    print(f'  {d.get(\"label\", nid)} ({G.degree(nid)} edges)')
print()
print('Commands:')
print('  /claude-code-docs <question>        BFS traversal query')
print('  /claude-code-docs path \"A\" \"B\"      Shortest path')
print('  /claude-code-docs explain \"X\"       Node neighborhood')
"
```
