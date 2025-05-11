from typing import Optional, Callable
from viewforge.state.signal import Signal
from viewforge.core.component import Component
from viewforge.core.libtypes import Css
from viewforge.core.app import App

class TextBox(Component):
    def __init__(
        self,
        name: Optional[str] = None,
        bind: Optional[Signal] = None,
        on_input: Optional[Callable] = None,
        on_change: Optional[Callable] = None,
        css: Css = None,
        **props
    ):
        self.name = name
        self.bind = bind
        self.on_input = on_input
        self.on_change = on_change

        if isinstance(bind, Signal):
            bind.subscribe(self.update)

        if isinstance(name, Signal):
            props["name"] = name

        if callable(on_input):
            if not hasattr(on_input, "_handler_name"):
                raise ValueError("Handler for 'on_input' must be registered using @handler().")
            props["on_input"] = on_input

        if callable(on_change):
            if not hasattr(on_change, "_handler_name"):
                raise ValueError("Handler for 'on_change' must be registered using @handler().")
            props["on_change"] = on_change

        super().__init__(css=css, **props)

    def render(self):
        name_value = self.get_prop("name")
        value_value = self.bind() if self.bind else ""
        name_attr = f'name="{name_value}"' if name_value else ""
        value_attr = f'value="{value_value}"'

        return f'<input id="{self.id}" type="text" {name_attr} {value_attr}{self.event_attr()}{self.style_attr()} />'
