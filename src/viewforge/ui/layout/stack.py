from typing import List
from viewforge.core.component import Component
from viewforge.core.libtypes import StyleProps, Css


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
