from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any
from urllib import request


@dataclass
class LlmConfig:
    mode: str = "mock"
    model: str = "gpt-4.1-mini"
    base_url: str = "https://api.openai.com/v1"
    api_key: str = ""


class LlmClient:
    def __init__(self, config: LlmConfig | None = None) -> None:
        if config is None:
            config = LlmConfig(
                mode=os.getenv("WI_LLM_MODE", "mock"),
                model=os.getenv("WI_LLM_MODEL", "gpt-4.1-mini"),
                base_url=os.getenv("WI_LLM_BASE_URL", "https://api.openai.com/v1"),
                api_key=os.getenv("WI_LLM_API_KEY", ""),
            )
        self.config = config

    def extract_knowledge(self, source_name: str, source_text: str, existing_index: str) -> dict[str, Any]:
        if self.config.mode.lower() != "openai":
            return self._mock_extract(source_name, source_text)

        prompt = (
            "You maintain a living wiki. Return strict JSON with keys: "
            "pages (list), contradictions (list), source_summary (string). "
            "Each page has: title, category, summary, key_claims, entities, sources, open_questions, related_pages. "
            "Use concise text. Do not include markdown."
        )
        payload = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": (
                        f"Existing index:\n{existing_index}\n\n"
                        f"Source name: {source_name}\n"
                        f"Source text:\n{source_text[:20000]}"
                    ),
                },
            ],
            "temperature": 0.1,
            "response_format": {"type": "json_object"},
        }

        data = json.dumps(payload).encode("utf-8")
        req = request.Request(
            url=f"{self.config.base_url.rstrip('/')}/chat/completions",
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api_key}",
            },
            method="POST",
        )
        with request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        content = body["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        return parsed

    def synthesize_answer(self, question: str, page_context: str) -> str:
        if self.config.mode.lower() != "openai":
            return (
                "Synthesis (mock mode):\n"
                f"Question: {question}\n"
                "This answer is composed from matched wiki pages. "
                "Set WI_LLM_MODE=openai for model-generated synthesis.\n\n"
                f"Context excerpt:\n{page_context[:1500]}"
            )

        prompt = "Answer using only the supplied wiki context. Cite page titles inline."
        payload = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Question: {question}\\n\\nContext:\\n{page_context[:24000]}"},
            ],
            "temperature": 0.2,
        }
        req = request.Request(
            url=f"{self.config.base_url.rstrip('/')}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api_key}",
            },
            method="POST",
        )
        with request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        return body["choices"][0]["message"]["content"].strip()

    def _mock_extract(self, source_name: str, source_text: str) -> dict[str, Any]:
        lines = [ln.strip() for ln in source_text.splitlines() if ln.strip()]
        summary = " ".join(lines[:3])[:500] if lines else "No text extracted"
        claims = []
        for line in lines[:20]:
            if any(marker in line.lower() for marker in [" is ", " are ", " should ", " must ", " can "]):
                claims.append(line[:180])
        if not claims and lines:
            claims = lines[:5]

        title = source_name.rsplit(".", 1)[0].replace("_", " ").replace("-", " ").title() or "Source"

        return {
            "source_summary": summary,
            "contradictions": [],
            "pages": [
                {
                    "title": title,
                    "category": "source-derived",
                    "summary": summary,
                    "key_claims": claims[:10],
                    "entities": self._guess_entities(lines),
                    "sources": [f"sources/{source_name}"],
                    "open_questions": [],
                    "related_pages": [],
                }
            ],
        }

    @staticmethod
    def _guess_entities(lines: list[str]) -> list[str]:
        entities: list[str] = []
        for line in lines[:40]:
            words = [w.strip(".,:;()[]{}!?\"") for w in line.split()]
            for idx, word in enumerate(words):
                if idx == 0:
                    continue
                if len(word) > 2 and word[0].isupper() and word[1:].islower():
                    entities.append(word)
        seen = set()
        unique = []
        for e in entities:
            key = e.lower()
            if key not in seen:
                seen.add(key)
                unique.append(e)
        return unique[:20]
