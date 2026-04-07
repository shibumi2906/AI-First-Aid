import json
import re


def parse_llm_json(raw: str) -> dict:
    print("\n===== PARSER INPUT =====")
    print(raw)
    print("===== END PARSER INPUT =====\n")

    try:
        # пробуем как есть
        return json.loads(raw)
    except:
        pass

    try:
        # вытаскиваем JSON из текста
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass

    print("\n!!!!! PARSER FAILED !!!!!\n")
    return {}