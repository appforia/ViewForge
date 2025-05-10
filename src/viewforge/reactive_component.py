from viewforge.app import App
from viewforge.signal import Signal
from viewforge.component import Component

class ReactiveComponent(Component):
    def render(self) -> str:
        # Begin tracking dependencies for this instance
        Signal.begin_tracking(self.update)
        html = self._render_content()
        Signal.end_tracking()
        return html

    def _render_content(self) -> str:
        raise NotImplementedError("Subclasses must implement _render_content()")

    def update(self, _=None):
        html = self.render().replace("`", "\\`")
        js = f'document.getElementById("{self._id}").outerHTML = `{html}`;'
        print(f"[Reactive] Updating {self.__class__.__name__} #{self._id}")
        App.current().window.evaluate_js(js)
