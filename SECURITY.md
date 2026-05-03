# Security Policy

## Supported Versions

| Version | Status |
|---------|--------|
| main branch | ✅ Supported |
| Previous releases | ⚠️ Best effort |

We recommend always using the latest version from the main branch.

## Reporting Security Issues

**Please do NOT open a public issue for security vulnerabilities.**

Instead, report privately:

1. Email the maintainer(s) with:
   - Description of the vulnerability
   - Affected version/commit
   - Reproduction steps (if applicable)
   - Potential impact
   - Suggested mitigation (optional)

2. We will:
   - Acknowledge receipt within 48 hours
   - Provide a remediation timeline
   - Credit you in the fix (unless you prefer anonymity)

## Security Best Practices

### When Using WI-system

- **Never commit credentials** — Keep API keys in environment variables only
- **Protect your wiki folder** — It may contain sensitive information
- **Review LLM outputs** — Generated content may hallucinate or contain errors
- **Use secure API keys** — Store in `.env` files (add to `.gitignore`)
- **Audit wiki changes** — Check `log.md` for unexpected modifications
- **Keep dependencies updated** — Run `pip install --upgrade` periodically

### Example `.env` setup (don't commit this!)

```bash
# .env (add to .gitignore)
WI_LLM_API_KEY=sk-xxx...
WI_LLM_BASE_URL=http://localhost:11434/v1
WI_LLM_MODEL=mistral:latest
```

Load via Python:
```python
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")
```

### LLM-Specific Concerns

- **Model outputs aren't guaranteed** — Always review synthesized answers
- **Token limits** — Long wikis may hit LLM context limits
- **API costs** — Using commercial LLM services incurs costs; be mindful
- **Data privacy** — Your wiki content is sent to the LLM (use local models if sensitive)

## Known Limitations

- **No encryption at rest** — Wiki files are plaintext markdown
- **Git history is public** — All commits visible if repo is public
- **LLM hallucinations** — Generated content may be inaccurate

## Dependency Security

WI-system has **no external dependencies** in the base installation, reducing supply chain risk. Optional dev dependencies (pytest, ruff, mypy) are well-maintained and widely used.

---

Thank you for helping keep WI-system secure!
