from viewforge.bridge import generate_js_stubs
import webview
from viewforge.render import render_html

def inject_js(html: str) -> str:
    stub_script = f"<script>\n{generate_js_stubs()}\n</script>"
    return html.replace("</body>", stub_script + "\n</body>")

class App:
    _instance = None

    def __init__(self, router=None):
        self.window = None
        self._components = []
        self.router = router
        App._instance = self
        self.api = AppAPI()

    def run(self, components=None):
        if components:
            self._components = components
            html = render_html(components)
        elif self.router:
            html = inject_js(render_html([RouterView(self.router)]))
        else:
            html = "<h1>No components or router provided</h1>"

        self.window = webview.create_window("ViewForge App", html=html, js_api=self.api)
        webview.start(http_server=True)

    def reload(self):
        if self.window:
            if self.router:
                html = inject_js(render_html([RouterView(self.router)]))
            else:
                html = inject_js(render_html(self._components))
            script = f"document.documentElement.innerHTML = `{html}`"
            self.window.evaluate_js(script)

    @classmethod
    def current(cls):
        return cls._instance

class AppAPI:
    def ping(self):
        print("JS → Python: ping received")

    def reload(self):
        print("JS → Python: reload requested")
        app = App.current()
        if app:
            app.reload()

class RouterView:
    def __init__(self, router):
        self.router = router

    def render(self):
        return self.router.render()
