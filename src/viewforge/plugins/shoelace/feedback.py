from viewforge.core.component import Component
from viewforge.state import Signal


class ShoelaceAlert(Component):
    def __init__(self, children=None, open=True, element_id=None, **props):
        self._children = children or []
        self._open = open
        self._props = props
        super().__init__(id=element_id)

    def render(self):
        attr_parts = [f'open'] if self._open else []
        for key, value in self._props.items():
            attr_parts.append(f'{key}="{value}"')
        content = "\n".join(c.render() for c in self._children)
        return f'<sl-alert {' '.join(attr_parts)}{self.style_attr()}>{content}</sl-alert>'


class ShoelaceSpinner(Component):
    def __init__(self, element_id=None, **props):
        self._props = props
        super().__init__(id=element_id)

    def render(self):
        attr_parts = [f'{key}="{value}"' for key, value in self._props.items()]
        return f'<sl-spinner {' '.join(attr_parts)}{self.style_attr()} />'


class ShoelaceProgressBar(Component):
    def __init__(self, value: int | Signal = 0, element_id=None, **props):
        self._value = value
        self._props = props
        super().__init__(id=element_id)

    def render(self):
        val = self._value() if isinstance(self._value, Signal) else self._value
        self._props['value'] = val
        attr_parts = [f'{key}="{value}"' for key, value in self._props.items()]
        return f'<sl-progress-bar {' '.join(attr_parts)}{self.style_attr()} />'


class ShoelaceTooltip(Component):
    def __init__(self, content: str, children=None, element_id=None, **props):
        self._content = content
        self._children = children or []
        self._props = props
        super().__init__(id=element_id)

    def render(self):
        attr_parts = [f'content="{self._content}"']
        attr_parts += [f'{key}="{value}"' for key, value in self._props.items()]
        child_html = "\n".join(child.render() for child in self._children)
        return f'<sl-tooltip {' '.join(attr_parts)}{self.style_attr()}>{child_html}</sl-tooltip>'


class ShoelaceSkeleton(Component):
    def __init__(self, element_id=None, **props):
        self._props = props
        super().__init__(id=element_id)

    def render(self):
        attr_parts = [f'{key}="{value}"' for key, value in self._props.items()]
        return f'<sl-skeleton {' '.join(attr_parts)}{self.style_attr()} />'


class ShoelaceProgressRing(Component):
    def __init__(self, value: int, **props):
        self.value = value
        self._props = props
        super().__init__()

    def render(self):
        self._props["value"] = self.value
        return f'<sl-progress-ring {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-progress-ring>'


class ShoelaceRating(Component):
    def __init__(self, value: int, max: int = 5, **props):
        self.value = value
        self.max = max
        self._props = props
        super().__init__()

    def render(self):
        self._props["value"] = self.value
        self._props["max"] = self.max
        return f'<sl-rating {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-rating>'
