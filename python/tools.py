"""工具调用（Function calling）：模型决定调用你的函数，你执行后把结果回填，再拿最终回答。
Function calling: the model asks for a tool, you run it and send the result back.

同一套 OpenAI 写法对 GPT、Claude、Gemini、DeepSeek、Kimi、GLM、Qwen 都适用，网关负责转换协议。
The same OpenAI-style code works for GPT, Claude, Gemini, DeepSeek, Kimi, GLM and Qwen.
"""

import json
import os

from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])
MODEL = "gpt-6-luna"  # 也可以换成 claude-sonnet-5、gemini-3.8-flash、deepseek-v4.1-flash、kimi-k3 …

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询城市当前天气 / Get the current weather in a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "城市名 / city name"}},
            "required": ["city"],
        },
    },
}]


def get_weather(city: str) -> dict:
    # 这里换成你自己的实现。Replace with a real lookup.
    return {"city": city, "condition": "晴 / sunny", "temperature_c": 22}


messages = [{"role": "user", "content": "杭州现在天气怎么样？适合出门跑步吗？"}]
resp = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
msg = resp.choices[0].message

if msg.tool_calls:
    messages.append({
        "role": "assistant",
        "content": msg.content,
        "tool_calls": [
            {"id": c.id, "type": "function", "function": {"name": c.function.name, "arguments": c.function.arguments}}
            for c in msg.tool_calls
        ],
    })
    for call in msg.tool_calls:
        args = json.loads(call.function.arguments or "{}")
        result = get_weather(**args)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result, ensure_ascii=False)})
    resp = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)

print(resp.choices[0].message.content)
