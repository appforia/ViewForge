from typing import Dict, Any
from viewforge.utils.stringcase import snake_to_kebab

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

SHADOW_PRESETS = {
    "none": "none",
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "md": "0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06)",
    "lg": "0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05)",
    "xl": "0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04)",
    "2xl": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
    "inner": "inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)",
}

ROUNDED_PRESETS = {
    "none": "0",
    "sm": "4px",
    "md": "6px",
    "lg": "8px",
    "xl": "12px",
    "2xl": "16px",
    "full": "9999px",
}

COLOR_PRESETS = {
    "primary": "#2563eb",
    "secondary": "#64748b",
    "success": "#16a34a",
    "warning": "#facc15",
    "danger": "#dc2626",
    "neutral": "#e5e7eb",
    "white": "#ffffff",
    "black": "#000000",
}

SPACING_PRESETS = {
    "0": "0px",
    "1": "4px",
    "2": "8px",
    "3": "12px",
    "4": "16px",
    "5": "20px",
    "6": "24px",
    "8": "32px",
    "10": "40px",
    "12": "48px",
    "16": "64px",
    "20": "80px",
}

FONT_SIZE_PRESETS = {
    "xs": "0.75rem",
    "sm": "0.875rem",
    "md": "1rem",
    "lg": "1.125rem",
    "xl": "1.25rem",
    "2xl": "1.5rem",
    "3xl": "1.875rem",
    "4xl": "2.25rem",
    "5xl": "3rem",
}

FONT_WEIGHT_PRESETS = {
    "light": "300",
    "normal": "400",
    "medium": "500",
    "semibold": "600",
    "bold": "700",
    "extrabold": "800",
}

PRESET_KEYS = {
    "rounded": ("border_radius", ROUNDED_PRESETS),
    "shadow": ("box_shadow", SHADOW_PRESETS),
    "font_size": ("font_size", FONT_SIZE_PRESETS),
}

def coerce_unit(value):
    if isinstance(value, (int, float)):
        return f"{value}px"
    return value


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


def merge_styles(*dicts):
    merged = {}
    for d in dicts:
        if d:
            merged.update(d)
    return "; ".join(f"{snake_to_kebab(k)}: {v}" for k, v in merged.items())
