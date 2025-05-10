from typing import List, Optional, Unpack
from viewforge.component import Component
from viewforge.libtypes import StyleProps, Css


class Box(Component):
    def __init__(
        self,
        children: Optional[List[Component]] = None,
        *,
        css: Css = None,
        **props: StyleProps
    ):
        self.children = children or []
        super().__init__(default_style={}, css=css, **props)

    def render(self):
        child_html = "\n".join(child.render() for child in self.children)
        return f'<div id="{self._id}"{self.style_attr()}>{child_html}</div>'
