from typing import Optional


def js_event_expression(event: str, element_type: Optional[str] = None) -> str:
    if element_type == "checkbox":
        return "this.checked"
    if event in {"input", "change"}:
        return "this.value"
    return "event"
