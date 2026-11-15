"""文生图：POST /v1/images/generations（OpenAI Images 形状）。
Text to image with the OpenAI SDK.

gpt-image-2 一张图常要 30 秒到 3 分钟，客户端超时请设 300 秒以上。
返回的图片链接是临时的（约 24 小时），拿到后请转存。
gpt-image-2 can take 30 s to 3 min per image: keep the client timeout at 300 s or more.
Image URLs are temporary (about 24 hours); download them.
"""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.dflop.top/v1",
    api_key=os.environ["PLATFORM_API_KEY"],
    timeout=300,
)

result = client.images.generate(
    model="gpt-image-2",
    # gpt-image-2 不读 size，画面比例写进提示词。gpt-image-2 ignores `size`: put the aspect ratio in the prompt.
    prompt="一只在竹林里喝茶的熊猫，水彩风格，画面比例 1:1",
)
print(result.data[0].url)
