from viewforge.utils.css import merge_styles
from viewforge.core import handler
from viewforge.core.component import Component
from viewforge.routing import router


class ShoelaceBreadcrumb(Component):
    def render(self):
        return '<sl-breadcrumb></sl-breadcrumb>'


class ShoelaceBreadcrumbItem(Component):
    def __init__(self, href: str = "", **props):
        self.href = href
        self._props = props
        super().__init__()

    def render(self):
        attrs = [f'href="{self.href}"'] + [f'{k}="{v}"' for k, v in self._props.items()]
        return f'<sl-breadcrumb-item {" ".join(attrs)}></sl-breadcrumb-item>'


class ShoelaceMenu(Component):
    def render(self):
        return '<sl-menu></sl-menu>'


class ShoelaceMenuItem(Component):
    def __init__(self, value: str, **props):
        self.value = value
        self._props = props
        super().__init__()

    def render(self):
        props = [f'value="{self.value}"'] + [f'{k}="{v}"' for k, v in self._props.items()]
        return f'<sl-menu-item {" ".join(props)}></sl-menu-item>'


class ShoelaceMenuLabel(Component):
    def __init__(self, label: str):
        self.label = label
        super().__init__()

    def render(self):
        return f'<sl-menu-label>{self.label}</sl-menu-label>'


class ShoelaceTab(Component):
    def __init__(self, slot: str = None, **props):
        self._slot = slot
        self._props = props
        super().__init__()

    def render(self):
        slot_attr = f'slot="{self._slot}"' if self._slot else ""
        props = " ".join(f'{k}="{v}"' for k, v in self._props.items())
        return f'<sl-tab {slot_attr} {props}></sl-tab>'


class ShoelaceTabPanel(Component):
    def __init__(self, slot: str = None, **props):
        self._slot = slot
        self._props = props
        super().__init__()

    def render(self):
        slot_attr = f'slot="{self._slot}"' if self._slot else ""
        props = " ".join(f'{k}="{v}"' for k, v in self._props.items())
        return f'<sl-tab-panel {slot_attr} {props}></sl-tab-panel>'


class ShoelaceTree(Component):
    def render(self):
        return '<sl-tree></sl-tree>'


class ShoelaceTreeItem(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        props = " ".join(f'{k}="{v}"' for k, v in self._props.items())
        return f'<sl-tree-item {props}></sl-tree-item>'


class RouteLinkButton(Component):
    def __init__(self, label: str, to: str, css=None, active_css=None):
        self.label = label
        self.to = to
        self._handler = self._register_handler()
        self.active_css = active_css or {"font_weight": "bold"}
        super().__init__(css)

    def _register_handler(self):
        name = f"goto_{self.label.lower().replace(' ', '_')}"

        @handler(name)
        def _go():
            router().navigate(self.to)

        return name

    def render(self):
        is_active = router()() == self.to
        style = merge_styles(self.css, self.active_css if is_active else None)
        css_str = f' style="{style}"' if style else ""
        return f'<button onclick="vf(\'{self._handler}\')"{css_str}>{self.label}</button>'
