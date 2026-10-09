> _**Originally published on [andrew.ooo](https://andrew.ooo/posts/open-llm-vtuber-offline-ai-companion-review/)** — visit the original for any updates, code snippets that aged out, or follow-up posts._


## TL;DR

**Open-LLM-VTuber** is the open-source attempt at a fully-offline [neuro-sama](https://www.twitch.tv/vedal987) clone — and this week it hit **10,447 stars (+2,388 in seven days)** on GitHub Trending. It bolts together a local LLM, swappable ASR/TTS, a Live2D talking avatar, and a desktop-pet renderer into a single voice-interactive AI companion that runs on Windows, macOS, and Linux.

- **Fully offline**: Ollama / LM Studio / vLLM / GGUF for the brain, sherpa-onnx or FunASR for the ears, sherpa-onnx / GPTSoVITS / CosyVoice for the mouth. No internet required for inference.
- **Hands-free voice loop**: real-time ASR with voice-activity detection, **interruption without headphones** (the AI doesn't hear its own voice — solved via echo cancellation).
- **Live2D avatar**: emotion mapping pushes Cubism expressions from the LLM ("set emotion: surprised"), plus touch-feedback and a transparent **desktop-pet mode** with global top-most and mouse click-through.
- **Visual perception**: webcam, screen capture, and screenshots feed a multimodal LLM so the companion can react to what it sees.
- **10K+ stars, 2.4K this week**, MIT-licensed (Python core), Live2D sample models under Live2D Inc.'s separate license.
- **v2.0 rewrite in progress** on the Zulip community — v1 is still maintained but feature-frozen.

If you've been waiting for the open-source answer to neuro-sama / character.ai voice mode / Vedal's commercial stack, this is the most complete free option in 2026. It's rough, opinionated, and still v1 — but it works.

## Quick Reference

| Field | Value |
|---|---|
| **Repo** | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) |
| **Author** | t41372 (Yi-Ting) + 80+ contributors |
| **Stars** | 10,447 (+2,388 this week — #4 on GitHub Trending Python) |
| **Language** | Python 3.10+ (FastAPI backend) + Electron desktop client |
| **License** | MIT (Live2D sample models under separate Live2D Inc. license) |
| **Install** | `uv` (Python deps) + `ffmpeg` + optional `deeplx` |
| **Platforms** | Windows, macOS (NVIDIA + Apple Silicon), Linux |
| **LLM backends** | Ollama, OpenAI-compatible, Gemini, Claude, Mistral, DeepSeek, Zhipu, GGUF, LM Studio, vLLM |
| **ASR backends** | sherpa-onnx, FunASR, Faster-Whisper, Whisper.cpp, Groq Whisper, Azure |
| **TTS backends** | sherpa-onnx, pyttsx3, MeloTTS, Coqui-TTS, GPTSoVITS, Bark, CosyVoice, Edge TTS, Fish Audio, Azure |
| **Docs** | [open-llm-vtuber.github.io/docs/quick-start](https://open-llm-vtuber.github.io/docs/quick-start) |

## What is Open-LLM-VTuber Actually?

It's a **voice-first AI companion**, not a chatbot with a face glued on. The architecture is built around the voice loop, and the Live2D avatar exists to give the LLM a body so emotions and expressions feel anchored.

The pipeline, end-to-end:

```plaintext
Microphone → VAD → ASR (FunASR/Whisper) → LLM (Ollama/vLLM/Claude API)
   ↓                                              ↓
Echo cancel ← Live2D emotion ← parse response ← stream tokens
                ↓                  ↓
            Avatar render      TTS (CosyVoice/GPTSoVITS) → Speaker
```

Every box is a swappable module. The `conf.yaml` file is the entire configuration surface — you flip backends by changing strings:

```yaml
# conf.yaml — minimal local-only setup
character_config:
  conf_name: "mao"          # Live2D model folder
  conf_uid: "mao_v1"
  live2d_model_name: "mao_pro_jp"
  human_name: "User"
  ai_name: "Mao"
  voice_interruption: true   # interrupt AI mid-sentence

  agent_config:
    conversation_agent_choice: "basic_memory_agent"
    agent_settings:
      basic_memory_agent:
        llm_provider: "ollama_llm"
    llm_configs:
      ollama_llm:
        base_url: "http://localhost:11434/v1"
        model: "qwen2.5:7b"
        temperature: 0.7

  asr_config:
    asr_model: "sherpa_onnx_asr"
    sherpa_onnx_asr:
      model_type: "sense_voice"        # Chinese + English + Japanese + Cantonese
      provider: "cpu"

  tts_config:
    tts_model: "sherpa_onnx_tts"
    sherpa_onnx_tts:
      vits_model: "./models/vits-melo-tts-zh_en/model.onnx"
      vits_lexicon: "./models/vits-melo-tts-zh_en/lexicon.txt"
      vits_tokens: "./models/vits-melo-tts-zh_en/tokens.txt"
      provider: "cpu"
```

That's the whole config for a fully-offline voice companion. Swap `ollama_llm` for `openai_compatible_llm` to use Groq, swap `sherpa_onnx_asr` for `faster_whisper_asr` for better English, and you're done.

## Install in 60 Seconds (macOS / Linux)

```bash
# 1. Install uv (Astral's Python package manager — Open-LLM-VTuber requires it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone
git clone https://github.com/Open-LLM-VTuber/Open-LLM-VTuber.git
cd Open-LLM-VTuber

# 3. Install Python deps (uv resolves everything via pyproject.toml)
uv sync

# 4. Install ffmpeg (TTS post-processing + audio resampling)
brew install ffmpeg          # macOS
# sudo apt install ffmpeg    # Debian/Ubuntu

# 5. Pull an LLM
ollama pull qwen2.5:7b

# 6. Run
uv run run_server.py
```

Open `http://localhost:12393` in your browser, grant microphone permission, and start talking. The Live2D model loads automatically with the default `mao` character.

For the desktop pet (transparent background, click-through, always-on-top), grab the Electron client from the [Releases page](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber/releases) and point it at your running server.

## What Actually Impressed Me

### 1. Voice interruption that works without headphones

This is the killer feature. Most local voice-assistant projects assume you wear headphones because the microphone picks up the assistant's own TTS output and causes feedback or loops. Open-LLM-VTuber implements **acoustic echo cancellation** in the browser's `MediaStreamTrack` pipeline so the ASR ignores audio that the TTS just played. The result: you can interrupt mid-sentence on a laptop's built-in speakers and microphone, and the AI shuts up cleanly.

### 2. Emotion mapping is structured, not vibes

The LLM is prompted to emit emotion tags inline:

```plaintext
[joy] That's great to hear! [neutral] What did you do today?
```

A regex in the response stream extracts `[joy]`, `[neutral]`, `[surprise]`, `[sad]`, etc., and pushes them to the Live2D model's expression parameter via WebSocket. You can map any tag to any Live2D expression in `model_dict.json`:

```json
{
  "name": "mao_pro_jp",
  "url": "/live2d-models/mao_pro_jp/runtime/mao_pro.model3.json",
  "kScale": 0.15,
  "initialXshift": 0,
  "initialYshift": 0,
  "emotionMap": {
    "neutral": 0,
    "anger":   1,
    "disgust": 2,
    "fear":    3,
    "joy":     4,
    "sad":     5,
    "surprise": 6
  },
  "tapMotions": {
    "head":   {"head_motion": 30, "tap_body": 70},
    "body":   {"shake": 50, "tap_body": 50}
  }
}
```

Touch events on the Live2D canvas trigger random motions weighted by region. It's the level of polish that makes the avatar feel alive rather than a static PNG.

### 3. Visual perception is opt-in, not creepy

The webcam and screen-share streams are off by default. Enabling them sends a frame to the LLM only on demand — when the user explicitly clicks the camera/screenshot button, or when the LLM emits a `[see]` tag asking to look. There's no continuous video pipe to OpenAI by default; with a multimodal local model (LLaVA, MiniCPM-V via Ollama), nothing leaves your machine.

### 4. The pet mode is genuinely fun

The Electron client supports a **transparent borderless window with click-through** so the Live2D model sits on your desktop without trapping mouse clicks. You can drag it anywhere, and it talks to you while you work. It's the closest open-source equivalent to a Windows desktop pet from the 2000s, but with an LLM brain.

## Community Reactions

From r/LocalLLaMA, r/NeuroSama, and the project's [Zulip](https://olv.zulipchat.com) (paraphrased — go read the threads):

- **"Finally an open neuro-sama"** — top sentiment in r/NeuroSama; people have been begging for a hackable companion since Vedal made his stack closed-source.
- **"sherpa-onnx + qwen2.5:7b runs fully on my M1 Air, 6GB RAM hit, ~1.5s latency"** — multiple reports of usable performance on modest hardware.
- **"Long-term memory is gone in v1.0.0, that hurts"** — the maintainer (`t41372`) confirmed long-term memory is being rebuilt for v2.0; the v1 memgpt integration was deprecated.
- **"The Chinese-first docs are a barrier"** — README is now in English/JP/KR/中文 but parts of the documentation site still default to Chinese. PRs welcome.
- **"Live2D model licensing is confusing for streamers"** — the sample models ship under Live2D Inc.'s free-material license, which permits non-commercial use; commercial streaming likely needs a Live2D Cubism Pro subscription.

## Honest Limitations

After three days of running it on an M2 Pro Mac mini with `qwen2.5:7b` via Ollama and `sherpa_onnx_asr` + `sherpa_onnx_tts`:

- **Latency stack adds up**. ASR ~200ms + 7B LLM time-to-first-token ~600ms + TTS first chunk ~400ms = ~1.2s before you hear the response start. Good for chat, bad for snappy back-and-forth. Smaller LLMs (Qwen 1.5B, Llama 3.2 1B) cut this in half but lose personality.
- **Long-term memory is missing in v1.0.0**. Chat logs persist to disk so you can resume conversations, but there's no automatic recall across sessions. The maintainer is rebuilding this in v2.0; in the meantime, you can graft mem0/Letta via the Agent interface.
- **macOS GPU acceleration is partial**. Sherpa-onnx and Whisper.cpp benefit from Apple's Accelerate framework, but TTS models (especially GPTSoVITS) still default to CPU on M-series and the first inference per session takes 5–10s.
- **The v2.0 rewrite is real**. The maintainer is open about v1 being feature-frozen and most new development moving to v2 (which is in design discussion as of June 2026). If you build heavily on v1's plugin interface, expect breakage.
- **No Docker image in the official repo right now**. There's a community Dockerfile but it lags behind. Bare-metal `uv run` is the supported path.
- **Live2D Inc.'s license is a sharp edge for commercial use**. The sample `mao`, `shizuku`, `Hiyori`, and `Mark` models are free for non-commercial use but require a Live2D Cubism Pro license for commercial streaming. Use your own Live2D model or a permissively-licensed third-party one if you plan to monetize.
- **Multi-user is single-tenant**. The server happily serves one voice session at a time. If you want a multi-user companion service, you'll need a frontend that proxies multiple isolated server instances.

## Where It Fits in the Stack

| Use Case | Open-LLM-VTuber | Alternative |
|---|---|---|
| **Offline desktop AI companion / waifu** | ✅ Best in class | z-waif, LLM-Live2D-Desktop-Assistant |
| **Streaming AI VTuber (neuro-sama clone)** | ✅ Designed for it | Vedal's stack (closed), Voxta (commercial) |
| **Voice-only assistant (Siri replacement)** | ⚠️ Possible but heavy | [Home Assistant Assist](https://www.home-assistant.io/voice_control/), Mycroft fork |
| **Headless voice agent / API** | ❌ Not the focus | LiveKit Agents, pipecat, [Dograh](/posts/dograh-open-source-voice-ai-vapi-alternative-review/) |
| **Phone-call voice AI** | ❌ Wrong stack | Vapi, Retell, Dograh |
| **Multimodal screen-aware agent** | ⚠️ Works with vision LLM | Claude Computer Use, [Cua](/posts/trycua-cua-open-source-computer-use-agents/) |

## Code: Custom Agent Plugin

The `agent_config.conversation_agent_choice` lets you inherit and ship your own agent. Here's a minimal example that wraps a Letta agent for long-term memory:

```python
# agents/agents/letta_agent.py
from typing import AsyncIterator
from agents.agent_interface import AgentInterface
from letta import create_client

class LettaAgent(AgentInterface):
    def __init__(self, agent_id: str, base_url: str = "http://localhost:8283"):
        self.client = create_client(base_url=base_url)
        self.agent_id = agent_id

    async def chat(self, user_input: str) -> AsyncIterator[str]:
        # Letta handles long-term memory + tool calls server-side
        response = self.client.user_message(
            agent_id=self.agent_id,
            message=user_input,
            stream=True,
        )
        async for chunk in response:
            if chunk.message_type == "assistant_message":
                yield chunk.content

    async def handle_interrupt(self):
        # Called when user starts speaking mid-response
        pass
```

Register it in `conf.yaml`:

```yaml
agent_config:
  conversation_agent_choice: "letta_agent"
  agent_settings:
    letta_agent:
      agent_id: "agent-12345"
      base_url: "http://localhost:8283"
```

Restart the server and your VTuber now has persistent cross-session memory via Letta — without touching the voice pipeline.

## FAQ

### How does Open-LLM-VTuber compare to z-waif and LLM-Live2D-Desktop-Assistant?

**z-waif** is single-author, opinionated, focuses on personality + RAG memory, and ships a polished Windows experience but is harder to extend. **LLM-Live2D-Desktop-Assistant** (by the same author as Open-LLM-VTuber) is the Tauri/Rust desktop-pet sibling — lighter footprint but fewer features. **Open-LLM-VTuber** is the most extensible: the broadest LLM/ASR/TTS backend matrix, the cleanest plugin interface, and the largest contributor base. Pick z-waif if you want one-click Windows install, Open-LLM-VTuber if you want to customize anything.

### Can I run Open-LLM-VTuber fully offline on a MacBook?

Yes, and that's the design center. On a 16GB M1 Air with `qwen2.5:7b` via Ollama + `sense_voice` ASR + sherpa-onnx MeloTTS, you get ~1.5s round-trip latency and ~6GB resident RAM. M2/M3 with 24GB+ can step up to Qwen2.5-14B or Llama 3.2 11B vision for better answers and visual perception, at ~2.5s latency.

### Does it work with Claude or GPT-5?

Yes — set `llm_provider: "openai_compatible_llm"` and point `base_url` at any OpenAI-compatible endpoint (Anthropic via [LiteLLM](https://github.com/BerriAI/litellm), OpenRouter, Groq, Together, Fireworks, or self-hosted vLLM). You lose offline-mode and gain quality. Most users do a hybrid: local Whisper + Cloud LLM + local TTS for cost vs latency tuning.

### Can I use my own Live2D model?

Yes. Drop the unpacked Cubism model into `live2d-models/<your_model_name>/` and add an entry to `model_dict.json` with the `emotionMap`, `tapMotions`, and `idleMotionGroup` fields. The docs cover [character customization](https://open-llm-vtuber.github.io/docs/user-guide/live2d) in detail. Custom models also let you sidestep the Live2D Inc. sample-model commercial-use restrictions.

### Is the visual perception (webcam, screen capture) sent to the cloud?

Only if your configured LLM is a cloud LLM. If you use a local multimodal model (LLaVA-1.6, MiniCPM-V, Qwen2.5-VL via Ollama, or LM Studio), the image stays on your machine. Visual perception is also opt-in per request — there's no continuous video stream to the LLM, only frames captured on user click or explicit `[see]` tag from the agent.

### How does this compare to character.ai voice mode or OpenAI's Advanced Voice?

Open-LLM-VTuber is **local, free, and customizable**; the cloud options are **smarter, lower latency, and have better TTS**. OpenAI's Advanced Voice is a single end-to-end model with sub-500ms latency that Open-LLM-VTuber can't match with a pipeline of separate ASR/LLM/TTS. But: cloud voice modes don't give you a Live2D avatar, can't run offline, charge per minute, and can be revoked. Pick Open-LLM-VTuber if privacy, customization, or the visual companion experience matter more than raw conversational quality.

### What's coming in v2.0?

Per the [Zulip](https://olv.zulipchat.com) discussions: a full rewrite around an event-driven core, proper multi-tenant support, restored long-term memory (Mem0 or Letta-native), Live2D Cubism 5 support, and a redesigned plugin API. No release date — the maintainer is consciously taking time to get the architecture right.

## Should You Use It?

**Yes** if you want a hackable, offline AI companion with a face, you're willing to tune `conf.yaml`, and you can live with v1's missing long-term memory. The voice loop quality is the best open-source voice-companion experience available in June 2026, and the active 80+ contributor community plus the planned v2.0 rewrite signal real momentum.

**No** if you want a polished one-click experience (use [z-waif](https://github.com/luna-saito/z-waif) on Windows or pay for [Voxta](https://voxta.ai/)), you need sub-500ms latency (use OpenAI Advanced Voice), or you want to monetize streaming with the sample Live2D models (license your own).

Star the repo, lurk on [Zulip](https://olv.zulipchat.com), and watch v2.0 — this is the open-source companion stack to bet on.
