"""文生视频：提交任务，再轮询结果。
Text to video: submit a task, then poll it.

Idempotency-Key：同一个提交意图用同一把键，重发多少次都只开一个任务、只扣一次费，
忘了任务 id 时把原请求原样再发一次就能拿回来（键保留 7 天）。
Idempotency-Key: reuse one key per submission; retries return the first response
(same task id) and are never charged twice. Kept for 7 days.
"""

import os
import time
import uuid

import requests

BASE = "https://api.dflop.top/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"}

submit = requests.post(
    f"{BASE}/videos/generations",
    headers={**HEADERS, "Idempotency-Key": str(uuid.uuid4())},
    json={
        "model": "doubao-seedance-2.0",
        "content": [{"type": "text", "text": "海边日落，无人机航拍视角。Sunset over the sea, drone shot."}],
        "duration": 5,
        "resolution": "720p",
        "ratio": "16:9",
    },
    timeout=60,
)
submit.raise_for_status()
task_id = submit.json()["id"]
print("task:", task_id)

# 一般 1–5 分钟。Usually 1-5 minutes.
while True:
    task = requests.get(f"{BASE}/videos/generations/{task_id}", headers=HEADERS, timeout=30).json()
    if task["status"] in ("succeeded", "failed", "expired", "cancelled"):
        break
    print("status:", task["status"], task.get("progress", ""))
    time.sleep(10)

if task["status"] == "succeeded":
    print("video:", task["video_url"])  # 临时链接，请转存。Temporary link: download it.
else:
    print("failed:", task.get("error"))
