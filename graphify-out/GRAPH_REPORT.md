# Graph Report - docs/  (2026-04-17)

## Corpus Check
- 110 files · ~295,688 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 797 nodes · 1241 edges · 59 communities detected
- Extraction: 34% EXTRACTED · 66% INFERRED · 0% AMBIGUOUS · INFERRED: 825 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]

## God Nodes (most connected - your core abstractions)
1. `Subagents in the SDK (isolated context, parallel execution)` - 27 edges
2. `MCP Server Integration (connect external tools)` - 21 edges
3. `CLAUDE.md Files (Persistent Instructions)` - 20 edges
4. `Claude Code Desktop App` - 19 edges
5. `Web Cloud Sessions on Anthropic Infrastructure` - 19 edges
6. `Agent Skills in the SDK (SKILL.md filesystem artifacts)` - 18 edges
7. `Hook Lifecycle` - 17 edges
8. `Plugins in the SDK (load custom extensions)` - 14 edges
9. `Managed Settings Scope` - 13 edges
10. `Context Window Compaction (/compact)` - 13 edges

## Surprising Connections (you probably didn't know these)
- `SDK Hooks (PreToolUse, PostToolUse, Stop, etc.)` --semantically_similar_to--> `SDK Hooks (intercept and control agent behavior)`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__overview.md → agent-sdk__hooks.md
- `Python @tool() Decorator` --semantically_similar_to--> `Custom Tool Definition (name, description, schema, handler)`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__python.md → agent-sdk__custom-tools.md
- `TypeScript tool() Function` --semantically_similar_to--> `Custom Tool Definition (name, description, schema, handler)`  [INFERRED] [semantically similar]
  graphify-out/.preprocessed/agent-sdk__typescript.md → agent-sdk__custom-tools.md
- `CLAUDE.md Files (Persistent Instructions)` --semantically_similar_to--> `CLAUDE.md Files (Project-Level Instructions)`  [INFERRED] [semantically similar]
  memory.md → graphify-out/.preprocessed/agent-sdk__modifying-system-prompts.md
- `PreToolUse Hook (block, modify, or approve tool calls)` --semantically_similar_to--> `PreToolUse Hook Event`  [INFERRED] [semantically similar]
  agent-sdk__hooks.md → hooks.md

## Hyperedges (group relationships)
- **Agent Loop Core Components** — agent_sdk__agent_loop_loop_overview, agent_sdk__agent_loop_turns, agent_sdk__agent_loop_message_types, agent_sdk__agent_loop_tool_execution, agent_sdk__agent_loop_result_subtypes [EXTRACTED 0.95]
- **System Prompt Modification Methods** — agent_sdk__modifying_system_prompts_claude_md, agent_sdk__modifying_system_prompts_output_styles, agent_sdk__modifying_system_prompts_preset_append, agent_sdk__modifying_system_prompts_custom [EXTRACTED 0.95]
- **Session Management Patterns** — agent_sdk__sessions_continue_resume_fork, agent_sdk__sessions_claude_sdk_client, agent_sdk__sessions_continue_true, agent_sdk__typescript_v2_preview_create_session, agent_sdk__sessions_fork_session [INFERRED 0.90]
- **Cost Tracking Pipeline** — agent_sdk__cost_tracking_per_step_usage, agent_sdk__cost_tracking_deduplication, agent_sdk__cost_tracking_per_model_usage, agent_sdk__cost_tracking_total_cost, agent_sdk__cost_tracking_cache_tokens [EXTRACTED 0.90]
- **User Input and Approval Flow** — agent_sdk__user_input_can_use_tool, agent_sdk__user_input_tool_approval, agent_sdk__user_input_ask_user_question, agent_sdk__user_input_permission_result, agent_sdk__agent_loop_permission_mode [INFERRED 0.90]
- **Permission System (hooks + rules + modes + canUseTool)** — permissions_evaluation_order, permissions_allow_deny_rules, permissions_mode_bypass, permissions_mode_acceptedits, permissions_mode_dontask, hooks_permission_decision, hooks_pretooluse [EXTRACTED 1.00]
- **Tool Ecosystem (custom tools + MCP + tool search + permissions)** — custom_tools_tool_definition, custom_tools_sdk_mcp_server, mcp_overview, tool_search_overview, custom_tools_allowed_tools, custom_tools_tool_name_format [EXTRACTED 0.95]
- **SDK Extensibility Features (skills, plugins, subagents, slash commands)** — skills_overview, plugins_overview, subagents_overview, slash_commands_overview, claude_code_features_feature_chooser [EXTRACTED 0.90]
- **Production Deployment Stack (hosting + security + observability)** — hosting_overview, secure_deployment_overview, observability_overview, hosting_container_sandboxing, secure_deployment_isolation_tech [INFERRED 0.85]
- **Hook Lifecycle (PreToolUse > execution > PostToolUse with matchers and callbacks)** — hooks_pretooluse, hooks_posttooluse, hooks_matchers, hooks_callback_inputs_outputs, hooks_permission_decision, hooks_async_output [EXTRACTED 0.95]
- **Defense-in-Depth Security Architecture** — permissions_tiered_system, sandboxing_overview, security_permission_architecture, security_prompt_injection_protections, hooks_pre_tool_use_event [INFERRED 0.90]
- **Hook Event System (all lifecycle events)** — hooks_hook_lifecycle, hooks_session_start_event, hooks_pre_tool_use_event, hooks_post_tool_use_event, hooks_stop_event, hooks_notification_event, hooks_config_change_event, hooks_elicitation_event [EXTRACTED 0.95]
- **Permission Mode Spectrum (restrictive to permissive)** — permission_modes_plan, permission_modes_default, permission_modes_accept_edits, permission_modes_auto, permission_modes_dont_ask, permission_modes_bypass [EXTRACTED 0.95]
- **Data Privacy and Governance Framework** — data_usage_training_policy, data_usage_retention, zero_data_retention_overview, security_privacy_safeguards, legal_license_terms [INFERRED 0.85]
- **Sandbox Dual Isolation (filesystem + network)** — sandboxing_filesystem_isolation, sandboxing_network_isolation, sandboxing_os_level_enforcement, sandboxing_rationale_dual_isolation [EXTRACTED 0.95]
- **Claude Code Extensibility Ecosystem** — mcp_overview, plugins_overview, skills_overview, subagents_overview, channels_overview [high 0.95]
- **Hierarchical Scope Pattern (local > project > user > managed)** — mcp_scope_hierarchy, plugins_ref_scopes, subagents_scopes, skills_locations, memory_claude_md [high 0.90]
- **Enterprise/Managed Configuration Controls** — mcp_managed_config, mcp_allowlist_denylist, marketplace_managed_restrictions, channels_enterprise, memory_managed_claude_md [high 0.90]
- **Agent Orchestration Mechanisms** — subagents_overview, agent_teams_overview, skills_context_fork, tools_agent, subagents_background [high 0.90]
- **Plugin Component Types** — plugins_structure, plugins_lsp, mcp_plugin_servers, plugins_ref_hooks, plugins_namespacing [high 0.90]
- **Settings Configuration Hierarchy** — settings_managed_scope, settings_user_scope, settings_project_scope, settings_local_scope, settings_scope_precedence [high 0.95]
- **Model Configuration System** — model_config_model_aliases, model_config_effort_level, model_config_extended_context, envvars_anthropic_model, model_config_restrict_selection [high 0.92]
- **Third-Party Cloud Provider Integration** — envvars_claude_code_use_bedrock, envvars_claude_code_use_vertex, envvars_claude_code_use_foundry, model_config_pin_models [high 0.92]
- **Context Window Management System** — context_window_structure, context_window_compaction, envvars_claude_autocompact_pct, envvars_disable_compact, statusline_context_window_fields [high 0.90]
- **.claude Directory Ecosystem** — claude_directory_project_scope, claude_directory_global_scope, claude_directory_claude_md, claude_directory_rules, claude_directory_skills [high 0.93]
- **IDE Integration Extensions** — vs-code_extension, jetbrains_plugin, desktop_app [high 0.92]
- **Third-Party Cloud Provider Integrations** — amazon-bedrock_setup, google-vertex-ai_setup, microsoft-foundry_setup, third-party-integrations_overview [high 0.95]
- **Model Version Pinning Pattern** — amazon-bedrock_model_pinning, google-vertex-ai_model_pinning, microsoft-foundry_model_pinning [high 0.93]
- **Diff Review Across Surfaces** — vs-code_inline_diff, jetbrains_diff_viewing, desktop_diff_review, web-quickstart_review_iterate [high 0.88]
- **Remote and Async Work Patterns** — claude-code-on-the-web_cloud_sessions, desktop_dispatch, slack_integration, platforms_away_from_terminal, desktop-scheduled-tasks_overview [high 0.87]
- **Core Agentic Architecture** — how_it_works_agentic_loop, how_it_works_tool_use_cycle, how_it_works_context_window, how_it_works_checkpoints, how_it_works_permission_modes [high 0.95]
- **Non-Interactive/CI Pipeline Pattern** — headless_non_interactive, headless_bare_mode, headless_ci_cd_usage, cli_reference_print_flag, cli_reference_output_format, cli_reference_allowed_tools [high 0.93]
- **Parallel Execution Strategies** — common_workflows_git_worktrees, best_practices_parallel_sessions, cli_reference_worktree_flag, features_overview_agent_teams, best_practices_subagent_investigation [high 0.90]
- **Context Window Optimization Strategies** — best_practices_context_management, how_it_works_context_window, features_overview_context_cost, interactive_mode_btw, best_practices_failure_patterns [high 0.92]
- **Claude Code Extensibility System** — features_overview_feature_comparison, features_overview_hooks_vs_mcp, features_overview_combine_patterns, features_overview_skills_vs_subagents, features_overview_feature_layering [high 0.93]
- **Cost and Usage Observability Pipeline** — costs_cost_command, costs_team_spend_limits, monitoring_opentelemetry, monitoring_metrics, analytics_dashboard, analytics_api_dashboard, monitoring_roi [high 0.90]
- **CI/CD Platform Integrations** — github_actions_overview, gitlab_cicd_overview, ghes_overview, github_actions_cloud_providers, gitlab_cicd_cloud_providers [high 0.92]
- **Remote and Cloud Session Access** — remote_control_overview, ultraplan_overview, remote_control_vs_web, ultraplan_execution_choice [high 0.88]
- **Scheduling and Automation System** — scheduled_loop_command, scheduled_cron_tools, scheduled_comparison, w15_monitor_tool, scheduled_dynamic_pacing [high 0.88]
- **Weekly Feature Release Cycle (W13-W15)** — whats_new_overview, w13_auto_mode, w13_computer_use, w14_computer_use_cli, w15_ultraplan, w15_monitor_tool, w15_autofix_pr [high 0.85]

## Communities

### Community 0 - "Community 0"
Cohesion: 0.04
Nodes (69): Chrome Extension for Browser Automation, Chrome Screenshot and GIF Recording, Chrome Site-level Permissions, Chrome Tab Control and Navigation, Chrome Visual Verification and Live Debugging, Auto-fix Pull Requests from Web, Web Cloud Sessions on Anthropic Infrastructure, GitHub Authentication for Cloud Sessions (+61 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (66): AgentDefinition Configuration, Claude Code Features (Skills, Slash Commands, Memory, Plugins), Subagents (Agent Tool), Python ToolAnnotations, TypeScript ToolAnnotations, Agent Teams vs Subagents Comparison, Fan-Out Parallel Sessions and Multi-Claude Workflows, Subagents for Investigation (Context Isolation) (+58 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (64): Authentication Providers (API Key, Bedrock, Vertex AI, Azure), Quickstart Bug-Fixing Agent Example, Bedrock Automatic Credential Refresh, Bedrock Cross-Region Inference Profiles, Bedrock IAM Policy Configuration, Bedrock Mantle Endpoint, Bedrock Model Version Pinning, Amazon Bedrock Setup and Configuration (+56 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (53): Permission Mode Options (default, acceptEdits, plan, dontAsk, auto, bypassPermissions), SDK Hooks (PreToolUse, PostToolUse, Stop, etc.), Tool Permission Control (allowed_tools, disallowed_tools), Permission Modes (default, acceptEdits, dontAsk, auto, bypassPermissions), canUseTool Callback, Modified Tool Input (Approve with Changes), PermissionResultAllow / PermissionResultDeny, Tool Approval Requests (Allow/Deny) (+45 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (48): AWS Guardrails for Content Filtering, Cloud Session Security and Isolation, Computer Use Safety (Lock, Escape, Sentinel Warnings), Cloud Execution Data Flow, Development Container Reference Setup, ConfigChange Hook Event, Audit Configuration Changes (Hook Pattern), Hook If Condition Filter (+40 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (41): Package Name Changes (TS: @anthropic-ai/claude-agent-sdk, Python: claude-agent-sdk), query() Function, Agent SDK vs Client SDK Comparison, Session Management (resume, fork), Python ClaudeAgentOptions, Python ClaudeSDKClient Class, Python query() Function, ClaudeSDKClient Auto Session Management (+33 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (41): Agent Loop Architecture, Message Types (SystemMessage, AssistantMessage, UserMessage, StreamEvent, ResultMessage), Tool Execution in Agent Loop, Turns and Round Trips, Built-in Tools (Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch, Monitor), Enable Streaming Output (include_partial_messages), Streaming Limitations (Extended Thinking, Structured Output), StreamEvent / SDKPartialAssistantMessage Type (+33 more)

### Community 7 - "Community 7"
Cohesion: 0.07
Nodes (41): Breaking Change: Settings Sources No Longer Loaded by Default, settingSources Option (user, project, local), CLAUDE.md Best Practices, Project Instructions (CLAUDE.md and rules loading in SDK), CLAUDE.md Load Locations (project, parent, child, local, user, rules), Choose the Right Feature (CLAUDE.md vs Skills vs Subagents vs Hooks vs MCP), settingSources (load CLAUDE.md, skills, hooks from filesystem), Application Data (Transcripts, History, Snapshots) (+33 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (39): Result Subtypes (success, error_max_turns, error_max_budget_usd, etc.), Turns and Budget Limits (max_turns, max_budget_usd), Accumulate Costs Across Multiple Calls, Cost Tracking on Failed Conversations, Total Cost Tracking (total_cost_usd), Capture Session ID from ResultMessage, Structured Output Error Handling (error_max_structured_output_retries), API Customer Analytics Dashboard (Console) (+31 more)

### Community 9 - "Community 9"
Cohesion: 0.07
Nodes (38): Agent Loop Hooks (PreToolUse, PostToolUse, Stop, SubagentStart/Stop, PreCompact), Two Hook Types (filesystem shell commands vs programmatic callbacks), /hooks Command, Desktop Notifications via Hooks, Combine Features Patterns (Skill+MCP, Hook+MCP, etc.), When to Use Hooks vs MCP vs Plugins, Agent-based Hook Type, Hook Callback Inputs and Outputs (systemMessage, permissionDecision, updatedInput) (+30 more)

### Community 10 - "Community 10"
Cohesion: 0.09
Nodes (35): MCP Server Integration, Python create_sdk_mcp_server(), Python @tool() Decorator, TypeScript createSdkMcpServer(), TypeScript tool() Function, AskUserQuestion Tool, Option Previews (markdown/html) - TypeScript Only, AskUserQuestion Format (questions, options, multiSelect) (+27 more)

### Community 11 - "Community 11"
Cohesion: 0.08
Nodes (34): Model Selection Option, Parallel Tool Execution, Prompt Caching, Cache Tokens (cache_creation_input_tokens, cache_read_input_tokens), Token Deduplication for Parallel Tool Calls, Per-Model Usage Breakdown (modelUsage), Per-Step Token Usage (input_tokens, output_tokens), Breaking Change: System Prompt No Longer Default (+26 more)

### Community 12 - "Community 12"
Cohesion: 0.09
Nodes (34): Contribution Metrics with GitHub Integration, PR Attribution and claude-code-assisted Label, Automated PR Code Review (Multi-Agent Analysis), Manual Review Trigger (@claude review), /loop Skill (Recurring Prompts), /schedule Command (Create Routines), Pull Request Creation Workflow, Running Claude on a Schedule (+26 more)

### Community 13 - "Community 13"
Cohesion: 0.1
Nodes (30): /plugin Command (Manage Plugins), Plugin Auto-Updates, Code Intelligence Plugins (LSP), External Integration Plugins (GitHub, Slack, Sentry, etc.), Official Anthropic Plugin Marketplace, Team Marketplace Configuration (extraKnownMarketplaces), marketplace.json Schema, Managed Marketplace Restrictions (strictKnownMarketplaces) (+22 more)

### Community 14 - "Community 14"
Cohesion: 0.11
Nodes (28): Effort Level (low, medium, high, max), /effort Command (Model Effort Level), Rate Limit Recommendations by Team Size, CLAUDE_CODE_DISABLE_FAST_MODE Environment Variable, CLAUDE_CODE_EFFORT_LEVEL Environment Variable, Fast Mode Cost Tradeoff ($30/$150 MTok), Fast Mode Overview (2.5x Speed Opus 4.6), Fast Mode Per-Session Opt-In (fastModePerSessionOptIn) (+20 more)

### Community 15 - "Community 15"
Cohesion: 0.11
Nodes (26): Automatic Context Compaction, Context Window Management, CLAUDE.md Files (Project-Level Instructions), Context Window Management, Common Failure Patterns to Avoid, /btw Command (Side Question), /compact Command (Context Compaction), Context Window Compaction (/compact) (+18 more)

### Community 16 - "Community 16"
Cohesion: 0.11
Nodes (24): Agent Teams Display Modes (in-process, split panes/tmux), Agent Teams Inter-Agent Messaging, Agent Teams (Multi-Session Orchestration), Agent Teams Plan Approval Gate, Agent Teams Shared Task List, Explore-Plan-Code-Commit Workflow, /plan Command (Enter Plan Mode), Plan Mode for Safe Code Analysis (+16 more)

### Community 17 - "Community 17"
Cohesion: 0.15
Nodes (16): Claude Code SDK to Claude Agent SDK Rename, Agent SDK Overview, Provide Specific Context in Prompts, Desktop App Installation and First Session, Claude Code Overview, Installation Methods (curl, Homebrew, WinGet), Quickstart First Session Workflow, System Requirements and Platform Support (+8 more)

### Community 18 - "Community 18"
Cohesion: 0.23
Nodes (12): Discord Channel Plugin, Channels Enterprise Controls (channelsEnabled, allowedChannelPlugins), iMessage Channel Plugin, Channels (Push Events into Sessions), Channel claude/channel Capability Declaration, Channel Notification Format (notifications/claude/channel), Channel Permission Relay, Channel Reply Tool (Two-Way Communication) (+4 more)

### Community 19 - "Community 19"
Cohesion: 0.7
Nodes (5): Output Styles (Persistent Configurations), .claude/output-styles/ Directory, Built-in Output Styles (Default/Explanatory/Learning), Custom Output Styles (Markdown with Frontmatter), Output Styles Overview

### Community 20 - "Community 20"
Cohesion: 0.67
Nodes (3): --add-dir Flag for Additional Directories, CLAUDE.md from --add-dir (CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD), Working Directories and Additional Directories

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (3): --bare Flag for Minimal Startup, CLAUDE_CODE_SIMPLE / --bare Mode, Bare Mode (--bare) for Fast Startup

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (2): Dynamic OTel Headers for Enterprise Auth, Tag Telemetry with Service Name and Resource Attributes

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (2): PostToolUseFailure Hook (handle tool errors), StopFailure Hook Event

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (2): Async Hooks (Background Execution), Async Hook Output (fire-and-forget for side effects)

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (2): DontAsk Permission Mode, dontAsk Permission Mode (deny instead of prompting)

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (2): Remote Control Connection Security, Remote Control Session Security

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (2): Plugin User Configuration (userConfig), Plugin settings.json (Default Agent)

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (2): Plugin Environment Variables (CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA), Plugin Persistent Data Directory

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (2): Skill allowed-tools (Pre-approve Tools), Skill Tool Restrictions (allowed-tools only in CLI, not SDK)

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (2): Give Claude Verification Criteria, Test Writing Workflow

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (2): Plugin bin/ Directory (PATH Executables), Plugin Executables on PATH (Week 14)

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (1): Tool Categories (Read-only, Analyze+Modify, Full Automation)

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (1): V2 Session Cleanup (await using / manual close)

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (1): TypeScript persistSession: false (In-Memory Only)

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (1): Streaming Message Flow Order

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (1): Tool Error Handling (isError flag vs uncaught exception)

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (1): Return Images and Resources from Tools

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (1): Optimize Tool Discovery (descriptive names and descriptions)

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (1): Tool Search Limits (10K tools, 3-5 results, Sonnet 4+ / Opus 4+)

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (1): Hook Timeout Configuration

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (1): Plugin Caching and File Resolution

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (1): Plugin Monitors Configuration

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (1): Skill Supporting Files (templates, scripts, reference)

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (1): Line Break Input Methods (Shift+Enter, Ctrl+J)

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (1): Terminal Notification Setup

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (1): Multi-Root Workspaces Support

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (1): Web Session Pre-fill via URL Parameters

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (1): Codebase Exploration Workflow

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (1): Code Refactoring Workflow

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (1): Prompt Suggestions Feature

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (1): Code Review Severity Levels (Important, Nit, Pre-existing)

### Community 52 - "Community 52"
Cohesion: 1.0
Nodes (1): Voice Dictation Language Support (20 languages)

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (1): Metrics Cardinality Control

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (1): One-Time Reminder Scheduling

### Community 55 - "Community 55"
Cohesion: 1.0
Nodes (1): GitHub Actions Beta to v1.0 Migration

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (1): What's New - Weekly Dev Digest

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (1): /powerup Interactive Lessons (Week 14)

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (1): /team-onboarding Command (Week 15)

## Knowledge Gaps
- **186 isolated node(s):** `Claude Code Features (Skills, Slash Commands, Memory, Plugins)`, `Agent SDK vs Client SDK Comparison`, `Tool Categories (Read-only, Analyze+Modify, Full Automation)`, `Python ClaudeAgentOptions`, `V2 session.send() / session.stream() Pattern` (+181 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 22`** (2 nodes): `Dynamic OTel Headers for Enterprise Auth`, `Tag Telemetry with Service Name and Resource Attributes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (2 nodes): `PostToolUseFailure Hook (handle tool errors)`, `StopFailure Hook Event`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (2 nodes): `Async Hooks (Background Execution)`, `Async Hook Output (fire-and-forget for side effects)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `DontAsk Permission Mode`, `dontAsk Permission Mode (deny instead of prompting)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `Remote Control Connection Security`, `Remote Control Session Security`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `Plugin User Configuration (userConfig)`, `Plugin settings.json (Default Agent)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `Plugin Environment Variables (CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA)`, `Plugin Persistent Data Directory`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `Skill allowed-tools (Pre-approve Tools)`, `Skill Tool Restrictions (allowed-tools only in CLI, not SDK)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `Give Claude Verification Criteria`, `Test Writing Workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (2 nodes): `Plugin bin/ Directory (PATH Executables)`, `Plugin Executables on PATH (Week 14)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (1 nodes): `Tool Categories (Read-only, Analyze+Modify, Full Automation)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (1 nodes): `V2 Session Cleanup (await using / manual close)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `TypeScript persistSession: false (In-Memory Only)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `Streaming Message Flow Order`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `Tool Error Handling (isError flag vs uncaught exception)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `Return Images and Resources from Tools`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Optimize Tool Discovery (descriptive names and descriptions)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `Tool Search Limits (10K tools, 3-5 results, Sonnet 4+ / Opus 4+)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `Hook Timeout Configuration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `Plugin Caching and File Resolution`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `Plugin Monitors Configuration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `Skill Supporting Files (templates, scripts, reference)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `Line Break Input Methods (Shift+Enter, Ctrl+J)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `Terminal Notification Setup`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `Multi-Root Workspaces Support`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `Web Session Pre-fill via URL Parameters`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `Codebase Exploration Workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `Code Refactoring Workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `Prompt Suggestions Feature`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `Code Review Severity Levels (Important, Nit, Pre-existing)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `Voice Dictation Language Support (20 languages)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `Metrics Cardinality Control`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `One-Time Reminder Scheduling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (1 nodes): `GitHub Actions Beta to v1.0 Migration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `What's New - Weekly Dev Digest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `/powerup Interactive Lessons (Week 14)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `/team-onboarding Command (Week 15)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Subagents in the SDK (isolated context, parallel execution)` connect `Community 1` to `Community 3`, `Community 7`, `Community 9`, `Community 10`, `Community 13`, `Community 16`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Why does `MCP Server Integration (connect external tools)` connect `Community 10` to `Community 0`, `Community 2`, `Community 3`, `Community 7`, `Community 9`, `Community 12`, `Community 13`, `Community 14`, `Community 15`, `Community 18`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Why does `Plugins in the SDK (load custom extensions)` connect `Community 13` to `Community 1`, `Community 9`, `Community 10`, `Community 15`, `Community 18`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `Subagents in the SDK (isolated context, parallel execution)` (e.g. with `Built-in Subagents (Explore, Plan, general-purpose)` and `Background Subagents (Concurrent Execution)`) actually correct?**
  _`Subagents in the SDK (isolated context, parallel execution)` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `MCP Server Integration (connect external tools)` (e.g. with `In-Process SDK MCP Server (createSdkMcpServer / create_sdk_mcp_server)` and `MCP Server Configuration (.mcp.json)`) actually correct?**
  _`MCP Server Integration (connect external tools)` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `CLAUDE.md Files (Persistent Instructions)` (e.g. with `AGENTS.md Compatibility` and `/init Command (Initialize CLAUDE.md)`) actually correct?**
  _`CLAUDE.md Files (Persistent Instructions)` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Claude Code Desktop App` (e.g. with `Desktop Code Tab (Chat/Cowork/Code)` and `Claude Code Environments (Terminal, VS Code, Desktop, Web, JetBrains)`) actually correct?**
  _`Claude Code Desktop App` has 2 INFERRED edges - model-reasoned connections that need verification._