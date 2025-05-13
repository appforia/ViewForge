import os
import webview
from importlib.resources import files
from viewforge.core.registry import handler_registry
from viewforge.routing.router import register_decorated_routes, router
from viewforge.routing.router_view import RouterView
from viewforge.utils.tempdir import viewforge_runtime_dir
from viewforge.utils.extract_static_assets import extract_static_assets


class App:
    _instance = None
    _default_template_path = str(files("viewforge.static").joinpath("index.html"))

    def __init__(self, title: str = "ViewForge App"):
        self.window = None
        self.title = title
        self._components = None
        App._instance = self
        self.api = API()

    def run(self, components=None, debug=False):
        runtime_dir = viewforge_runtime_dir()
        output_html = os.path.join(runtime_dir, "index.html")
        assets_dir = os.path.join(runtime_dir, "assets")

        if components is None:
            print("[App] Router mode enabled — using registered @route views.")
            register_decorated_routes()
            router().navigate("/")

        if components:
            if callable(components):
                print("[App] Building components...")
                result = components()
                self._components = result if isinstance(result, list) else [result]
            else:
                self._components = components if isinstance(components, list) else [components]

            extract_static_assets(assets_dir)

            file_path = App.inject_into_template(
                template_path=App._default_template_path,
                out_path=output_html,
                components=self._components,
                placeholder="<!--VIEWFORGE-CONTENT-->"
            )

        else:
            current_path = router()()
            router().navigate(current_path or "/")
            extract_static_assets(assets_dir)

            file_path = App.inject_into_template(
                template_path=App._default_template_path,
                out_path=output_html,
                components=[RouterView()],
                placeholder="<!--VIEWFORGE-CONTENT-->"
            )

        print("[App] Creating window")
        print("Registered handlers:", list(handler_registry.get().keys()))
        self.window = webview.create_window(self.title, url=f"file://{file_path}", js_api=self.api)
        webview.start(debug=debug, http_server=True)

    def reload(self):
        if self.window:
            runtime_dir = viewforge_runtime_dir()
            output_html = os.path.join(runtime_dir, "index.html")
            assets_dir = os.path.join(runtime_dir, "assets")

            if self._components:
                components = self._components
                if not isinstance(components, list):
                    components = [components]
                extract_static_assets(assets_dir)
                file_path = App.inject_into_template(
                    template_path=App._default_template_path,
                    out_path=output_html,
                    components=components,
                    placeholder="<!--VIEWFORGE-CONTENT-->"
                )
            else:
                current_path = router()()
                router().navigate(current_path or "/")
                extract_static_assets(assets_dir)
                file_path = App.inject_into_template(
                    template_path=App._default_template_path,
                    out_path=output_html,
                    components=[RouterView()],
                    placeholder="<!--VIEWFORGE-CONTENT-->"
                )

            self.window.load_url(f"file://{file_path}")

    def evaluate_js(self, js_code: str):
        if self.window:
            return self.window.evaluate_js(js_code)
        return None

    @staticmethod
    def inject_into_template(template_path, out_path, components, placeholder="<!--VIEWFORGE-CONTENT-->"):
        with open(template_path, "r", encoding="utf-8") as f:
            html = f.read()

        rendered = "\n".join(c.render() for c in components)
        html = html.replace(placeholder, rendered)

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        return os.path.abspath(out_path)

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
