"""图生视频：把一张图当首帧，让它动起来（Seedance 2.0）。
Image to video: animate a first-frame picture.

    python video_image_to_video.py first-frame.jpg
    python video_image_to_video.py https://your-cdn.com/first-frame.jpg

本地图片会转成 data URI（单张 ≤ 30 MB）；也可以直接给公网 URL。
A local file is sent as a data URI (up to 30 MB); a public URL also works.
"""

import base64
import mimetypes
import os
import sys
import time
import uuid

import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

src = sys.argv[1] if len(sys.argv) > 1 else "first-frame.jpg"
if src.startswith(("http://", "https://")):
    image_url = src
else:
    mime = mimetypes.guess_type(src)[0] or "image/jpeg"
    with open(src, "rb") as f:
        image_url = f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"

r = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},
    json={
        "model": "doubao-seedance-2.0",
        "content": [
            {"type": "text", "text": "画面中的人物转身望向远方，镜头缓慢推进"},
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
        "duration": 5,
        "resolution": "720p",
    },
    timeout=120,
)
r.raise_for_status()
task = r.json()
print("task:", task["id"])

while task["status"] not in ("succeeded", "failed", "expired", "cancelled"):
    time.sleep(10)
    task = requests.get(f"{BASE}/videos/generations/{task['id']}", headers=HEADERS, timeout=30).json()
    print("status:", task["status"])

print(task.get("video_url") or task.get("error"))  # 7 天有效，请转存
