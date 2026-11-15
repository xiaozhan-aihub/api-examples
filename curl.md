# curl

```bash
export PLATFORM_API_KEY=sk-gpushare-xxxxxxxx
```

## 对话 · Chat Completions (OpenAI)

```bash
curl https://api.dflop.top/v1/chat/completions \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-6-luna", "messages": [{"role": "user", "content": "Hello"}]}'
```

流式加 `"stream": true`（加 `-N` 关掉 curl 的缓冲）。Add `"stream": true` (and `-N`) for streaming.

## Messages (Anthropic)

```bash
curl https://api.dflop.top/v1/messages \
  -H "x-api-key: $PLATFORM_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"model": "claude-sonnet-5", "max_tokens": 1024, "messages": [{"role": "user", "content": "Hello"}]}'
```

## generateContent (Gemini)

```bash
curl "https://api.dflop.top/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "Hello"}]}]}'
```

## 文生图 · Images

```bash
curl https://api.dflop.top/v1/images/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  --max-time 300 \
  -d '{"model": "gpt-image-2", "prompt": "一只在竹林里喝茶的熊猫，水彩风格，画面比例 1:1"}'
```

## 文生视频 · Videos (submit + poll)

```bash
curl https://api.dflop.top/v1/videos/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{"model": "doubao-seedance-2.0", "content": [{"type": "text", "text": "海边日落，无人机航拍视角"}], "duration": 5, "resolution": "720p", "ratio": "16:9"}'

curl https://api.dflop.top/v1/videos/generations/$TASK_ID \
  -H "Authorization: Bearer $PLATFORM_API_KEY"
```

## 模型与余额 · Models and balance

```bash
curl https://api.dflop.top/v1/models -H "Authorization: Bearer $PLATFORM_API_KEY"
curl https://api.dflop.top/v1/key/balance -H "Authorization: Bearer $PLATFORM_API_KEY"

# 开放数据，不需要密钥。Open data, no key needed (CC BY 4.0).
curl https://model.dflop.top/data/models.json
```

更多：[API 参考](https://model.dflop.top/docs/reference/api-reference) · [图像 / 视频 / 音乐 / 语音](https://model.dflop.top/docs/reference/media-apis)
