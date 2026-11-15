"""JSON 输出：response_format={"type": "json_object"}，拿到可以直接 json.loads 的结果。
JSON mode: ask for a JSON object and parse it directly.

提示词里要写明「输出 JSON」和字段。Claude 走 OpenAI 接口时这个参数会被忽略（响应头 X-Protocol-Warning 会说明），
需要严格 JSON 时用 GPT、Gemini、DeepSeek、Kimi、GLM、Qwen 等模型。
Say "JSON" and the fields in the prompt. Through this endpoint Claude ignores response_format.
"""

import json
import os

from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "只输出 JSON，字段：name（字符串）、price_cny（数字）、tags（字符串数组）。"},
        {"role": "user", "content": "从这段话提取商品信息：这款无线降噪耳机售价 899 元，续航 40 小时，支持快充。"},
    ],
)
data = json.loads(resp.choices[0].message.content)
print(data)
