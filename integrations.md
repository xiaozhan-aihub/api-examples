# 在常用工具里接入 · Using the gateway in common tools

小战AIhub 的对话接口与 OpenAI 兼容，所以凡是能填「OpenAI API 地址」或「OpenAI 兼容服务商」的工具都能直接用。
三样东西就够了：

| 项 | 值 |
|---|---|
| API 地址（Base URL） | `https://api.dflop.top/v1` |
| API Key | `sk-gpushare-` 开头的密钥（在 [控制台](https://model.dflop.top/dashboard/keys) 创建） |
| 模型 | 调用 ID，例如 `gpt-6-luna`、`claude-sonnet-5`、`gemini-3.8-flash`、`deepseek-v4.1-flash`、`kimi-k3`（[完整列表](https://github.com/xiaozhan-aihub/ai-model-api-pricing)） |

The chat API is OpenAI-compatible: any tool that accepts a custom OpenAI base URL works with
`https://api.dflop.top/v1`, an `sk-gpushare-` key and a model id from the list.

## 编程工具 · Coding tools

| 工具 | 怎么填 | 详细步骤 |
|---|---|---|
| Cursor | Settings → Models → OpenAI API Key：勾选 Override OpenAI Base URL，填 `https://api.dflop.top/v1`；先 Add Model 填调用 ID，再关掉内置的 OpenAI 模型，最后 Verify | [文档](https://model.dflop.top/docs/integrations/cursor) |
| Cline（VS Code） | API Provider 选 OpenAI Compatible，Base URL `https://api.dflop.top/v1`，Model ID 填调用 ID | [文档](https://model.dflop.top/docs/integrations/cline) |
| Continue（VS Code / JetBrains） | `config.yaml` 里 `provider: openai`、`apiBase: https://api.dflop.top/v1`、`model` 填调用 ID | [文档](https://model.dflop.top/docs/integrations/continue) |

## 聊天客户端 · Chat apps

| 工具 | 怎么填 | 详细步骤 |
|---|---|---|
| Open WebUI | Settings → Connections → OpenAI API：API Base URL `https://api.dflop.top/v1`，Key 填密钥；模型列表会自动拉取，建议在 Models 里关掉生图、视频这类非对话模型 | [文档](https://model.dflop.top/docs/integrations/open-webui) |
| Cherry Studio、Chatbox、LobeChat、NextChat 等 | 添加一个 OpenAI（或「OpenAI 兼容」）类型的服务商：API 地址填 `https://api.dflop.top/v1`（只让填域名的客户端填 `https://api.dflop.top`，它会自己补 `/v1`），密钥填 `sk-gpushare-…`，模型名填调用 ID | — |

## 中转与工作流平台 · Relays and workflow tools

| 工具 | 怎么填 | 详细步骤 |
|---|---|---|
| New API / One API | 渠道类型选 OpenAI，Base URL 填 `https://api.dflop.top`（**不带** `/v1`），点「获取模型列表」；余额列能正常显示 | [文档](https://model.dflop.top/docs/integrations/new-api) |
| Dify | 模型供应商里添加「OpenAI-API-compatible」，API endpoint 填 `https://api.dflop.top/v1`，模型名填调用 ID | — |
| n8n | OpenAI 凭证里把 Base URL 改成 `https://api.dflop.top/v1` | — |

## 开发框架 · Frameworks

| 框架 | 示例 |
|---|---|
| OpenAI SDK（Python / Node.js） | [python/chat.py](python/chat.py) · [node/chat.mjs](node/chat.mjs) |
| Anthropic SDK | [python/anthropic_messages.py](python/anthropic_messages.py)（`base_url` 不带 `/v1`） |
| Google Gen AI SDK | [python/gemini_native.py](python/gemini_native.py) |
| LangChain | [python/langchain_chat.py](python/langchain_chat.py)：`ChatOpenAI(base_url="https://api.dflop.top/v1", ...)` |
| LlamaIndex | `OpenAILike(model="gpt-6-luna", api_base="https://api.dflop.top/v1", api_key=..., is_chat_model=True)` |
| Vercel AI SDK | [node/ai_sdk.mjs](node/ai_sdk.mjs)：`createOpenAICompatible({ baseURL: "https://api.dflop.top/v1", ... })` |

生图、视频、音乐和语音不走对话接口，在这些工具里选它们会报错；它们的调用方式见 [README](README.md#3-按场景找示例)。
Image, video, music and speech models use their own endpoints, not the chat API; see the [README](README.md#3-按场景找示例).
