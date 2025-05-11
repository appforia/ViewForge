from viewforge.core.component import Component
from viewforge.routing.router import router
from viewforge.core.registry import handler
from viewforge.utils.css import merge_styles

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
