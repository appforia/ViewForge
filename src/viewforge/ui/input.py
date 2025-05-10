from typing import Optional, Callable
from viewforge.component import Component
from viewforge.signal import Signal


class TextInput(Component):
    def __init__(
        self,
        name: Optional[str] = None,
        bind: Optional[Signal] = None,
        on_input: Optional[Callable] = None,
        on_change: Optional[Callable] = None,
        css=None
    ):
        self.name = name
        self.bind = bind
        self.on_input = on_input
        self.on_change = on_change
        self.input_handler = getattr(on_input, "_handler_name", "") if callable(on_input) else ""
        self.change_handler = getattr(on_change, "_handler_name", "") if callable(on_change) else ""
        super().__init__(css)

    def render(self):
        name_attr = f'name="{self.name}"' if self.name else ""
        value_attr = f'value="{self.bind()}"' if self.bind else ""
        input_attr = f'oninput="vf(\'{self.input_handler}\', this.value)"' if self.input_handler else ""
        change_attr = f'onchange="vf(\'{self.change_handler}\', this.value)"' if self.change_handler else ""

        return f'<input id="{self._id}" type="text" {name_attr} {value_attr} {input_attr} {change_attr}{self.style_attr()} />'
