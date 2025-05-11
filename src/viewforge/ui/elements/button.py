from typing import Callable, Optional, Union
from viewforge.state.signal import Signal
from viewforge.core.component import Component
from viewforge.core.libtypes import Css, StyleProps


class Button(Component):
    def __init__(
            self,
            label: Union[str, Signal],
            on_click: Optional[Callable] = None,
            *,
            css: Css = None,
            **props: StyleProps
    ):
        self.label = label
        if callable(on_click):
            props["on_click"] = on_click  # generic event handler

        if isinstance(label, Signal):
            label.subscribe(self.update)

        super().__init__(css=css, **props)

    def render(self) -> str:
        content = self.label() if isinstance(self.label, Signal) else self.label
        return f'<button id="{self.id}"{self.event_attr(element_type="button")}{self.style_attr()}>{content}</button>'

