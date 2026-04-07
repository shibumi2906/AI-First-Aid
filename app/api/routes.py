import base64
import uuid
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import ValidationError

from app.config import settings
from app.schemas.response import AnalyzeResponse
from app.services.llm_service import analyze_image_with_llm
from app.services.parser import parse_llm_json
from app.services.prompt_loader import load_system_prompt
from app.services.response_builder import build_safe_fallback_response
from app.utils.logger import logger

router = APIRouter()


@router.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    image: UploadFile = File(...),
    text: str | None = Form(default=None),
) -> AnalyzeResponse:
    logger.info("Analyze request received")

    original_name = image.filename or "uploaded_image"
    suffix = Path(original_name).suffix.lower()

    if suffix not in settings.ALLOWED_EXTENSIONS:
        logger.warning(f"Unsupported file type: {suffix}")
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Allowed: jpg, jpeg, png",
        )

    file_bytes = await image.read()

    if not file_bytes:
        logger.warning("Empty uploaded file")
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty",
        )

    if len(file_bytes) > settings.MAX_FILE_SIZE_BYTES:
        logger.warning("Uploaded file exceeds size limit")
        raise HTTPException(
            status_code=400,
            detail="File is too large. Maximum size is 5 MB",
        )

    saved_path = settings.UPLOAD_DIR / f"{uuid.uuid4().hex}{suffix}"

    try:
        with saved_path.open("wb") as destination:
            destination.write(file_bytes)

        image_base64 = base64.b64encode(file_bytes).decode("utf-8")
        user_text = text.strip() if text and text.strip() else ""
        system_prompt = load_system_prompt()

        raw_response = analyze_image_with_llm(
            image_base64=image_base64,
            user_text=user_text,
            system_prompt=system_prompt,
        )

        if not raw_response:
            logger.error("LLM returned empty response")
            return build_safe_fallback_response(
                reason="Model returned empty output"
            )

        parsed_response = parse_llm_json(raw_response)
        validated_response = AnalyzeResponse.model_validate(parsed_response)

        logger.info(f"Analyze request processed successfully: {saved_path.name}")
        return validated_response

    except ValidationError:
        logger.exception("LLM response validation failed")
        return build_safe_fallback_response(
            reason="Model returned invalid structured data"
        )

    except Exception:
        logger.exception("LLM processing failed")
        return build_safe_fallback_response(
            reason="Model failed to produce valid output"
        )

    finally:
        try:
            if saved_path.exists():
                saved_path.unlink()
        except Exception:
            logger.exception(f"Failed to remove temporary file: {saved_path}")