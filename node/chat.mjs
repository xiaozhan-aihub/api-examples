// OpenAI Node SDK：普通调用 + 流式。Plain call and streaming with the OpenAI Node SDK.
//
//   npm install
//   export PLATFORM_API_KEY=sk-gpushare-...
//   node chat.mjs

import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.dflop.top/v1",
  apiKey: process.env.PLATFORM_API_KEY,
});

const resp = await client.chat.completions.create({
  model: "gpt-6-luna",
  messages: [{ role: "user", content: "用一句话介绍你自己。Introduce yourself in one sentence." }],
});
console.log(resp.choices[0].message.content);

// 流式：最后一个块只带 usage，choices 为空，用 ?. 就不会出错。
// Streaming: the last chunk carries only `usage` with empty `choices`; `?.` keeps this safe.
const stream = await client.chat.completions.create({
  model: "claude-sonnet-5",
  messages: [{ role: "user", content: "写一首关于秋天的四行短诗。Write a four-line poem about autumn." }],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
console.log();
