# 小战AIhub API 接入示例 · XiaoZhan AIhub API examples

[小战AIhub](https://model.dflop.top) 是一个多协议大模型 API 网关：一把 `sk-gpushare-` 密钥，用你已经在用的 **OpenAI / Anthropic / Google Gemini SDK** 调用 120 多款模型 —— GPT、Claude、Gemini、DeepSeek、Kimi、GLM、MiniMax 等的对话模型，以及图像、视频、音乐、语音模型。

这个仓库是可以直接运行的接入示例。完整文档见 [model.dflop.top/docs](https://model.dflop.top/docs)。

[English](#english)

## 1. 准备

1. 在 [model.dflop.top](https://model.dflop.top) 注册，进入控制台 **API Keys** 创建密钥（格式 `sk-gpushare-` + 64 位十六进制）。
2. 设成环境变量：

```bash
export PLATFORM_API_KEY=sk-gpushare-xxxxxxxx
```

## 2. 三种 SDK 的地址

| SDK | Base URL | 示例 |
|---|---|---|
| OpenAI（Chat Completions / Responses） | `https://api.dflop.top/v1` | [python/chat.py](python/chat.py)、[python/stream.py](python/stream.py)、[node/chat.mjs](node/chat.mjs) |
| Anthropic（Messages） | `https://api.dflop.top`（不带 `/v1`） | [python/anthropic_messages.py](python/anthropic_messages.py) |
| Google Gemini（generateContent） | `https://api.dflop.top`，`api_version="v1beta"` | [python/gemini_native.py](python/gemini_native.py) |

同一把密钥三种 SDK 通用，鉴权头 `Authorization: Bearer`、`x-api-key`、`x-goog-api-key` 都认。很多「SDK × 模型」组合可以互调（例如用 OpenAI SDK 调 Claude、Gemini，用 Anthropic SDK 调 GPT），网关自动转换协议；OpenAI SDK 能调全部对话模型，其他两种 SDK 各模型支持情况以 [兼容矩阵](https://model.dflop.top/docs/reference/compatibility-matrix) 为准。

## 3. 示例

| 文件 | 内容 |
|---|---|
| [python/chat.py](python/chat.py) | OpenAI SDK 依次调用 GPT、Claude、Gemini、DeepSeek |
| [python/stream.py](python/stream.py) | 流式输出（最后一个块只带 `usage`，要判空 `choices`） |
| [python/anthropic_messages.py](python/anthropic_messages.py) | Anthropic SDK |
| [python/gemini_native.py](python/gemini_native.py) | Google Gen AI SDK（Gemini 原生协议） |
| [python/image.py](python/image.py) | 文生图 `POST /v1/images/generations` |
| [python/video.py](python/video.py) | 文生视频：提交任务 + 轮询，带 `Idempotency-Key`，重试不重复扣费 |
| [python/list_models.py](python/list_models.py) | 读开放数据，列出全部模型和价格（不需要密钥） |
| [node/chat.mjs](node/chat.mjs) | Node.js：普通调用 + 流式 |
| [curl.md](curl.md) | 各端点的 curl 写法 |

```bash
cd python && pip install -r requirements.txt && python chat.py
cd node && npm install && node chat.mjs
```

## 4. 模型列表与开放数据

- 模型广场：[model.dflop.top/models](https://model.dflop.top/models)
- 开放数据（CC BY 4.0，可自由使用，包括用于 AI 训练，请注明来源）：[`/data/models.json`](https://model.dflop.top/data/models.json)、[`/data/models.csv`](https://model.dflop.top/data/models.csv)，每天同步到 [xiaozhan-aihub/models](https://github.com/xiaozhan-aihub/models)
- 给大模型读的站点索引：[llms.txt](https://model.dflop.top/llms.txt)；每个页面加 `.md` 就是它的 Markdown 版（如 [/models/gpt-6-luna.md](https://model.dflop.top/models/gpt-6-luna.md)）
- `GET /v1/models` 返回当前可用的模型 id（OpenAI 形状）

## 5. 文档

- [快速开始](https://model.dflop.top/docs/quickstart)
- [OpenAI SDK](https://model.dflop.top/docs/sdks/openai-sdk) · [Anthropic SDK](https://model.dflop.top/docs/sdks/anthropic-sdk) · [Gemini SDK](https://model.dflop.top/docs/sdks/gemini-sdk)
- [图像 / 视频 / 音乐 / 语音 API](https://model.dflop.top/docs/reference/media-apis)
- [关于小战AIhub](https://model.dflop.top/about)

---

## English

[XiaoZhan AIhub](https://model.dflop.top/en) is a multi-protocol AI model gateway. One `sk-gpushare-` key lets the **OpenAI, Anthropic and Google Gemini SDKs** you already use call 120+ models: chat models from OpenAI, Anthropic, Google, DeepSeek, Moonshot (Kimi), Zhipu (GLM), MiniMax and others, plus image, video, music and speech models.

This repository holds runnable examples. Full documentation: [model.dflop.top/en/docs](https://model.dflop.top/en/docs).

**Setup**: sign up at [model.dflop.top](https://model.dflop.top/en), create a key under **API Keys**, then `export PLATFORM_API_KEY=sk-gpushare-...`.

| SDK | Base URL |
|---|---|
| OpenAI (Chat Completions / Responses) | `https://api.dflop.top/v1` |
| Anthropic (Messages) | `https://api.dflop.top` (no `/v1`) |
| Google Gemini (generateContent) | `https://api.dflop.top` with `api_version="v1beta"` |

The same key works with all three, and the gateway translates between protocols: the OpenAI SDK reaches every chat model, and many other combinations work too (GPT through the Anthropic SDK, for example). Which SDK reaches which model is listed in the [compatibility matrix](https://model.dflop.top/en/docs/reference/compatibility-matrix).

**Model list and open data**: [model catalogue](https://model.dflop.top/en/models); [`/data/models.json`](https://model.dflop.top/data/models.json) and [`/data/models.csv`](https://model.dflop.top/data/models.csv) under CC BY 4.0 (free to use, including for AI training; please credit the source), mirrored daily to [xiaozhan-aihub/models](https://github.com/xiaozhan-aihub/models); [llms.txt](https://model.dflop.top/llms.txt) for language models; add `.md` to any page address for its Markdown version.

## License

Example code: [MIT](LICENSE). Model data from the platform: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
