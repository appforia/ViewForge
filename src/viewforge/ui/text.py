from typing import Optional
from viewforge.libtypes import TextSize, FontWeight, StyleProps, Tag, Align, Css
from viewforge.component import Component
from viewforge.utils import resolve_preset
from viewforge.ui.presets import FONT_SIZE_PRESETS, FONT_WEIGHT_PRESETS


class Text(Component):
    def __init__(
            self,
            content: str,
            *,
            tag: Tag = "div",
            size: Optional[TextSize] = None,
            weight: Optional[FontWeight] = None,
            color: Optional[str] = None,
            align: Optional[Align] = None,
            css: Css = None,
            **props: StyleProps
    ):
        self.content = content
        self.tag = tag

        resolved_props = {}
        if size:
            resolved_props["font_size"] = resolve_preset(size, FONT_SIZE_PRESETS)
        if weight:
            resolved_props["font_weight"] = resolve_preset(weight, FONT_WEIGHT_PRESETS)
        if color:
            resolved_props["color"] = color
        if align:
            resolved_props["text_align"] = align

        super().__init__(default_style={}, css=css, **resolved_props, **props)

    def render(self):
        return f'<{self.tag}{self.style_attr()}>{self.content}</{self.tag}>'
