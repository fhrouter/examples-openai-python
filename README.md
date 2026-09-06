# FHRouter Python Examples — Free LLM API via the OpenAI SDK

Minimal Python examples for calling [FHRouter](https://fhrouter.com) with the official OpenAI SDK. The free tier includes frontier models (Grok 4.6, DeepSeek V4 Flash, GLM 5.3 Flash) on every account — no credit card.

> **Free tier:** frontier AI models (Grok, DeepSeek, GLM) free on every [FHRouter](https://fhrouter.com) account — no credit card. [Free LLM API](https://fhrouter.com/free-llm-api) · [How free models work](https://fhrouter.com/docs/free-models)

## Setup

```bash
pip install openai
export FHROUTER_API_KEY="your-key"   # create at https://fhrouter.com/token
```

All examples use base URL `https://fhrouter.com/v1` — the whole [OpenAI-compatible API](https://fhrouter.com/docs/api-reference) works: streaming, tool calls, embeddings, OpenAI-shaped errors.

## Files

- [`chat.py`](chat.py) — simple chat call to a free model
- [`streaming.py`](streaming.py) — token-by-token streaming
- [`list_models.py`](list_models.py) — list models your key can call

## Free models

Current free set: `grok-4.6`, `deepseek-v4-flash`, `glm-5.3-flash` (rotates — see the [live catalog](https://fhrouter.com/free-llm-api)).

## Links

- [FHRouter](https://fhrouter.com) — the gateway
- [Free LLM API](https://fhrouter.com/free-llm-api) — the free tier
- [Docs](https://fhrouter.com/docs) · [API reference](https://fhrouter.com/docs/api-reference) · [Blog](https://fhrouter.com/blog)
- Setup guides: [Claude Code](https://fhrouter.com/docs/guides/claude-code) · [Codex CLI](https://fhrouter.com/docs/guides/codex) · [Gemini CLI](https://fhrouter.com/docs/guides/gemini)

---

<sub>Examples only — FHRouter itself runs at [fhrouter.com](https://fhrouter.com). Sign up and start calling frontier models for free in minutes.</sub>
