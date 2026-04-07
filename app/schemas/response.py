from typing import Literal

from pydantic import BaseModel, Field


ScenarioType = Literal["electrical_panel", "generic_electrical"]
ConfidenceType = Literal["low", "medium", "high"]


class AnalyzeResponse(BaseModel):
    scenario: ScenarioType
    what_is_this: str = Field(..., min_length=1)
    what_you_see: list[str] = Field(..., min_length=1)
    problem_detected: bool
    problem_description: str = Field(..., min_length=1)
    safe_actions: list[str] = Field(..., min_length=1)
    stop_conditions: list[str] = Field(..., min_length=1)
    confidence: ConfidenceType