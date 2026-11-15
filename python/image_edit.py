"""图生图 / 改图：用 OpenAI SDK 的 images.edit 直接上传本地图片（POST /v1/images/edits）。
Edit an image by uploading a local file.

    python image_edit.py original.png

也可以在 /v1/images/generations 里传 image（公网 URL 或 data URI）。gpt-image-2 不读 size，比例写在提示词里。
You can also pass `image` (URL or data URI) to /v1/images/generations.
"""

import os
import sys

from openai import OpenAI

path = sys.argv[1] if len(sys.argv) > 1 else "original.png"
client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"], timeout=300)

with open(path, "rb") as f:
    result = client.images.edit(
        model="gpt-image-2",  # 也可以用 doubao-seedream-5-0-260128、nano-banana-2、qwen-image-3.0 …
        image=f,
        prompt="把沙发改成蓝色，其余保持不变。画面比例 3:2（横构图）",
    )
print(result.data[0].url)  # 临时链接（约 24 小时），请转存。Temporary link: download it.
