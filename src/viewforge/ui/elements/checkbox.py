from typing import Optional, Union, Callable
from viewforge.state.signal import Signal
from viewforge.core.component import Component
from viewforge.core.libtypes import Css
from viewforge.utils.html import escape_html

class Checkbox(Component):
    def __init__(
        self,
        label: str,
        checked: Union[bool, Signal],
        on_change: Optional[Callable] = None,
        disabled: Optional[bool] = False,
        css: Css = None,
        **props
    ):
        self.label = label
        self.disabled = disabled

        # Signal-aware but non-subscribing binding
        if isinstance(checked, Signal):
            self._checked_signal = checked
            self.checked = checked()  # initial value only
        else:
            self._checked_signal = None
            self.checked = checked

        if callable(on_change):
            if not hasattr(on_change, "_handler_name"):
                raise ValueError("Handler for 'on_change' must be registered using @handler().")
            props["on_change"] = on_change

        super().__init__(css=css, **props)

    def render(self):
        is_checked = self._checked_signal() if self._checked_signal else self.checked
        checked_attr = ' checked' if is_checked else ''
        disabled_attr = ' disabled' if self.disabled else ''

        return (
            f'<label id="{self.id}"{self.style_attr()}>'
            f'<input type="checkbox"{checked_attr}{disabled_attr}{self.event_attr(element_type="checkbox")}>'
            f' {escape_html(self.label)}'
            f'</label>'
        )

