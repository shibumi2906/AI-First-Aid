import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma4:e2b"


def call_llm(image_base64: str, user_text: str, system_prompt: str) -> str:
    prompt = f"""{system_prompt}

User request:
{user_text if user_text else "Определи, что изображено на фото, есть ли опасность, и верни ответ строго в JSON."}
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image_base64],
        "stream": False,
    }

    try:
        print("\n===== LLM REQUEST PAYLOAD =====")
        print(f"model: {MODEL_NAME}")
        print(f"prompt preview: {prompt[:1000]}")
        print(f"image attached: yes, base64 length = {len(image_base64)}")
        print("===== END REQUEST PAYLOAD =====\n")

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=180,
        )

        print("\n===== RAW LLM RESPONSE =====")
        print(f"status_code: {response.status_code}")
        print(response.text)
        print("===== END RESPONSE =====\n")

        response.raise_for_status()

        data = response.json()
        return data.get("response", "")

    except Exception as e:
        print("\n!!!!! LLM ERROR !!!!!")
        print(str(e))
        print("!!!!! END ERROR !!!!!\n")
        raise


def analyze_image_with_llm(image_base64: str, user_text: str, system_prompt: str) -> str:
    return call_llm(
        image_base64=image_base64,
        user_text=user_text,
        system_prompt=system_prompt,
    )