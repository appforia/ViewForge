import re
import uuid
import html
import json
from typing import Dict, Any

from viewforge.ui.presets import ROUNDED_PRESETS, SHADOW_PRESETS, FONT_SIZE_PRESETS, SPACING_PRESETS

PRESET_KEYS = {
    "rounded": ("border_radius", ROUNDED_PRESETS),
    "shadow": ("box_shadow", SHADOW_PRESETS),
    "font_size": ("font_size", FONT_SIZE_PRESETS),
}

SPACING_KEYS = {
    "padding", "padding_top", "padding_bottom", "padding_left", "padding_right",
    "margin", "margin_top", "margin_bottom", "margin_left", "margin_right",
}

SHORTHAND_MAP = {
    "padding_x": ["padding_left", "padding_right"],
    "padding_y": ["padding_top", "padding_bottom"],
    "margin_x": ["margin_left", "margin_right"],
    "margin_y": ["margin_top", "margin_bottom"],
}


def camel_to_kebab(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def merge_styles(*dicts):
    merged = {}
    for d in dicts:
        if d:
            merged.update(d)
    return "; ".join(f"{snake_to_kebab(k)}: {v}" for k, v in merged.items())


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


def coerce_unit(value):
    if isinstance(value, (int, float)):
        return f"{value}px"
    return value


def snake_to_kebab(name: str) -> str:
    return name.replace("_", "-")


def resolve_preset(value, presets: dict) -> str:
    """
    Resolves a value using a preset mapping dictionary.

    If the value exists as a key in the preset dictionary, returns the mapped value.
    Otherwise, returns the original value.
    """
    if isinstance(value, str) and value in presets:
        return presets[value]
    return value


def apply_style_props(*styles: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges and normalizes multiple style dictionaries into a single CSS-ready style dict.

    Behavior:
    - Merges all provided dictionaries in order (later ones override earlier ones).
    - Resolves known style presets for specific properties:
        - 'rounded' → 'border_radius' via ROUNDED_PRESETS
        - 'shadow' → 'box_shadow' via SHADOW_PRESETS
        - 'font_size' → 'font_size' via FONT_SIZE_PRESETS
    - Expands shorthand spacing props:
        - 'padding_x' → 'padding_left' and 'padding_right'
        - 'padding_y' → 'padding_top' and 'padding_bottom'
        - 'margin_x' → 'margin_left' and 'margin_right'
        - 'margin_y' → 'margin_top' and 'margin_bottom'
    - Coerces all numeric values to CSS units (e.g., 16 → "16px").

    Parameters:
        *styles: Arbitrary style dictionaries to merge and normalize.

    Returns:
        A single dictionary with kebab-case-compatible CSS property names and unit-coerced values.
    """
    merged = {}
    for style in styles:
        if style:
            merged.update(style)

    result = {}
    for key, val in merged.items():
        if key in SHORTHAND_MAP:
            for expanded_key in SHORTHAND_MAP[key]:
                result[expanded_key] = coerce_unit(val)
        elif key in PRESET_KEYS:
            css_key, preset_map = PRESET_KEYS[key]
            result[css_key] = coerce_unit(resolve_preset(val, preset_map))
        else:
            result[key] = coerce_unit(val)

    return result
