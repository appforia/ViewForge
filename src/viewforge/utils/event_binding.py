def js_event_expression(event: str) -> str:
    return {
        "input": "this.value",
        "change": "this.value",
        "click": "null",
        "submit": "null",
        "focus": "null",
        "blur": "null",
        "keydown": "event.key",
        "keyup": "event.key",
        "mouseenter": "null",
        "mouseleave": "null",
    }.get(event, "null")
