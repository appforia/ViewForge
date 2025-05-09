from typing import Dict, Any


class Component:
    def __init__(self, style: Dict[str, Any] = None):
        style = style or {}
        self._style_dict = style
        self.style = "; ".join(f"{k}: {v}" for k, v in style.items())

    def render(self) -> str:
        raise NotImplementedError("Subclasses must implement render().")

    def style_attr(self) -> str:
        return f' style="{self.style}"' if self.style else ""
