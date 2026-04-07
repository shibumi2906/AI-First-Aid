from app.schemas.response import AnalyzeResponse


def build_safe_fallback_response(reason: str | None = None) -> AnalyzeResponse:
    problem_description = (
        reason.strip()
        if reason and reason.strip()
        else "The system is not confident enough to identify the object safely"
    )

    return AnalyzeResponse(
        scenario="generic_electrical",
        what_is_this="Electrical equipment",
        what_you_see=["The image could not be analyzed reliably"],
        problem_detected=False,
        problem_description=problem_description,
        safe_actions=[
            "Do not touch wires",
            "Call an electrician",
        ],
        stop_conditions=[
            "If you see damage",
            "If there is smoke or smell",
            "If you are not sure",
        ],
        confidence="low",
    )