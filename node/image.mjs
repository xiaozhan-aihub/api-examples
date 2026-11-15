// 文生图：OpenAI Node SDK 的 images.generate（POST /v1/images/generations）。
// Text to image with the OpenAI Node SDK.
//
//   node image.mjs

import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.dflop.top/v1",
  apiKey: process.env.PLATFORM_API_KEY,
  timeout: 300_000, // 部分模型一张图要 30 秒到 3 分钟。Some models take up to 3 minutes.
});

const result = await client.images.generate({
  model: "doubao-seedream-5-0-260128", // 或 gpt-image-2、nano-banana-pro、qwen-image-3.0 …
  prompt: "一只在竹林里喝茶的熊猫，水彩风格",
  size: "2048x2048", // Seedream 5.0 的尺寸下限约 1920x1920
});
console.log(result.data[0].url); // 临时链接（约 24 小时），请转存
