# Uninstalling Claude Code Documentation + Knowledge Graph

## Quick Uninstall

```bash
~/.claude-code-docs/uninstall.sh
```

Or use the docs command:

```bash
/docs uninstall
```

## What Gets Removed

The uninstaller removes:

1. **`/docs` command** -- `~/.claude/commands/docs.md`
2. **Documentation rule** -- `~/.claude/rules/claude-code-docs.md`
3. **Documentation skill** -- `~/.claude/skills/claude-code-docs/`
4. **Legacy hooks** -- any claude-code-docs hooks from `~/.claude/settings.json`
5. **Installation directory** -- `~/.claude-code-docs`

## Manual Uninstall

```bash
# 1. Remove the command, rule, and skill
rm -f ~/.claude/commands/docs.md
rm -f ~/.claude/rules/claude-code-docs.md
rm -rf ~/.claude/skills/claude-code-docs

# 2. Remove the installation directory
rm -rf ~/.claude-code-docs
```

If you had a legacy install (v0.3.x or earlier), also remove the PreToolUse hook
from `~/.claude/settings.json` referencing claude-code-docs.

## Reinstalling

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/install.sh | bash
```
