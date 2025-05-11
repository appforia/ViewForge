from viewforge.component import Component
from viewforge.router import router


class RouterView(Component):
    def __init__(self):
        super().__init__()

    def render(self):
        return router().render()
