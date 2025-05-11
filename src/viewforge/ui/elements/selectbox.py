from typing import List, Optional, Union, Callable
from viewforge.state.signal import Signal
from viewforge.core.component import Component
from viewforge.core.libtypes import Css
from viewforge.utils.html import escape_html

class SelectBox(Component):
    def __init__(
        self,
        name: Union[str, Signal],
        options: Union[List[str], Signal],
        selected: Optional[Union[str, Signal]] = None,
        on_change: Optional[Callable] = None,
        css: Css = None,
        **props
    ):
        self.name = name
        self.options = options
        self.selected = selected
        self.on_change = on_change

        if isinstance(options, Signal):
            options.subscribe(self.update)
        if isinstance(name, Signal):
            props["name"] = name
        if isinstance(selected, Signal):
            selected.subscribe(self.update)

        if callable(on_change):
            if not hasattr(on_change, "_handler_name"):
                raise ValueError("Handler for 'on_change' must be registered using @handler().")
            props["on_change"] = on_change

        super().__init__(css=css, **props)

    def render(self):
        name_value = self.get_prop("name")
        options_value = self.options() if isinstance(self.options, Signal) else self.options
        selected_value = self.selected() if isinstance(self.selected, Signal) else self.selected

        options_html = "\n".join(
            f'<option value="{escape_html(opt)}"{" selected" if opt == selected_value else ""}>{escape_html(opt)}</option>'
            for opt in options_value
        )

        return f'<select id="{self.id}" name="{name_value}"{self.event_attr()}{self.style_attr()}>{options_html}</select>'
