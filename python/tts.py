"""语音合成（TTS）：OpenAI SDK 的 audio.speech.create 照官方写法就能用，直接拿到 MP3。
Text to speech with the OpenAI SDK.

voice 填 OpenAI 的音色名（alloy、nova…）会用平台默认音色；要换音色，用 GET /v1/audio/voices 里的音色 id，
或者自己克隆的音色 id。长文案请改用 "async": true 提交 + 轮询（见 curl.md）。
OpenAI voice names map to the platform default; use an id from GET /v1/audio/voices for other voices.
"""

import os

from openai import OpenAI

client = OpenAI(base_url="https://api.dflop.top/v1", api_key=os.environ["PLATFORM_API_KEY"])

speech = client.audio.speech.create(
    model="voice-tts-pro",
    voice="alloy",
    input="你好，欢迎使用小战AIhub 语音合成。Hello and welcome.",
)
speech.write_to_file("hello.mp3")
print("saved hello.mp3")
