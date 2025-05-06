import json
from viewforge.app import App

class Component:
    def render(self) -> str:
        raise NotImplementedError()

class Text(Component):
    def __init__(self, content: str, justify: str = "left"):
        self.content = content
        self.justify = justify

    def render(self):
        return f'<div style="text-align: {self.justify};">{self.content}</div>'

class Button(Component):
    def __init__(self, text: str, handler=None, bind=None):
        self.text = text
        self.bind = bind or []

        if callable(handler):
            handler_name = getattr(handler, "_handler_name", None)
            if not handler_name:
                handler_name = App.current().register_anonymous(handler)
        else:
            handler_name = handler or ""

        self.handler_name = handler_name

    def render(self):
        bind_json = json.dumps(self.bind)
        return (
            f'<button data-handler="{self.handler_name}" data-bind=\'{bind_json}\' onclick="sendBoundForm(this)">'
            f'{self.text}</button>'
        )

class TextInput(Component):
    def __init__(self, name: str, placeholder: str = ""):
        self.name = name
        self.placeholder = placeholder

    def render(self):
        return (
            f'<input type="text" id="{self.name}" placeholder="{self.placeholder}" '
            f'style="padding: 6px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px;" />'
        )

class PasswordInput(Component):
    def __init__(self, name: str, placeholder: str = ""):
        self.name = name
        self.placeholder = placeholder

    def render(self):
        return (
            f'<input type="password" id="{self.name}" placeholder="{self.placeholder}" '
            f'style="padding: 6px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px;" />'
        )

class Checkbox(Component):
    def __init__(self, label: str, name: str, checked: bool = False):
        self.label = label
        self.name = name
        self.checked = checked

    def render(self):
        checked_attr = "checked" if self.checked else ""
        return (
            f'<label style="display: flex; align-items: center; gap: 8px;">'
            f'<input type="checkbox" id="{self.name}" {checked_attr} />{self.label}'
            f'</label>'
        )

class SelectBox(Component):
    def __init__(self, name: str, options: list[str], selected: str = ""):
        self.name = name
        self.options = options
        self.selected = selected

    def render(self):
        options_html = ''.join(
            f'<option value="{opt}"{" selected" if opt == self.selected else ""}>{opt}</option>'
            for opt in self.options
        )
        return (
            f'<select id="{self.name}" '
            f'style="padding: 6px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px;">'
            f'{options_html}</select>'
        )

class RadioButtonGroup(Component):
    def __init__(self, name: str, options: list[str], selected: str = ""):
        self.name = name
        self.options = options
        self.selected = selected

    def render(self):
        radios = ""
        for opt in self.options:
            checked = "checked" if opt == self.selected else ""
            radios += (
                f'<label style="margin-right: 8px;">'
                f'<input type="radio" name="{self.name}" value="{opt}" {checked} '
                f'onchange="document.getElementById(\'{self.name}\').value = this.value;" /> {opt}'
                f'</label>'
            )
        return (
            f'<input type="hidden" id="{self.name}" value="{self.selected}"/>'
            f'<div style="display: flex; flex-wrap: wrap; gap: 8px;">{radios}</div>'
        )

class TextArea(Component):
    def __init__(self, name: str, placeholder: str = "", rows: int = 4):
        self.name = name
        self.placeholder = placeholder
        self.rows = rows

    def render(self):
        return (
            f'<textarea id="{self.name}" placeholder="{self.placeholder}" rows="{self.rows}" '
            f'style="width: 100%; padding: 6px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px;"></textarea>'
        )

class ValidationMessage(Component):
    def __init__(self, message: str, visible: bool = False, id: str = "validation-message"):
        self.message = message
        self.visible = visible
        self.id = id

    def render(self):
        style = (
            "color: red; font-size: 12px; margin-top: 4px;"
            + (" display: block;" if self.visible else " display: none;")
        )
        return f'<div id="{self.id}" style="{style}">{self.message}</div>'

class StackFrame(Component):
    def __init__(self):
        self.children = []
        self.style = {}

    def configure(self, **kwargs):
        self.style.update(kwargs)
        return self

    def add(self, *components):
        self.children.extend(components)
        return self

    def render(self):
        padding = self.style.get("padding", 0)
        gap = self.style.get("gap", 0)
        direction = self.style.get("direction", "vertical")
        style_str = f"display: flex; flex-direction: {'column' if direction == 'vertical' else 'row'}; gap: {gap}px; padding: {padding}px;"
        return f'<div style="{style_str}">' + ''.join(child.render() for child in self.children) + '</div>'

class GridFrame(Component):
    def __init__(self, columns: int = 2, gap: int = 8):
        self.columns = columns
        self.gap = gap
        self.children = []

    def add(self, *components):
        self.children.extend(components)
        return self

    def render(self):
        style = (
            f"display: grid; "
            f"grid-template-columns: repeat({self.columns}, 1fr); "
            f"gap: {self.gap}px;"
        )
        return f'<div style="{style}">' + ''.join(child.render() for child in self.children) + '</div>'

class AbsoluteFrame(Component):
    def __init__(self, width: int = 400, height: int = 300):
        self.width = width
        self.height = height
        self.children = []

    def add(self, *components):
        self.children.extend(components)
        return self

    def render(self):
        return (
            f'<div style="position: relative; width: {self.width}px; height: {self.height}px; border: 1px solid #ccc;">'
            + ''.join(child.render() for child in self.children)
            + '</div>'
        )

class Positioned(Component):
    def __init__(self, component: Component, x: int, y: int):
        self.component = component
        self.x = x
        self.y = y

    def render(self):
        return f'<div style="position: absolute; left: {self.x}px; top: {self.y}px;">{self.component.render()}</div>'
