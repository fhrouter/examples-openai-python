"""Stream a response token-by-token from a free model."""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://fhrouter.com/v1",
    api_key=os.environ["FHROUTER_API_KEY"],
)

stream = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Write a haiku about APIs"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
