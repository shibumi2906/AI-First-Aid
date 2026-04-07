from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    image: str = Field(..., min_length=1, description="Base64 encoded image")
    text: str | None = Field(default=None, description="Optional user text")
