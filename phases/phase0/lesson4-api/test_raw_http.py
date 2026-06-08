import os
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv()

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['DEEPSEEK_API_KEY']}",
}
body = json.dumps({
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    "max_tokens": 256,
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    # Print full response for comparison
    print("=== Full response ===")
    print(json.dumps(result, indent=2))
    print("\n=== Just the text ===")
    print(result["choices"][0]["message"]["content"])
