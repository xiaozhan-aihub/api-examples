# curl 示例 · curl examples

各端点的 curl 写法。同一把 `sk-gpushare-` 密钥通用。
Every endpoint with curl; one `sk-gpushare-` key for all of them.

```bash
export PLATFORM_API_KEY=sk-gpushare-xxxxxxxx
```

- [对话 · Chat Completions](#对话--chat-completions-openai)
- [OpenAI Responses（联网检索）](#openai-responses联网检索)
- [Anthropic Messages](#messages-anthropic)
- [Gemini generateContent](#generatecontent-gemini)
- [文生图 · 图生图 · GIF](#文生图--images)
- [文生视频 · 图生视频](#文生视频--videos)
- [AI 音乐 · Suno](#ai-音乐--music-suno)
- [语音合成 · TTS](#语音合成--text-to-speech)
- [模型与余额](#模型与余额--models-and-balance)

## 对话 · Chat Completions (OpenAI)

```bash
curl https://api.dflop.top/v1/chat/completions \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-6-luna", "messages": [{"role": "user", "content": "Hello"}]}'
```

`model` 换成任意对话模型的调用 ID（`claude-sonnet-5`、`gemini-3.8-flash`、`deepseek-v4.1-flash`、`kimi-k3`、`glm-5.3`、`grok-4.7` …）。
流式加 `"stream": true`（加 `-N` 关掉 curl 的缓冲）。Add `"stream": true` (and `-N`) for streaming.

## OpenAI Responses（联网检索）

```bash
curl https://api.dflop.top/v1/responses \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-6-luna",
    "input": [{"role": "user", "content": "今天有什么科技新闻？"}],
    "tools": [{"type": "web_search"}]
  }'
```

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
# 文生图。gpt-image-2 不读 size，比例写在提示词里；客户端超时请设 300 秒以上。
curl https://api.dflop.top/v1/images/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  --max-time 300 \
  -d '{"model": "gpt-image-2", "prompt": "一只在竹林里喝茶的熊猫，水彩风格，画面比例 1:1"}'

# 指定尺寸（Seedream 5.0 的尺寸下限约 1920x1920）
curl https://api.dflop.top/v1/images/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "doubao-seedream-5-0-260128", "prompt": "赛博朋克风格的城市夜景", "size": "2048x2048"}'

# 图生图：上传本地文件
curl https://api.dflop.top/v1/images/edits \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  --max-time 300 \
  -F "model=gpt-image-2" \
  -F "prompt=把沙发改成蓝色，其余保持不变" \
  -F "image[]=@original.png"

# GIF 动图（GPT-Image 2.6）
curl https://api.dflop.top/v1/images/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  --max-time 300 \
  -d '{"model": "gpt-image-2.6-flare", "prompt": "一只卡通小猫挥手打招呼，循环动画", "output_format": "gif", "size": "512x512", "frame_count": 9, "frame_duration_ms": 200}'
```

长耗时可以在请求体里加 `"async": true` 改成提交 + 轮询 `GET /v1/images/generations/{id}`。返回的图片链接约 24 小时有效。

## 文生视频 · Videos

```bash
# 提交（带 Idempotency-Key，重试不会重复扣费）
curl https://api.dflop.top/v1/videos/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{"model": "doubao-seedance-2.0", "content": [{"type": "text", "text": "海边日落，无人机航拍视角"}], "duration": 5, "resolution": "720p", "ratio": "16:9"}'

# 图生视频：content 里加一张首帧图
curl https://api.dflop.top/v1/videos/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{"model": "tvod-kling-video-3.0", "content": [{"type": "text", "text": "人物转身望向远方"}, {"type": "image_url", "image_url": {"url": "https://your-cdn.com/first-frame.jpg"}}], "duration": 5}'

# 轮询（一般 1–5 分钟），以及列出最近的任务
curl https://api.dflop.top/v1/videos/generations/$TASK_ID -H "Authorization: Bearer $PLATFORM_API_KEY"
curl "https://api.dflop.top/v1/videos/generations?limit=10" -H "Authorization: Bearer $PLATFORM_API_KEY"
```

各模型支持的时长、分辨率、画幅见 [视频模型价格与参数](https://github.com/xiaozhan-aihub/ai-model-api-pricing/blob/main/pricing/video-generation-api.md)。

## AI 音乐 · Music (Suno)

```bash
curl https://api.dflop.top/v1/music/generations \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "suno-v6", "prompt": "一首关于夏天海边散步的轻快中文流行歌"}'

curl https://api.dflop.top/v1/music/generations/$TASK_ID -H "Authorization: Bearer $PLATFORM_API_KEY"
```

一次生成 2 首完整歌曲；自定义歌词传 `lyrics`，曲风传 `tags`，纯音乐传 `"instrumental": true`。

## 语音合成 · Text to speech

```bash
# 同步：返回 JSON，audio_url 是长期有效的 MP3 链接
curl https://api.dflop.top/v1/audio/speech \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "voice-tts-pro", "input": "你好，欢迎使用语音合成。"}'

# 长文案用异步，再轮询 GET /v1/audio/speech/{id}
curl https://api.dflop.top/v1/audio/speech \
  -H "Authorization: Bearer $PLATFORM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "voice-tts-pro", "input": "……很长的文案……", "async": true}'

# 可用音色（平台公共音色 + 你克隆的音色）
curl https://api.dflop.top/v1/audio/voices -H "Authorization: Bearer $PLATFORM_API_KEY"
```

## 模型与余额 · Models and balance

```bash
curl https://api.dflop.top/v1/models -H "Authorization: Bearer $PLATFORM_API_KEY"
curl https://api.dflop.top/v1/key/balance -H "Authorization: Bearer $PLATFORM_API_KEY"

# 开放数据，不需要密钥。Open data, no key needed (CC BY 4.0).
curl https://model.dflop.top/data/models.json
```

更多：[API 参考](https://model.dflop.top/docs/reference/api-reference) · [图像 / 视频 / 音乐 / 语音](https://model.dflop.top/docs/reference/media-apis)
