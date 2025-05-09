from typing import List, Optional, Callable
from viewforge.component import Component
from viewforge.signal import Signal
from viewforge.bridge import register_handler
from viewforge.router import router


class Text(Component):
    def __init__(self, content: str, style=None):
        self.content = content
        super().__init__(style)

    def render(self):
        return f'<div{self.style_attr()}>{self.content}</div>'


class TextInput(Component):
    def __init__(self, name: Optional[str] = None, bind: Optional[Signal] = None, on_input: Optional[Callable] = None,
                 style=None):
        self.name = name
        self.bind = bind
        self.on_input = on_input
        self.handler_name = ""
        super().__init__(style)

        if callable(on_input) or bind:
            def combined_handler(value):
                if bind:
                    bind.set(value)
                if on_input:
                    on_input(value)

            self.handler_name = register_handler(f"on_input_{name or id(self)}", combined_handler)

    def render(self):
        handler_attr = f'oninput="{self.handler_name}(this.value)"' if self.handler_name else ""
        name_attr = f'name="{self.name}"' if self.name else ""
        value_attr = f'value="{self.bind()}"' if self.bind else ""
        return f'<input type="text" {name_attr} {value_attr} {handler_attr}{self.style_attr()} />'


class Button(Component):
    def __init__(self, label: str, onclick: Callable = None, style=None):
        super().__init__(style)
        self.label = label
        self.onclick = onclick
        self.onclick_name = ""

        if callable(onclick):
            self.onclick_name = register_handler(f"on_{label.lower().replace(' ', '_')}", onclick)

    def render(self) -> str:
        onclick_attr = f'onclick="{self.onclick_name}()"' if self.onclick_name else ""
        return f'<button {onclick_attr}{self.style_attr()}>{self.label}</button>'


class Stack(Component):
    def __init__(self, children: List[Component], gap: str = "1rem", style=None):
        self.children = children
        base_style = {"display": "flex", "flexDirection": "column", "gap": gap}
        if style:
            base_style.update(style)
        super().__init__(base_style)

    def render(self):
        inner = "\n".join(c.render() for c in self.children)
        return f'<div{self.style_attr()}>{inner}</div>'


class SelectBox(Component):
    def __init__(self, name: str, options: List[str], on_change: Optional[Callable] = None, style=None):
        self.name = name
        self.options = options
        self.on_change = on_change
        self.handler_name = ""
        super().__init__(style)

        if callable(on_change):
            self.handler_name = register_handler(f"on_select_{name}", on_change)

    def render(self):
        handler_attr = f'onchange="{self.handler_name}(this.value)"' if self.handler_name else ""
        options_html = "\n".join(f'<option value="{opt}">{opt}</option>' for opt in self.options)
        return f'<select name="{self.name}" {handler_attr}{self.style_attr()}>{options_html}</select>'


class Checkbox(Component):
    def __init__(self, label: str, name: str, on_change: Optional[Callable] = None, checked: bool = False, style=None):
        self.label = label
        self.name = name
        self.checked = checked
        self.handler_name = ""
        self.on_change = on_change
        super().__init__(style)

        if callable(on_change):
            self.handler_name = register_handler(f"on_check_{name}", on_change)

    def render(self):
        checked_attr = "checked" if self.checked else ""
        handler_attr = f'onchange="{self.handler_name}(this.checked)"' if self.handler_name else ""
        return (
            f'<label{self.style_attr()}><input type="checkbox" name="{self.name}" {checked_attr} {handler_attr} /> '
            f'{self.label}</label>'
        )


class Form(Component):
    def __init__(self, children: List[Component], on_submit: Optional[Callable] = None, style=None):
        self.children = children
        self.handler_name = ""
        if callable(on_submit):
            self.handler_name = register_handler("on_form_submit", on_submit)
        super().__init__(style or {"display": "flex", "flexDirection": "column", "gap": "1rem"})

    def render(self):
        submit_js = (
            f"event.preventDefault(); const form = event.target;"
            f" const data = Object.fromEntries(new FormData(form).entries());"
            f" window.pywebview.api.{self.handler_name}(data);"
        ) if self.handler_name else ""

        inner_html = "\n".join(c.render() for c in self.children)
        return f'<form onsubmit="{submit_js}"{self.style_attr()}>{inner_html}</form>'


class FormGroup(Component):
    def __init__(self, children: List[Component], style=None):
        self.children = children
        super().__init__(style or {"display": "flex", "flexDirection": "column", "gap": "0.5rem"})

    def render(self):
        inner = "\n".join(child.render() for child in self.children)
        return f'<fieldset{self.style_attr()}>{inner}</fieldset>'


class RouteLinkButton(Component):
    def __init__(self, label: str, to: str, style=None):
        self.label = label
        self.to = to
        self.handler_name = register_handler(f"goto_{label.lower().replace(' ', '_')}", self._navigate)
        super().__init__(style)

    def _navigate(self):
        if router():
            router().navigate(self.to)
            from viewforge.app import App
            app = App.current()
            if app:
                app.reload()

    def render(self):
        return f'<button onclick="{self.handler_name}()"{self.style_attr()}>{self.label}</button>'
