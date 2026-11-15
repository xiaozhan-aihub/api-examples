"""用 OpenAI SDK 依次调用几家厂商的模型。
Call models from several vendors with the OpenAI SDK.

    pip install -r requirements.txt
    export PLATFORM_API_KEY=sk-gpushare-...
    python chat.py
"""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.dflop.top/v1",
    api_key=os.environ["PLATFORM_API_KEY"],
)

# 同一个客户端，换个 model 就是另一家的模型。
# Same client; change `model` to switch vendor.
MODELS = ["gpt-6-luna", "claude-sonnet-5", "gemini-3.8-flash", "deepseek-v4.1-flash"]

for model in MODELS:
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "用一句话介绍你自己。Introduce yourself in one sentence."}],
    )
    print(f"[{model}] {resp.choices[0].message.content}\n")
