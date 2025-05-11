import webview
from viewforge.rendering.render import render_html
from viewforge.core.registry import handler_registry
from viewforge.routing.router import register_decorated_routes, _route_registry, router
from viewforge.routing.router_view import RouterView


class App:
    _instance = None

    def __init__(self, router=None, title: str = "ViewForge App"):
        self.window = None
        self.title = title
        self.router = router
        self._components = None
        App._instance = self
        self.api = API()

    def run(self, components=None, debug=False):
        # Automatically register decorated routes
        if _route_registry:
            register_decorated_routes()
            router().navigate("/")  # Ensure initial route

        if components:
            if callable(components):
                print("[App] Building components...")
                self._components = components()
            else:
                self._components = components
            html = render_html(self._components, title=self.title)

        elif self.router:
            html = render_html([RouterView(self.router)], title=self.title)
        else:
            html = "<h1>No components or router provided</h1>"

        print("[App] Creating window")
        print("Registered handlers:", list(handler_registry.get().keys()))
        self.window = webview.create_window(self.title, html=html, js_api=self.api)
        webview.start(debug=debug, http_server=True)

    def reload(self):
        if self.window:
            if self.router:
                html = render_html([RouterView(self.router)], title=self.title)
            else:
                html = render_html(self._components, title=self.title)
            script = f"document.documentElement.innerHTML = `{html}`"
            self.window.evaluate_js(script)

    @classmethod
    def current(cls):
        return cls._instance


class API:
    def handle_event(self, name, *args):
        print(f"[API] Handling event: {name} with args: {args}")
        handler = handler_registry.get().get(name)
        if handler:
            return handler(*args)
        raise ValueError(f"No handler named '{name}'")
