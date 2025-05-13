from viewforge.core.component import Component


class ShoelaceDialog(Component):
    def __init__(self, label: str = "", **props):
        self.label = label
        self._props = props
        super().__init__()

    def render(self):
        label_attr = f'label="{self.label}"' if self.label else ""
        props = " ".join(f'{k}="{v}"' for k, v in self._props.items())
        return f'<sl-dialog {label_attr} {props}></sl-dialog>'


class ShoelaceDrawer(Component):
    def __init__(self, label: str = "", **props):
        self.label = label
        self._props = props
        super().__init__()

    def render(self):
        label_attr = f'label="{self.label}"' if self.label else ""
        props = " ".join(f'{k}="{v}"' for k, v in self._props.items())
        return f'<sl-drawer {label_attr} {props}></sl-drawer>'


class ShoelaceDropdown(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-dropdown {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-dropdown>'


class ShoelacePopup(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-popup {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-popup>'


class ShoelaceSplitPanel(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-split-panel {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-split-panel>'


class ShoelaceCarousel(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-carousel {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-carousel>'


class ShoelaceCarouselItem(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-carousel-item {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-carousel-item>'
