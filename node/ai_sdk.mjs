// Vercel AI SDK：用 @ai-sdk/openai-compatible 接网关，model 填任意对话模型的调用 ID。
// The Vercel AI SDK through the OpenAI-compatible provider.
//
//   npm install
//   node ai_sdk.mjs

import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { generateText, streamText } from "ai";

const aihub = createOpenAICompatible({
  name: "aihub",
  baseURL: "https://api.dflop.top/v1",
  apiKey: process.env.PLATFORM_API_KEY,
});

const { text } = await generateText({
  model: aihub("gpt-6-luna"),
  prompt: "用一句话介绍向量数据库。Explain vector databases in one sentence.",
});
console.log(text);

const result = streamText({
  model: aihub("claude-sonnet-5"),
  prompt: "写一首关于秋天的四行短诗。Write a four-line poem about autumn.",
});
for await (const part of result.textStream) process.stdout.write(part);
console.log();
