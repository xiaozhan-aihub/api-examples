"""AI 音乐（Suno V6）：一句话描述生成歌曲，一次出 2 首完整歌曲（含歌词与封面）。
Suno V6 music: one prompt, two full songs with lyrics and cover art.

自定义歌词传 lyrics，曲风传 tags（如 "synthwave, female vocal"），纯音乐传 instrumental=True。
Pass `lyrics` for your own words, `tags` for the style, `instrumental: true` for no vocals.
"""

import os
import time
import uuid

import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

r = requests.post(
    f"{BASE}/music/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},
    json={"model": "suno-v6", "prompt": "一首关于夏天海边散步的轻快中文流行歌"},
    timeout=60,
)
r.raise_for_status()
task = r.json()
print("task:", task["id"])

# 一般 2–4 分钟。Usually 2-4 minutes.
while task["status"] not in ("succeeded", "failed", "expired", "cancelled"):
    time.sleep(15)
    task = requests.get(f"{BASE}/music/generations/{task['id']}", headers=HEADERS, timeout=30).json()
    print("status:", task["status"])

for track in task.get("tracks", []):
    print(track["title"], track["audio_url"])  # 长期有效的链接
