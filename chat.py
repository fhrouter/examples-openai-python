"""Chat with a free frontier model on FHRouter (OpenAI SDK)."""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://fhrouter.com/v1",
    api_key=os.environ["FHROUTER_API_KEY"],
)

response = client.chat.completions.create(
    model="grok-4.6",  # free; also: deepseek-v4-flash, glm-5.3-flash
    messages=[{"role": "user", "content": "Hello, world"}],
)
print(response.choices[0].message.content)
