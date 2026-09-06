"""List models visible to your FHRouter key."""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://fhrouter.com/v1",
    api_key=os.environ["FHROUTER_API_KEY"],
)

for model in client.models.list().data:
    print(model.id)
