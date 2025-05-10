import uuid
from viewforge.app import App


class Component:
    def __init__(self, css=None, **style):
        self._id = f"vf-{uuid.uuid4().hex[:8]}"
        self.css = css or {}
        self.style = style
        self._rendered_once = False  # Optional: track lifecycle

    def style_attr(self):
        if not self.style:
            return ""
        styles = "; ".join(f"{k.replace('_', '-')}: {v}" for k, v in self.style.items())
        return f' style="{styles}"'

    def render(self) -> str:
        raise NotImplementedError("Subclasses must implement render()")

    def update(self, _=None):
        html = self.render().replace("`", "\\`")  # escape backticks
        script = f'document.getElementById("{self._id}").outerHTML = `{html}`;'
        print(f"[ViewForge] Updating #{self._id}")
        App.current().window.evaluate_js(script)
