from typing import Callable, Optional
from viewforge.component import Component
from viewforge.libtypes import Css, StyleProps

class Button(Component):
    def __init__(
        self,
        label: str,
        on_click: Optional[Callable] = None,
        *,
        css: Css = None,
        **props: StyleProps
    ):
        self.label = label
        self.onclick_name = getattr(on_click, "_handler_name", "") if callable(on_click) else ""
        super().__init__(default_style={}, css=css, **props)

    def render(self) -> str:
        onclick_attr = f' onclick="vf(\'{self.onclick_name}\')"' if self.onclick_name else ""
        return f'<button{onclick_attr}{self.style_attr()}>{self.label}</button>'
