#!/bin/bash
set -euo pipefail

# Claude Code Documentation + Knowledge Graph - Uninstaller v0.1.0

echo "Claude Code Docs + Knowledge Graph - Uninstaller"
echo "================================================="
echo ""

echo "This will remove:"
echo "  - /docs command (commands/docs.md)"
echo "  - Documentation rule (rules/claude-code-docs.md)"
echo "  - Documentation skill (skills/claude-code-docs/)"
echo "  - Legacy hooks from settings.json (if any)"
echo "  - Installation directory (~/.claude-code-docs)"
echo ""

read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

# Remove command
if [[ -f ~/.claude/commands/docs.md ]]; then
    rm -f ~/.claude/commands/docs.md
    echo "Removed /docs command"
fi

# Remove rule
if [[ -f ~/.claude/rules/claude-code-docs.md ]]; then
    rm -f ~/.claude/rules/claude-code-docs.md
    echo "Removed documentation rule"
fi

# Remove skill
if [[ -d ~/.claude/skills/claude-code-docs ]]; then
    rm -rf ~/.claude/skills/claude-code-docs
    echo "Removed /claude-code-docs skill"
fi

# Remove legacy hooks from settings.json
if [[ -f ~/.claude/settings.json ]]; then
    if jq -e '.hooks.PreToolUse[]? | select(.hooks[0].command | contains("claude-code-docs"))' ~/.claude/settings.json >/dev/null 2>&1; then
        cp ~/.claude/settings.json ~/.claude/settings.json.backup
        jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.hooks[0].command | contains("claude-code-docs") | not)]' ~/.claude/settings.json > ~/.claude/settings.json.tmp
        jq 'if .hooks.PreToolUse == [] then .hooks |= del(.PreToolUse) else . end | if .hooks == {} then del(.hooks) else . end' ~/.claude/settings.json.tmp > ~/.claude/settings.json
        rm -f ~/.claude/settings.json.tmp
        echo "Removed legacy hooks (backup: ~/.claude/settings.json.backup)"
    fi
fi

# Remove installation directory
if [[ -d ~/.claude-code-docs ]]; then
    rm -rf ~/.claude-code-docs
    echo "Removed ~/.claude-code-docs"
fi

echo ""
echo "Uninstall complete!"
echo ""
echo "To reinstall:"
echo "curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/install.sh | bash"
