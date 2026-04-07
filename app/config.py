from pathlib import Path

from pydantic import BaseModel


class Settings(BaseModel):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    OLLAMA_URL: str = "http://127.0.0.1:11434/api/generate"
    MODEL_NAME: str = "gemma4:e2b"
    REQUEST_TIMEOUT_SECONDS: int = 120
    UPLOAD_DIR: Path = Path("uploads")
    MAX_FILE_SIZE_BYTES: int = 5 * 1024 * 1024
    ALLOWED_EXTENSIONS: tuple[str, ...] = (".jpg", ".jpeg", ".png")


settings = Settings()
settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)