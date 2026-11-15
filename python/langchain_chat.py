"""LangChain：ChatOpenAI 指向网关，model 填任意对话模型的调用 ID。
LangChain's ChatOpenAI pointed at the gateway.

    pip install langchain-openai
"""

import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-v4.1-flash",  # 或 gpt-6-luna、claude-sonnet-5、gemini-3.8-flash、kimi-k3 …
    base_url="https://api.dflop.top/v1",
    api_key=os.environ["PLATFORM_API_KEY"],
)

print(llm.invoke("用一句话解释什么是 RAG。Explain RAG in one sentence.").content)

for chunk in llm.stream("写一句关于春天的话。Write one line about spring."):
    print(chunk.content, end="", flush=True)
print()
