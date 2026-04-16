# Graph Report - docs/  (2026-04-16)

## Corpus Check
- 110 files · ~295,688 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 117 nodes · 409 edges · 11 communities detected
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 78 edges (avg confidence: 0.78)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Agent SDK (Build & Deploy)|Agent SDK (Build & Deploy)]]
- [[_COMMUNITY_Platforms & IDE Integrations|Platforms & IDE Integrations]]
- [[_COMMUNITY_Configuration & Environment|Configuration & Environment]]
- [[_COMMUNITY_Extensions & Orchestration|Extensions & Orchestration]]
- [[_COMMUNITY_Security & Compliance|Security & Compliance]]
- [[_COMMUNITY_Getting Started & Workflows|Getting Started & Workflows]]
- [[_COMMUNITY_SDK Core Abstractions|SDK Core Abstractions]]
- [[_COMMUNITY_SDK Built-in Tools|SDK Built-in Tools]]
- [[_COMMUNITY_SDK Result Types|SDK Result Types]]
- [[_COMMUNITY_SDK Permission Model|SDK Permission Model]]
- [[_COMMUNITY_SDK Context Management|SDK Context Management]]

## God Nodes (most connected - your core abstractions)
1. `Agent SDK Overview` - 22 edges
2. `Agent SDK Reference - TypeScript` - 21 edges
3. `Agent SDK Reference - Python` - 17 edges
4. `Continue local sessions from any device with Remote Control` - 17 edges
5. `Agent SDK Permissions` - 16 edges
6. `Troubleshooting` - 16 edges
7. `Agent SDK Quickstart` - 15 edges
8. `Manage costs effectively` - 15 edges
9. `How the Agent Loop Works` - 14 edges
10. `Agent SDK Claude Code Features` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Control Execution with Hooks` --semantically_similar_to--> `Claude Code Hooks Reference`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__hooks.md → hooks.md
- `Agent SDK Permissions` --semantically_similar_to--> `Permissions`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__permissions.md → permissions.md
- `Agent SDK Subagents` --semantically_similar_to--> `Claude Code Subagents`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__subagents.md → sub-agents.md
- `Agent SDK Subagents` --semantically_similar_to--> `Agent Teams`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__subagents.md → agent-teams.md
- `Agent SDK Hosting` --semantically_similar_to--> `Secure Deployment`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__hosting.md → agent-sdk__secure-deployment.md

## Hyperedges (group relationships)
- **Python and TypeScript SDK Parallel Implementations** — agent-sdk__python, agent-sdk__typescript, agent-sdk__overview, agent-sdk__quickstart [EXTRACTED 0.95]
- **Agent Loop Execution Lifecycle (turns, messages, tools, result)** — agent-sdk__agent-loop, agent-sdk__hooks, agent-sdk__permissions, agent-sdk__cost-tracking, overview_result_message, overview_builtin_tools [EXTRACTED 0.90]
- **Session Continuity Patterns (resume, continue, fork, V2 sessions)** — agent-sdk__sessions, overview_claude_sdk_client, overview_v2_session, agent-sdk__typescript-v2-preview [INFERRED 0.85]
- **Tool Extensibility System** — agent-sdk__custom-tools, agent-sdk__mcp, agent-sdk__tool-search [INFERRED 0.90]
- **Security and Permissions Layer** — agent-sdk__permissions, agent-sdk__hooks, agent-sdk__secure-deployment [INFERRED 0.85]
- **Agent Composition and Extension** — agent-sdk__subagents, agent-sdk__skills, agent-sdk__plugins [INFERRED 0.85]
- **Security and access control layer** — permissions, permission-modes, sandboxing, security, hooks [INFERRED 0.90]
- **Data governance and compliance** — data-usage, zero-data-retention, legal-and-compliance [INFERRED 0.90]
- **Trust, authentication, and privacy** — authentication, security, data-usage, legal-and-compliance [INFERRED 0.85]
- **Plugin Ecosystem** — plugins, plugins-reference, plugin-marketplaces, discover-plugins [EXTRACTED 1.00]
- **Claude Code Extensibility Layer** — mcp, plugins, skills, channels, tools-reference [INFERRED 0.85]
- **Agent Orchestration System** — sub-agents, agent-teams, skills, routines [INFERRED 0.80]
- **Configuration Hierarchy** — settings, server-managed-settings, env-vars, claude-directory [INFERRED 0.90]
- **Model and Performance Tuning** — model-config, fast-mode, context-window [INFERRED 0.85]
- **UI Customization** — terminal-config, keybindings, statusline, output-styles [INFERRED 0.85]
- **Third-party cloud provider integrations** — amazon-bedrock, google-vertex-ai, microsoft-foundry, third-party-integrations, llm-gateway [INFERRED 0.90]
- **IDE and editor integrations for Claude Code** — vs-code, jetbrains, desktop, platforms [INFERRED 0.90]
- **Web and cloud session ecosystem** — claude-code-on-the-web, web-quickstart, slack, desktop-scheduled-tasks [INFERRED 0.85]
- **Getting Started Journey** — overview, quickstart, setup [INFERRED 0.90]
- **Core Usage Patterns** — common-workflows, best-practices, how-claude-code-works, interactive-mode, cli-reference [INFERRED 0.85]
- **Terminal Experience Features** — interactive-mode, voice-dictation, fullscreen, cli-reference [INFERRED 0.85]
- **Operations and cost monitoring** — costs, monitoring-usage, analytics [INFERRED 0.90]
- **CI/CD platform integrations** — github-actions, gitlab-ci-cd, github-enterprise-server [INFERRED 0.90]
- **Remote and cloud session access** — remote-control, ultraplan, scheduled-tasks [INFERRED 0.85]

## Communities

### Community 0 - "Agent SDK (Build & Deploy)"
Cohesion: 0.31
Nodes (28): How the Agent Loop Works, Agent SDK Claude Code Features, Track Cost and Usage, Agent SDK Custom Tools, Agent SDK File Checkpointing, Control Execution with Hooks, Agent SDK Hosting, Agent SDK MCP Integration (+20 more)

### Community 1 - "Platforms & IDE Integrations"
Cohesion: 0.2
Nodes (25): Amazon Bedrock Setup, Use Claude Code with Chrome (beta), Use Claude Code on the web, Computer Use, Use Claude Code Desktop, Get started with the desktop app, Schedule recurring tasks in Claude Code Desktop, Fullscreen Rendering (+17 more)

### Community 2 - "Configuration & Environment"
Cohesion: 0.28
Nodes (18): Track team usage with analytics, Checkpointing, Claude Directory Explorer, Context Window, Manage costs effectively, Environment Variables, Fast Mode, Claude Code with GitHub Enterprise Server (+10 more)

### Community 3 - "Extensions & Orchestration"
Cohesion: 0.4
Nodes (17): Agent Teams, Channels, Channels Reference, Commands, Discover and Install Plugins, Claude Code GitHub Actions, Claude Code GitLab CI/CD, MCP (Model Context Protocol) (+9 more)

### Community 4 - "Security & Compliance"
Cohesion: 0.49
Nodes (11): Secure Deployment, Authentication, Data usage, Claude Code Hooks Reference, Claude Code Hooks Guide, Legal and compliance, Permission Modes, Permissions (+3 more)

### Community 5 - "Getting Started & Workflows"
Cohesion: 0.47
Nodes (11): Best Practices, CLI Reference, Code Review, Common Workflows, Development Containers, Extend Claude Code, Headless / Programmatic Mode, How Claude Code Works (+3 more)

### Community 6 - "SDK Core Abstractions"
Cohesion: 0.67
Nodes (3): ClaudeSDKClient (Python), query() Function, V2 Session (createSession/send/stream)

### Community 7 - "SDK Built-in Tools"
Cohesion: 1.0
Nodes (1): Built-in Tools (Read, Edit, Write, Bash, Glob, Grep, etc.)

### Community 8 - "SDK Result Types"
Cohesion: 1.0
Nodes (1): ResultMessage / SDKResultMessage

### Community 9 - "SDK Permission Model"
Cohesion: 1.0
Nodes (1): Permission Modes (default, acceptEdits, dontAsk, auto, bypassPermissions)

### Community 10 - "SDK Context Management"
Cohesion: 1.0
Nodes (1): Context Window and Compaction

## Knowledge Gaps
- **8 isolated node(s):** `query() Function`, `Built-in Tools (Read, Edit, Write, Bash, Glob, Grep, etc.)`, `ResultMessage / SDKResultMessage`, `Permission Modes (default, acceptEdits, dontAsk, auto, bypassPermissions)`, `Context Window and Compaction` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `SDK Built-in Tools`** (1 nodes): `Built-in Tools (Read, Edit, Write, Bash, Glob, Grep, etc.)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `SDK Result Types`** (1 nodes): `ResultMessage / SDKResultMessage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `SDK Permission Model`** (1 nodes): `Permission Modes (default, acceptEdits, dontAsk, auto, bypassPermissions)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `SDK Context Management`** (1 nodes): `Context Window and Compaction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Troubleshooting` connect `Configuration & Environment` to `Platforms & IDE Integrations`, `Extensions & Orchestration`, `Security & Compliance`, `Getting Started & Workflows`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Why does `Agent SDK Permissions` connect `Agent SDK (Build & Deploy)` to `Configuration & Environment`, `Security & Compliance`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Why does `Continue local sessions from any device with Remote Control` connect `Platforms & IDE Integrations` to `Extensions & Orchestration`, `Security & Compliance`, `Getting Started & Workflows`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Continue local sessions from any device with Remote Control` (e.g. with `Plan in the cloud with ultraplan` and `Run prompts on a schedule`) actually correct?**
  _`Continue local sessions from any device with Remote Control` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Agent SDK Permissions` (e.g. with `Control Execution with Hooks` and `Agent SDK MCP Integration`) actually correct?**
  _`Agent SDK Permissions` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `query() Function`, `Built-in Tools (Read, Edit, Write, Bash, Glob, Grep, etc.)`, `ResultMessage / SDKResultMessage` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._