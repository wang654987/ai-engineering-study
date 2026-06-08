import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url=os.environ["DEEPSEEK_BASE_URL"],
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
    max_tokens=256,
)

print(response.choices[0].message.content)
