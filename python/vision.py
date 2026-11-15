"""识图：把本地图片作为 data URI 发给模型（OpenAI 的 image_url 写法）。
Image input: send a local picture as a data URI.

    python vision.py photo.jpg

支持读图的模型（模型广场「读图」标记）都可以，例如 gpt-6-luna、claude-sonnet-5、gemini-3.8-flash、qwen3.8-omni-flash、glm-5.3-flash。
Any vision model works, e.g. gpt-6-luna, claude-sonnet-5, gemini-3.8-flash.
"""

import base64
import mimetypes
import os
import sys

from openai import OpenAI

path = sys.argv[1] if len(sys.argv) > 1 else "photo.jpg"
mime = mimetypes.guess_type(path)[0] or "image/jpeg"
with open(path, "rb") as f:
    data_uri = f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

resp = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "这张图里有什么？用三句话描述。Describe this picture in three sentences."},
            {"type": "image_url", "image_url": {"url": data_uri}},
        ],
    }],
)
print(resp.choices[0].message.content)
