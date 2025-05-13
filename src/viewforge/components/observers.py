from viewforge.core.component import Component


class ShoelaceMutationObserver(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-mutation-observer {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-mutation-observer>'


class ShoelaceResizeObserver(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-resize-observer {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-resize-observer>'
