// 文生视频：提交任务，再轮询结果（POST /v1/videos/generations）。
// Text to video: submit a task, then poll it.
//
//   node video.mjs

import { randomUUID } from "node:crypto";

const BASE = "https://api.dflop.top/v1";
const headers = {
  Authorization: `Bearer ${process.env.PLATFORM_API_KEY}`,
  "Content-Type": "application/json",
};

const submit = await fetch(`${BASE}/videos/generations`, {
  method: "POST",
  // 同一个提交意图用同一把 Idempotency-Key，重试不会重复扣费。Retries with the same key are never charged twice.
  headers: { ...headers, "Idempotency-Key": randomUUID() },
  body: JSON.stringify({
    model: "tvod-kling-video-3.0", // 或 doubao-seedance-2.0、tvod-veo-3.1-fast、minimax-h3、wan3.0-video …
    content: [{ type: "text", text: "海边日落，无人机航拍视角" }],
    duration: 5,
    resolution: "720p",
    ratio: "16:9",
  }),
});
if (!submit.ok) throw new Error(`${submit.status} ${await submit.text()}`);
let task = await submit.json();
console.log("task:", task.id);

while (!["succeeded", "failed", "expired", "cancelled"].includes(task.status)) {
  await new Promise((r) => setTimeout(r, 10_000));
  task = await (await fetch(`${BASE}/videos/generations/${task.id}`, { headers })).json();
  console.log("status:", task.status);
}
console.log(task.video_url ?? task.error); // 7 天有效，请转存
