from pathlib import Path


def load_system_prompt() -> str:
    # путь к текущему файлу
    current_file = Path(__file__).resolve()

    # идём вверх до app/
    app_dir = current_file.parent.parent

    # формируем путь к prompts/system.txt
    prompt_path = app_dir / "prompts" / "system.txt"

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")