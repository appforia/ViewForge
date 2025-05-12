from viewforge.core.component import Component
from viewforge.routing.router import router, current_route


class RouterView(Component):
    def __init__(self):
        super().__init__()

    def render(self):
        view_html = router().render()

        # Optionally include route meta info or fallback
        route = current_route()
        if not route:
            return "<div class='router-view'>No route selected</div>"

        return f"<div class='router-view'>{view_html}</div>"
