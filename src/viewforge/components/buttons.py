from viewforge.core.component import Component
from viewforge.state.signal import Signal


class ShoelaceButton(Component):
    def __init__(self, label: str | Signal, **props):
        self.label = label
        super().__init__(**props)

    def render(self):
        content = self.label() if isinstance(self.label, Signal) else self.label
        return f'<sl-button id="{self.id}"{self.attributes("button")}>{content}</sl-button>'


class ShoelaceIconButton(Component):
    def __init__(self, name: str, library: str = "default", label: str = "", **props):
        self.name = name
        self.library = library
        self.label = label
        super().__init__(**props)

    def render(self):
        return (
            f'<sl-icon-button id="{self.id}" name="{self.name}" '
            f'library="{self.library}" label="{self.label}"{self.attributes("icon-button")}></sl-icon-button>'
        )


class ShoelaceButtonGroup(Component):
    def __init__(self, **props):
        super().__init__(**props)

    def render(self):
        return f'<sl-button-group id="{self.id}"{self.attributes("button-group")}></sl-button-group>'


class ShoelaceCopyButton(Component):
    def __init__(self, value: str, **props):
        self.value = value
        super().__init__(**props)

    def render(self):
        return f'<sl-copy-button id="{self.id}" value="{self.value}"{self.attributes("copy-button")}></sl-copy-button>'
