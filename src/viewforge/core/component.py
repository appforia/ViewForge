import uuid
from typing import Any, Optional
from viewforge.core.libtypes import Css
from viewforge.state.signal import Signal
from viewforge.utils.event_binding import js_event_expression


class Component:
    def __init__(self, css: Css = None, **props):
        self._id = f"vf-{uuid.uuid4().hex[:8]}"
        self._style = {}
        self._signal_bindings: dict[str, Signal] = {}
        self._event_handlers: dict[str, str] = {}
        self.css = css or {}

        for key, value in props.items():
            if key.startswith("on_"):
                if isinstance(value, Signal):
                    print(f"[Warning] Ignoring signal bound to event: {key}")
                    continue
                if callable(value) and not hasattr(value, "_handler_name"):
                    raise ValueError(
                        f"[Error] Handler for '{key}' must be registered using @handler(). Lambdas are not allowed.")
                if callable(value):
                    handler_name = getattr(value, "_handler_name", None)
                    if handler_name:
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
        style = self._style.copy()
        for key, sig in self._signal_bindings.items():
            if key in self._style or key not in self.__dict__:
                style[key] = sig()
        if not style:
            return ""
        css_str = "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in style.items())
        return f' style="{css_str}"'

    def event_attr(self, element_type: Optional[str] = None) -> str:
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

    def get_prop(self, key: str) -> Any:
        if key in self._signal_bindings:
            return self._signal_bindings[key]()
        return getattr(self, key, None)

    def render(self) -> str:
        raise NotImplementedError("Subclasses must implement render()")

    def update(self, _=None):
        from viewforge.core.app import App  # ✅ lazy import to avoid circular reference
        html = self.render().replace("`", "\\`")
        js = f'document.getElementById("{self.id}").outerHTML = `{html}`'
        App.current().window.evaluate_js(js)
