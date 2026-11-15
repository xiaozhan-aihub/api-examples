"""GIF 动图：gpt-image-2.6-flare / gpt-image-2.6-sunburst 把 output_format 设成 gif。
Animated GIF from GPT-Image 2.6.

size 是每一帧的尺寸（宽高都要是 16 的倍数）；frame_count 2–16，frame_duration_ms 20–2000。
`size` is per frame; frame_count 2-16; frame_duration_ms 20-2000.
"""

import os

import requests

r = requests.post(
    "https://api.dflop.top/v1/images/generations",
    headers={"Authorization": f"Bearer {os.environ['PLATFORM_API_KEY']}"},
    json={
        "model": "gpt-image-2.6-flare",
        "prompt": "一只卡通小猫抬起爪子挥手打招呼，动作循环，纯色浅黄背景",
        "output_format": "gif",
        "size": "512x512",
        "frame_count": 9,
        "frame_duration_ms": 200,
    },
    timeout=300,
)
r.raise_for_status()
print(r.json()["data"][0]["url"])  # 无限循环的 .gif，临时链接，请转存
