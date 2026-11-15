"""Anthropic SDK（Messages API）。

base_url 不带 /v1；SDK 默认发的 x-api-key 头网关直接认。
The base URL has no /v1; the x-api-key header the SDK sends is accepted as is.
"""

import os

from anthropic import Anthropic

client = Anthropic(
    base_url="https://api.dflop.top",
    api_key=os.environ["PLATFORM_API_KEY"],
)

message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "用三点概括什么是 API 网关。Summarise what an API gateway is in three points."}],
)
print(message.content[0].text)

# 同一个 SDK 也能调别家的模型，例如 GPT（网关自动转换协议）。
# The same SDK can call other vendors' models too, e.g. GPT (the gateway translates).
message = client.messages.create(
    model="gpt-6-luna",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content[0].text)
