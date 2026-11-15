"""读开放数据（不需要密钥），列出全部对话模型及其价格。
Read the open data (no key needed) and list the chat models with their prices.

数据：https://model.dflop.top/data/models.json，CC BY 4.0。
Data: https://model.dflop.top/data/models.json, CC BY 4.0.
"""

import json
import urllib.request

URL = "https://model.dflop.top/data/models.json"

with urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "aihub-examples"}), timeout=30) as r:
    data = json.load(r)

print(f"{data['count']} models, updated {data['updated_at']}  ({data['license']['name']})\n")


def cny(m, key):
    v = (m.get("price") or {}).get(key)
    return f"¥{v['cny']:g}" if v else "-"


text = sorted((m for m in data["models"] if m["category"] == "text"), key=lambda m: m["id"])
print(f"{'model':<34}{'context':>10}  {'input/1M':>10}  {'output/1M':>10}")
for m in text:
    ctx = m.get("context_window") or 0
    print(f"{m['id']:<34}{ctx:>10,}  {cny(m, 'input_per_1m_tokens'):>10}  {cny(m, 'output_per_1m_tokens'):>10}")
