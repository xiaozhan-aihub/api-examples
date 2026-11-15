"""OpenAI Responses API（POST /v1/responses），带联网检索。
The OpenAI Responses API with the built-in web_search tool.

多轮对话请每轮把完整历史放进 input（网关不保存会话，previous_response_id 不可用）。
Keep the whole history in `input` on every turn (previous_response_id is not available).
"""

import os

from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.responses.create(
    model="gpt-6-luna",
    instructions="回答简洁，给出处。Be concise and cite sources.",
    input=[{"role": "user", "content": "最近一周有哪些新发布的大模型？What new AI models came out this week?"}],
    tools=[{"type": "web_search"}],
    reasoning={"effort": "medium"},
)
print(resp.output_text)
