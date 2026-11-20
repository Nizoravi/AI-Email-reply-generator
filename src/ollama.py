import json
import urllib.request

def generate_reply(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "qwen2.5:0.5b",
        "prompt": prompt,
        "stream": False
    }

    request_data = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=request_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["response"]