from typing import List, Optional, Callable
from viewforge.component import Component
from viewforge.router import router


class Checkbox(Component):
    def __init__(self, label: str, name: str, on_change: Optional[Callable] = None, checked: bool = False, css=None):
        self.label = label
        self.name = name
        self.checked = checked
        self.handler_name = getattr(on_change, "_handler_name", "") if callable(on_change) else ""
        super().__init__(css)

    def render(self):
        checked_attr = "checked" if self.checked else ""
        handler_attr = f'onchange="{self.handler_name}(this.checked)"' if self.handler_name else ""
        return (
            f'<label{self.style_attr()}><input type="checkbox" name="{self.name}" {checked_attr} {handler_attr} /> '
            f'{self.label}</label>'
        )


class Form(Component):
    def __init__(self, children: List[Component], on_submit: Optional[Callable] = None, css=None):
        self.children = children
        self.handler_name = getattr(on_submit, "_handler_name", "") if callable(on_submit) else ""
        super().__init__(css or {"display": "flex", "flex_direction": "column", "gap": "1rem"})

    def render(self):
        submit_js = (
            f"event.preventDefault(); const form = event.target;"
            f" const data = Object.fromEntries(new FormData(form).entries());"
            f" window.pywebview.api.{self.handler_name}(data);"
        ) if self.handler_name else ""

        inner_html = "\n".join(c.render() for c in self.children)
        return f'<form onsubmit="{submit_js}"{self.style_attr()}>{inner_html}</form>'


class FormGroup(Component):
    def __init__(self, children: List[Component], css=None):
        self.children = children
        super().__init__(css or {"display": "flex", "flex_direction": "column", "gap": "0.5rem"})

    def render(self):
        inner = "\n".join(child.render() for child in self.children)
        return f'<fieldset{self.style_attr()}>{inner}</fieldset>'


class RouteLinkButton(Component):
    def __init__(self, label: str, to: str, css=None):
        self.label = label
        self.to = to
        self.handler_name = f"goto_{label.lower().replace(' ', '_')}"
        super().__init__(css)

    def _navigate(self):
        if router():
            router().navigate(self.to)
            from viewforge.app import App
            app = App.current()
            if app:
                app.reload()

    def render(self):
        return f'<button onclick="{self.handler_name}()"{self.style_attr()}>{self.label}</button>'
