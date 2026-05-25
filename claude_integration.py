import json
import os
import urllib.request

API_URL = "https://api.anthropic.com/v1/complete"
API_KEY_ENV = "ANTHROPIC_API_KEY"


class ClaudeIntegrationError(Exception):
    pass


def get_api_key() -> str:
    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        raise ClaudeIntegrationError(
            f"Environment variable {API_KEY_ENV} is not set."
        )
    return api_key


def generate_claude_response(prompt: str, model: str = "claude-3.5", max_tokens: int = 400) -> str:
    api_key = get_api_key()
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens_to_sample": max_tokens,
        "temperature": 0.3,
    }
    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "X-API-Key": api_key,
        },
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
    result = json.loads(body)
    return result.get("completion", "")


if __name__ == "__main__":
    demo_prompt = (
        "Write a short developer-facing summary of the difference between "
        "Claude and ChatGPT, focusing on code workflow.")
    try:
        answer = generate_claude_response(demo_prompt)
        print("=== Claude response ===")
        print(answer)
    except ClaudeIntegrationError as exc:
        print(f"ERROR: {exc}")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8")
        print(f"HTTP ERROR: {exc.code} - {error_body}")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
