from typing import List, Optional, Callable
from viewforge.component import Component


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
