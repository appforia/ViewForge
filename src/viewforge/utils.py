import re
import uuid
import html
import json


def camel_to_kebab(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def merge_styles(*dicts):
    merged = {}
    for d in dicts:
        if d:
            merged.update(d)
    return "; ".join(f"{k}: {v}" for k, v in merged.items())


def escape_html(text: str) -> str:
    return html.escape(text)


def js_func(name: str, *args):
    arg_str = ", ".join(json.dumps(arg) for arg in args)
    return f"{name}({arg_str})"


def generate_id(prefix="el"):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


def snake_to_camel(name: str) -> str:
    parts = name.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])


def camel_to_snake(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
