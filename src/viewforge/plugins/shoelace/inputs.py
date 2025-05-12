from viewforge.core.component import Component
from viewforge.state import Signal


class ShoelaceCheckbox(Component):
    def __init__(self, checked: bool | Signal, on_change=None, **props):
        self.checked = checked
        self._props = props
        if isinstance(self.checked, Signal) and on_change is None:
            self._props["on_change"] = lambda e: self.checked.set(e)
        elif on_change:
            self._props["on_change"] = on_change
        super().__init__()

    def render(self):
        checked = self.checked() if isinstance(self.checked, Signal) else self.checked
        self._props["checked"] = "true" if checked else "false"
        return f'<sl-checkbox {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-checkbox>'


class ShoelaceRadio(Component):
    def __init__(self, value: str, **props):
        self.value = value
        self._props = props
        super().__init__()

    def render(self):
        self._props["value"] = self.value
        return f'<sl-radio {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-radio>'


class ShoelaceRadioGroup(Component):
    def __init__(self, value: str | Signal, on_change=None, **props):
        self.value = value
        self._props = props
        if isinstance(self.value, Signal) and on_change is None:
            self._props["on_change"] = lambda e: self.value.set(e)
        elif on_change:
            self._props["on_change"] = on_change
        super().__init__()

    def render(self):
        current = self.value() if isinstance(self.value, Signal) else self.value
        self._props["value"] = current
        return f'<sl-radio-group {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-radio-group>'


class ShoelaceTextarea(Component):
    def __init__(self, value: str | Signal, placeholder: str = "", **props):
        self.value = value
        self.placeholder = placeholder
        self._props = props
        super().__init__()

    def render(self):
        val = self.value() if isinstance(self.value, Signal) else self.value
        self._props["value"] = val
        self._props["placeholder"] = self.placeholder
        return f'<sl-textarea {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-textarea>'


class ShoelaceRange(Component):
    def __init__(self, value: int | Signal, min: int = 0, max: int = 100, step: int = 1, **props):
        self.value = value
        self._props = props
        self._props["min"] = min
        self._props["max"] = max
        self._props["step"] = step
        super().__init__()

    def render(self):
        val = self.value() if isinstance(self.value, Signal) else self.value
        self._props["value"] = val
        return f'<sl-range {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-range>'


class ShoelaceSwitch(Component):
    def __init__(self, checked: bool | Signal, on_change=None, **props):
        self.checked = checked
        self._props = props
        if isinstance(self.checked, Signal) and on_change is None:
            self._props["on_change"] = lambda e: self.checked.set(e)
        elif on_change:
            self._props["on_change"] = on_change
        super().__init__()

    def render(self):
        checked = self.checked() if isinstance(self.checked, Signal) else self.checked
        self._props["checked"] = "true" if checked else "false"
        return f'<sl-switch {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-switch>'


class ShoelaceColorPicker(Component):
    def __init__(self, value: str | Signal, **props):
        self.value = value
        self._props = props
        super().__init__()

    def render(self):
        val = self.value() if isinstance(self.value, Signal) else self.value
        self._props["value"] = val
        return f'<sl-color-picker {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-color-picker>'


class ShoelaceInput(Component):
    def __init__(self, value: str | Signal, placeholder: str = "", **props):
        self.value = value
        self.placeholder = placeholder
        self._props = props
        super().__init__()

    def render(self):
        val = self.value() if isinstance(self.value, Signal) else self.value
        if isinstance(self.value, Signal) and "on_input" not in self._props:
            self._props["on_input"] = lambda e: self.value.set(e)
        self._props["value"] = val
        self._props["placeholder"] = self.placeholder
        return f'<sl-input {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-input>'


class ShoelaceSelect(Component):
    def __init__(self, value: str | Signal, **props):
        self.value = value
        self._props = props
        super().__init__()

    def render(self):
        val = self.value() if isinstance(self.value, Signal) else self.value
        if isinstance(self.value, Signal) and "on_change" not in self._props:
            self._props["on_change"] = lambda e: self.value.set(e)
        self._props["value"] = val
        return f'<sl-select {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-select>'
