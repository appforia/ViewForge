from viewforge.core.component import Component
from typing import Optional


class ShoelaceIcon(Component):
    def __init__(self, name: str, library: Optional[str] = None, **props):
        self.name = name
        self.library = library
        self._props = props
        super().__init__()

    def render(self) -> str:
        attrs = [f'name="{self.name}"']
        if self.library:
            attrs.append(f'library="{self.library}"')
        for k, v in self._props.items():
            attrs.append(f'{k}="{v}"')
        return f'<sl-icon {" ".join(attrs)}></sl-icon>'


class ShoelaceFormatBytes(Component):
    def __init__(self, value: int, **props):
        self.value = value
        self._props = props
        super().__init__()

    def render(self) -> str:
        return f'<sl-format-bytes value="{self.value}" {self._render_props()}></sl-format-bytes>'

    def _render_props(self):
        return " ".join(f'{k}="{v}"' for k, v in self._props.items())


class ShoelaceFormatDate(Component):
    def __init__(self, date: str, **props):
        self.date = date
        self._props = props
        super().__init__()

    def render(self) -> str:
        return f'<sl-format-date date="{self.date}" {self._render_props()}></sl-format-date>'

    def _render_props(self):
        return " ".join(f'{k}="{v}"' for k, v in self._props.items())


class ShoelaceFormatNumber(Component):
    def __init__(self, number: float, **props):
        self.number = number
        self._props = props
        super().__init__()

    def render(self) -> str:
        return f'<sl-format-number value="{self.number}" {self._render_props()}></sl-format-number>'

    def _render_props(self):
        return " ".join(f'{k}="{v}"' for k, v in self._props.items())


class ShoelaceInclude(Component):
    def __init__(self, src: str, **props):
        self.src = src
        self._props = props
        super().__init__()

    def render(self) -> str:
        return f'<sl-include src="{self.src}" {self._render_props()}></sl-include>'

    def _render_props(self):
        return " ".join(f'{k}="{v}"' for k, v in self._props.items())


class ShoelaceMutationObserver(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self) -> str:
        return f'<sl-mutation-observer {self._render_props()}></sl-mutation-observer>'

    def _render_props(self):
        return " ".join(f'{k}="{v}"' for k, v in self._props.items())


class ShoelaceVisuallyHidden(Component):
    def __init__(self, content: str, **props):
        self.content = content
        self._props = props
        super().__init__()

    def render(self) -> str:
        return f'<sl-visually-hidden {self._render_props()}>{self.content}</sl-visually-hidden>'

    def _render_props(self):
        return " ".join(f'{k}="{v}"' for k, v in self._props.items())
