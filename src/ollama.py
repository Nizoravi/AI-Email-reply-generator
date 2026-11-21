import json
import urllib.request
import urllib.error


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

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))

        if "response" not in result:
            raise RuntimeError("Unexpected response received from Ollama.")

        return result["response"]

    except urllib.error.HTTPError as error:
        raise RuntimeError(
            f"Ollama API error: HTTP {error.code}"
        ) from error

    except urllib.error.URLError as error:
        raise RuntimeError(
            "Cannot connect to Ollama. Make sure Ollama is running."
        ) from error

    except TimeoutError as error:
        raise RuntimeError(
            "The request timed out. Please try again."
        ) from error

    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise RuntimeError(
            "Could not process the response from Ollama."
        ) from error