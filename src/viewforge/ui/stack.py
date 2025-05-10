from typing import List, Unpack
from viewforge.component import Component
from viewforge.libtypes import StyleProps, Css


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
        super().__init__(default_style=default_style, css=css, **props)

    def render(self):
        child_html = "\n".join(child.render() for child in self.children)
        return f'<div id="{self._id}"{self.style_attr()}>{child_html}</div>'
