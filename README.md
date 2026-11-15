# 大模型 API 接入示例 · XiaoZhan AIhub API examples

**一把 API Key，用 OpenAI / Anthropic / Google Gemini SDK 调用 GPT、Claude、Gemini、DeepSeek、Kimi、GLM、通义千问、Grok 等 120 多款模型，还有生图、视频、AI 音乐和语音合成。**

[小战AIhub](https://model.dflop.top) 是多协议大模型 API 网关：你已经在用的 SDK 不用换，把 `base_url` 指向网关、`model` 填调用 ID 就行。这个仓库是可以直接运行的示例（Python、Node.js、curl），覆盖对话、流式输出、工具调用、JSON 输出、识图、文生图、图生图、GIF 动图、文生视频、图生视频、Suno 音乐、语音合成，以及 Cursor、Cline、Open WebUI、LangChain、Vercel AI SDK 等工具的接入。

[English](#english) · [模型价格表（每日更新）](https://github.com/xiaozhan-aihub/ai-model-api-pricing) · [文档](https://model.dflop.top/docs)

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key="sk-gpushare-...")
resp = client.chat.completions.create(
    model="claude-sonnet-5",  # 换成 gpt-6-luna、gemini-3.8-flash、deepseek-v4.1-flash、kimi-k3 …
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
```

## 1. 准备

1. 在 [model.dflop.top](https://model.dflop.top) 注册，进入控制台 **API Keys** 创建密钥（格式 `sk-gpushare-` + 64 位十六进制）。
2. 设成环境变量：

```bash
export PLATFORM_API_KEY=sk-gpushare-xxxxxxxx
```

3. 装依赖：

```bash
cd python && pip install -r requirements.txt
cd node && npm install
```

## 2. 三种 SDK 的地址

| SDK | Base URL | 示例 |
|---|---|---|
| OpenAI（Chat Completions / Responses / Images / Audio） | `https://api.dflop.top/v1` | [python/chat.py](python/chat.py)、[node/chat.mjs](node/chat.mjs) |
| Anthropic（Messages） | `https://api.dflop.top`（不带 `/v1`） | [python/anthropic_messages.py](python/anthropic_messages.py) |
| Google Gemini（generateContent） | `https://api.dflop.top`，`api_version="v1beta"` | [python/gemini_native.py](python/gemini_native.py) |

同一把密钥三种 SDK 通用，鉴权头 `Authorization: Bearer`、`x-api-key`、`x-goog-api-key` 都认。OpenAI SDK 能调全部对话模型（网关自动转换协议，例如用 OpenAI SDK 调 Claude、Gemini）；Anthropic SDK、Gemini SDK 各能调哪些模型见 [兼容矩阵](https://model.dflop.top/docs/reference/compatibility-matrix)，或 [价格表的「能力对照」](https://github.com/xiaozhan-aihub/ai-model-api-pricing/blob/main/pricing/llm-api.md#能力对照)。

## 3. 按场景找示例

| 场景 | Python | Node.js / curl | 说明 |
|---|---|---|---|
| 对话 | [chat.py](python/chat.py) | [chat.mjs](node/chat.mjs) · [curl](curl.md#对话--chat-completions-openai) | 同一个客户端换个 `model` 就是另一家的模型 |
| 流式输出 | [stream.py](python/stream.py) | [chat.mjs](node/chat.mjs) | 最后一个块只带 `usage`，`choices` 为空 |
| OpenAI Responses + 联网检索 | [responses.py](python/responses.py) | [curl](curl.md#openai-responses联网检索) | 内置 `web_search` 工具 |
| 工具调用（Function calling） | [tools.py](python/tools.py) | | GPT、Claude、Gemini、DeepSeek、Kimi 同一套写法 |
| JSON 输出 | [json_output.py](python/json_output.py) | | `response_format={"type": "json_object"}` |
| 识图（图片输入） | [vision.py](python/vision.py) | | 本地图片转 data URI |
| Claude 原生（Anthropic SDK） | [anthropic_messages.py](python/anthropic_messages.py) | [curl](curl.md#messages-anthropic) | |
| Gemini 原生（Google Gen AI SDK） | [gemini_native.py](python/gemini_native.py) | [curl](curl.md#generatecontent-gemini) | |
| 文生图 | [image.py](python/image.py) | [image.mjs](node/image.mjs) · [curl](curl.md#文生图--images) | GPT-Image、Seedream、Nano Banana、Qwen Image、可灵图像 |
| 图生图 / 改图 | [image_edit.py](python/image_edit.py) | [curl](curl.md#文生图--images) | 直接上传本地图片 |
| GIF 动图 | [image_gif.py](python/image_gif.py) | [curl](curl.md#文生图--images) | GPT-Image 2.6 |
| 文生视频 | [video.py](python/video.py) | [video.mjs](node/video.mjs) · [curl](curl.md#文生视频--videos) | Seedance、Veo、可灵、Vidu、海螺、万相；提交 + 轮询 |
| 图生视频 | [video_image_to_video.py](python/video_image_to_video.py) | [curl](curl.md#文生视频--videos) | 一张首帧图让它动起来 |
| AI 音乐（Suno V6） | [music.py](python/music.py) | [curl](curl.md#ai-音乐--music-suno) | 一次生成 2 首完整歌曲 |
| 语音合成（TTS） | [tts.py](python/tts.py) | [curl](curl.md#语音合成--text-to-speech) | OpenAI SDK 的 `audio.speech.create` 直接用 |
| LangChain | [langchain_chat.py](python/langchain_chat.py) | | `ChatOpenAI(base_url=...)` |
| Vercel AI SDK | | [ai_sdk.mjs](node/ai_sdk.mjs) | `@ai-sdk/openai-compatible` |
| 列出全部模型和价格 | [list_models.py](python/list_models.py) | [curl](curl.md#模型与余额--models-and-balance) | 读开放数据，不需要密钥 |

在 Cursor、Cline、Continue、Open WebUI、Cherry Studio、Dify、n8n、New API 里怎么填，见 [integrations.md](integrations.md)。

## 4. 常用模型（调用 ID）

| 类别 | 模型 |
|---|---|
| 对话 | `gpt-6-luna`、`gpt-6.1-sol`、`claude-sonnet-5`、`claude-opus-5-5`、`gemini-3.8-flash`、`gemini-4-argon`、`deepseek-v4.1-flash`、`kimi-k3`、`glm-5.3`、`qwen3.8-max-cjx`、`grok-4.7` |
| 生图 | `gpt-image-2`、`gpt-image-2.6-flare`、`doubao-seedream-5-0-260128`、`nano-banana-pro`、`qwen-image-3.0`、`tvod-kling-image-3.0` |
| 视频 | `doubao-seedance-2.0`、`doubao-seedance-2.5`、`tvod-veo-3.1`、`tvod-kling-video-4.0`、`tvod-vidu-video-q3`、`minimax-h3`、`wan3.0-video` |
| 音乐与语音 | `suno-v6`、`voice-tts-pro` |

完整、实时的模型列表和价格：[ai-model-api-pricing](https://github.com/xiaozhan-aihub/ai-model-api-pricing)（每天自动更新，按类别和厂商分页）· [模型广场](https://model.dflop.top/models) · `GET /v1/models`。

## 5. 常见问题

**一把 API Key 能调哪些模型？** 平台上全部模型：对话、生图、视频、音乐和语音，共用同一个账户余额。

**和直接用 OpenAI SDK 有什么不同？** 只改两处：`base_url` 换成 `https://api.dflop.top/v1`，`api_key` 换成 `sk-gpushare-` 密钥；其余写法（流式、工具调用、JSON 输出、识图、Responses）照旧。

**用 OpenAI SDK 调 Claude 或 Gemini 行吗？** 行，网关会自动转换协议。需要 Claude 独有的能力（如 `cache_control`）时，用 Anthropic SDK 调 `/v1/messages` 更完整。

**视频和音乐为什么要轮询？** 它们是异步任务：提交后立即拿到任务 `id`，生成一般要 1–5 分钟。带上 `Idempotency-Key`，网络抖动重试也不会重复扣费；不想轮询可以传 `callback_url`。

**生成的图片、视频能保存多久？** 图片链接约 24 小时，视频链接 7 天，音乐和语音是长期链接。拿到后请转存。

**价格在哪看？** [ai-model-api-pricing](https://github.com/xiaozhan-aihub/ai-model-api-pricing) 每天同步全部模型的价格（CC BY 4.0 开放数据，也在 [Hugging Face](https://huggingface.co/datasets/xiaozhan-aihub/ai-model-api-pricing)），实时价格见 [模型广场](https://model.dflop.top/models)。

## 6. 文档

- [快速开始](https://model.dflop.top/docs/quickstart) · [API 参考](https://model.dflop.top/docs/reference/api-reference)
- [OpenAI SDK](https://model.dflop.top/docs/sdks/openai-sdk) · [Anthropic SDK](https://model.dflop.top/docs/sdks/anthropic-sdk) · [Gemini SDK](https://model.dflop.top/docs/sdks/gemini-sdk)
- [工具调用](https://model.dflop.top/docs/guides/tool-calling) · [流式输出](https://model.dflop.top/docs/guides/streaming) · [图生图](https://model.dflop.top/docs/guides/image-editing) · [任务回调](https://model.dflop.top/docs/guides/webhooks)
- [图像 / 视频 / 音乐 / 语音 API](https://model.dflop.top/docs/reference/media-apis) · [数字人 / 剪辑 API](https://model.dflop.top/docs/reference/digital-human-apis)
- 给大模型读的站点索引：[llms.txt](https://model.dflop.top/llms.txt)；每个页面加 `.md` 就是它的 Markdown 版
- [关于小战AIhub](https://model.dflop.top/about)

---

## English

[XiaoZhan AIhub](https://model.dflop.top/en) is a multi-protocol AI model gateway. One `sk-gpushare-` key lets the **OpenAI, Anthropic and Google Gemini SDKs** you already use call 120+ models: chat models from OpenAI (GPT), Anthropic (Claude), Google (Gemini), DeepSeek, Moonshot (Kimi), Zhipu (GLM), Alibaba (Qwen), xAI (Grok) and MiniMax, image models (GPT-Image, Seedream, Nano Banana, Qwen Image, Kling), video models (Seedance, Veo, Kling, Vidu, Hailuo, Wan), Suno music and text-to-speech.

This repository holds runnable examples in Python, Node.js and curl: chat, streaming, the Responses API with web search, function calling, JSON mode, image input, text-to-image, image editing, animated GIFs, text-to-video, image-to-video, music, text-to-speech, LangChain and the Vercel AI SDK. [integrations.md](integrations.md) shows the settings for Cursor, Cline, Continue, Open WebUI, Dify, n8n and New API.

| SDK | Base URL |
|---|---|
| OpenAI (Chat Completions, Responses, Images, Audio) | `https://api.dflop.top/v1` |
| Anthropic (Messages) | `https://api.dflop.top` (no `/v1`) |
| Google Gemini (generateContent) | `https://api.dflop.top` with `api_version="v1beta"` |

**Setup**: sign up at [model.dflop.top](https://model.dflop.top/en), create a key under **API Keys**, then `export PLATFORM_API_KEY=sk-gpushare-...`.

The OpenAI SDK reaches every chat model; the gateway translates protocols, so Claude and Gemini work through it too. Which models the Anthropic and Gemini SDKs reach is listed in the [compatibility matrix](https://model.dflop.top/en/docs/reference/compatibility-matrix). Video and music are asynchronous tasks: submit, then poll; an `Idempotency-Key` makes retries safe from double charges.

**Prices**: [ai-model-api-pricing](https://github.com/xiaozhan-aihub/ai-model-api-pricing) mirrors the price of every model daily (CC BY 4.0 open data, also on [Hugging Face](https://huggingface.co/datasets/xiaozhan-aihub/ai-model-api-pricing)); the live catalogue is at [model.dflop.top/en/models](https://model.dflop.top/en/models). Documentation: [model.dflop.top/en/docs](https://model.dflop.top/en/docs).

## License

Example code: [MIT](LICENSE). Model data from the platform: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
