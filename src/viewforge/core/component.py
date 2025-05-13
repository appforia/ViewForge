import uuid
from typing import Any, Optional
from viewforge.core.libtypes import Css
from viewforge.state.signal import Signal
from viewforge.core.event_binding import js_event_expression


def to_css(style: dict[str, Any]) -> str:
    """Converts a dict of style properties into CSS inline style string."""
    return "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in style.items())


class Component:
    __slots__ = (
        "_id",
        "_style",
        "_signal_bindings",
        "_event_handlers",
        "css",
    )

    def __init__(self, css: Css = None, **props):
        self._id = f"vf-{uuid.uuid4().hex[:8]}"
        self._style = {}
        self._signal_bindings: dict[str, Signal] = {}
        self._event_handlers: dict[str, str] = {}
        self.css = css or {}

        for key, value in props.items():
            if key.startswith("on_"):
                if isinstance(value, Signal):
                    raise ValueError(f"[Error] Signal cannot be used as an event handler: '{key}'")

                if not callable(value):
                    raise ValueError(f"[Error] Event handler for '{key}' must be a function, got: {type(value)}")

                if not hasattr(value, "_handler_name"):
                    raise ValueError(
                        f"[Error] Handler for '{key}' must be registered using @handler(). "
                        f"Lambdas or unregistered functions are not allowed.\n→ Received: {value}"
                    )

                handler_name = getattr(value, "_handler_name", None)
                if not handler_name:
                    raise ValueError(f"[Error] Failed to retrieve handler name for '{key}'")

                dom_event = key[3:]  # 'on_click' → 'click'
                self._event_handlers[dom_event] = handler_name
                continue

            if isinstance(value, Signal):
                self._signal_bindings[key] = value
                value.subscribe(self.update)
            else:
                self._style[key] = value

    @property
    def id(self):
        return self._id

    def style_attr(self) -> str:
        """Returns a string like: style="color: red; margin: 8px"."""
        style = self._style.copy()
        for key, sig in self._signal_bindings.items():
            style[key] = sig()
        if not style:
            return ""
        return f' style="{to_css(style)}"'

    def event_attr(self, element_type: Optional[str] = None) -> str:
        """Returns DOM event bindings like: oninput="vf('handler', this.value)"."""
        if not self._event_handlers:
            return ""
        parts = []
        for event, handler in self._event_handlers.items():
            arg = js_event_expression(event, element_type)
            if arg:
                parts.append(f'on{event}="vf(\'{handler}\', {arg})"')
            else:
                parts.append(f'on{event}="vf(\'{handler}\')"')
        return " " + " ".join(parts)

    def attributes(self, element_type: Optional[str] = None) -> str:
        """Returns combined style and event attributes."""
        return f'{self.style_attr()}{self.event_attr(element_type)}'

    def get_prop(self, key: str) -> Any:
        """Returns a signal-bound value or fallback attribute."""
        if key in self._signal_bindings:
            return self._signal_bindings[key]()
        return getattr(self, key, None)

    def render(self) -> str:
        raise NotImplementedError("Subclasses must implement render()")

    def update(self, _=None):
        """Triggers re-rendering of this component via JS DOM patching."""
        try:
            from viewforge.core.app import App
            app = App.current()
            if app and app.window:
                html = self.render()
                js = f'vf_update("{self.id}", `{html}`)'  # ✅ patched
                app.evaluate_js(js)
        except Exception as e:
            print(f"[Component.update] Failed to update {self.id}: {e}")
