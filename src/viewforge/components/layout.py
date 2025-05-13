from typing import List, Optional

from viewforge.core import Component
from viewforge.core.component import Component
from viewforge.core.libtypes import Css, StyleProps


class ShoelaceCard(Component):
    def __init__(self, children=None, **props):
        self._children = children or []
        self._props = props
        super().__init__()

    def render(self):
        slot_names = {getattr(child, "_slot", None) for child in self._children}
        slot_flags = {
            "header": "card-header",
            "footer": "card-footer",
        }

        classes = ["card-basic"]
        classes += [slot_flags[slot] for slot in slot_names if slot in slot_flags]

        if "class" in self._props:
            classes.append(self._props.pop("class"))

        self._props["class"] = " ".join(classes)
        children_html = "\n".join(child.render() for child in self._children)
        return f'<sl-card {" ".join(f"{k}={v!r}" for k, v in self._props.items())}>{children_html}</sl-card>'


class CardHeader(Component):
    _slot = "header"

    def __init__(self, content: str):
        self.content = content
        super().__init__()

    def render(self):
        return f'<div slot="header" class="card-header">{self.content}</div>'


class CardBody(Component):
    def __init__(self, content: str):
        self.content = content
        super().__init__()

    def render(self):
        return f'<div>{self.content}</div>'


class CardFooter(Component):
    _slot = "footer"

    def __init__(self, content: str):
        self.content = content
        super().__init__()

    def render(self):
        return f'<div slot="footer" class="card-footer">{self.content}</div>'


class ShoelaceTabGroup(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-tab-group {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-tab-group>'


class ShoelaceDivider(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-divider {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-divider>'


class ShoelaceTab(Component):
    def __init__(self, panel: str, **props):
        self.panel = panel
        self._props = props
        super().__init__()

    def render(self):
        self._props["panel"] = self.panel
        return f'<sl-tab {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-tab>'


class ShoelaceTabPanel(Component):
    def __init__(self, name: str, **props):
        self.name = name
        self._props = props
        super().__init__()

    def render(self):
        self._props["name"] = self.name
        return f'<sl-tab-panel {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-tab-panel>'


class ShoelaceSplitPanel(Component):
    def __init__(self, **props):
        self._props = props
        super().__init__()

    def render(self):
        return f'<sl-split-panel {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-split-panel>'


class ShoelaceDrawer(Component):
    def __init__(self, label: str = "", **props):
        self.label = label
        self._props = props
        super().__init__()

    def render(self):
        self._props["label"] = self.label
        return f'<sl-drawer {" ".join(f"{k}={v!r}" for k, v in self._props.items())}></sl-drawer>'


class Stack(Component):
    def __init__(
            self,
            children: List[Component],
            *,
            css: Css = None,
            **props: StyleProps
    ):
        self.children = children or []

        default_style = {
            "display": "flex",
            "flex_direction": "column",
            "gap": "1rem",
        }

        super().__init__(css=css, **default_style, **props)

    def render(self):
        child_html = "\n".join(child.render() for child in self.children)
        return f'<div id="{self.id}"{self.event_attr()}{self.style_attr()}>{child_html}</div>'


class Box(Component):
    def __init__(
            self,
            children: Optional[List[Component]] = None,
            *,
            css: Css = None,
            **props: StyleProps
    ):
        self.children = children or []
        super().__init__(css=css, **props)

    def render(self):
        child_html = "\n".join(child.render() for child in self.children)
        return f'<div id="{self.id}"{self.event_attr()}{self.style_attr()}>{child_html}</div>'
