# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the WI System, please **do not** open a public issue.

Instead, please email the maintainers directly with:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if you have one)

We will acknowledge receipt of your report within 48 hours and work with you to understand and fix the issue.

## Scope

Security considerations for WI System include:

- **Local files** — Template stores everything in plain markdown files. No encryption by default.
- **AI agent access** — The `template/AGENTS.md` rules are read by your AI agent of choice (Claude Code, Cursor, etc.)
- **Git history** — Committing your vault means all changes are version controlled (consider privacy when adding sensitive data)

## Recommendations

To use WI System securely:

1. **Keep sensitive data out** — Don't store passwords, API keys, or personal information in your vault
2. **Control access** — Your vault is just a folder; share it like any other git repo
3. **Review AGENTS.md** — Understand what rules you're giving your AI agent
4. **Use private repos** — If storing in git, use a private repository
5. **Trust your AI provider** — WI System delegates work to your AI agent (Claude, GPT, etc.) — review their privacy policies

## No security guarantees

WI System is a markdown template with no built-in encryption, authentication, or access control. It is suitable for personal and team knowledge bases, not for storing secrets or regulated data.
