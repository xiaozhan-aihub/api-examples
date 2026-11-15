"""流式输出。Streaming.

网关会在每条流的最后补一个只带 usage、choices 为空的块（计费依据），所以要先判空 choices。
The gateway ends every stream with a chunk that has empty `choices` and only `usage`,
so check `choices` before indexing it.
"""

import os

from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

stream = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "写一首关于秋天的四行短诗。Write a four-line poem about autumn."}],
    stream=True,
)

for chunk in stream:
    if not chunk.choices:
        if chunk.usage:
            print(f"\n\nusage: {chunk.usage.prompt_tokens} in / {chunk.usage.completion_tokens} out")
        continue
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
