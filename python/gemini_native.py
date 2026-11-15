"""Google Gen AI SDK（Gemini 原生协议 generateContent）。

SDK 默认发的 x-goog-api-key 头网关直接认。
The x-goog-api-key header the SDK sends is accepted as is.
"""

import os

from google import genai

client = genai.Client(
    api_key=os.environ["PLATFORM_API_KEY"],
    http_options={"base_url": "https://api.dflop.top", "api_version": "v1beta"},
)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="解释一下什么是向量数据库，100 字以内。Explain vector databases in under 60 words.",
)
print(response.text)
