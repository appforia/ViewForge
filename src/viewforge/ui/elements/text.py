from typing import Optional
from viewforge.state.signal import Signal
from viewforge.core.component import Component
from viewforge.core.libtypes import TextSize, FontWeight, StyleProps, Tag, Align, Css, ContentLike
from viewforge.utils.css import resolve_preset
from viewforge.ui.layout.presets import FONT_SIZE_PRESETS, FONT_WEIGHT_PRESETS


class Text(Component):
    def __init__(
            self,
            content: ContentLike,
            *,
            tag: Tag = "div",
            size: Optional[TextSize] = None,
            weight: Optional[FontWeight] = None,
            color: Optional[str] = None,
            align: Optional[Align] = None,
            css: Css = None,
            **props: StyleProps
    ):
        if callable(content) and not isinstance(content, Signal):
            raise TypeError("Text content must be a string or Signal, not a function")

        self._content = content
        self.tag = tag

        if isinstance(content, Signal):
            content.subscribe(self.update)

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
        value = self._content() if isinstance(self._content, Signal) else self._content
        return f'<{self.tag} id="{self.id}"{self.style_attr()}>{value}</{self.tag}>'
