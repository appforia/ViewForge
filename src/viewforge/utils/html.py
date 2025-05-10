import html
import uuid


def escape_html(text: str) -> str:
    return html.escape(text)


def generate_id(prefix="el"):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"
