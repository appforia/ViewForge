import re
from urllib.parse import urlencode, urlparse, parse_qs
from typing import Callable, Optional, Tuple


class Route:
    def __init__(self, name: str, path: str, view: Callable[[dict], 'Component']):
        self.name = name
        self.path = path
        self.view = view
        self._pattern, self._param_names = self._compile_path(path)

    def _compile_path(self, path: str) -> Tuple[re.Pattern, list]:
        parts = path.strip("/").split("/")
        pattern_parts = []
        param_names = []
        for part in parts:
            if part.startswith("<") and part.endswith(">"):
                name = part[1:-1]
                param_names.append(name)
                pattern_parts.append(r"(?P<%s>[^/]+)" % name)
            else:
                pattern_parts.append(re.escape(part))
        pattern = re.compile("^" + "/".join(pattern_parts) + "$")
        return pattern, param_names

    def match(self, path: str) -> Optional[dict]:
        match = self._pattern.match(path.strip("/"))
        if match:
            return match.groupdict()
        return None

    def build_path(self, *args, **kwargs) -> str:
        path = self.path
        for name, value in zip(self._param_names, args):
            path = path.replace(f"<{name}>", str(value))
        if kwargs:
            path += "?" + urlencode(kwargs)
        return path


class Router:
    def __init__(self):
        self.routes: list[Route] = []
        self.named_routes: dict[str, Route] = {}
        self.current_view: Optional[Callable] = None
        self.current_path: str = "/"
        self.current_params: dict = {}

    def add_route(self, path: str, view: Callable[[dict], 'Component'], name: Optional[str] = None):
        name = name or path.strip("/").split("/")[0] or "root"
        route = Route(name, path, view)
        self.routes.append(route)
        self.named_routes[name] = route

    def navigate(self, full_path: str):
        url = urlparse(full_path)
        path = url.path.strip("/")
        query = {k: v[0] if len(v) == 1 else v for k, v in parse_qs(url.query).items()}

        for route in self.routes:
            params = route.match(path)
            if params is not None:
                self.current_path = full_path
                self.current_params = {**params, "query": query}
                self.current_view = route.view
                return

        self.current_view = lambda params={}: NotFoundView()
        self.current_params = {"query": query}

    def render(self):
        if self.current_view:
            return self.current_view(self.current_params).render()
        return "<h1>404 Not Found</h1>"


def NotFoundView():
    from viewforge.ui import Text
    return Text("404 - Page not found")


# Global instance
_router_instance: Optional[Router] = None


def create_router():
    global _router_instance
    _router_instance = Router()
    return _router_instance


class RouterSignal:
    def __init__(self, router: Router):
        self._router = router

    def __call__(self) -> str:
        return self._router.current_path

    def navigate(self, name_or_path: str, *args, **kwargs):
        route = self._router.named_routes.get(name_or_path)
        if route:
            full_path = route.build_path(*args, **kwargs)
        else:
            full_path = name_or_path
        self._router.navigate(full_path)
        from viewforge.app import App
        app = App.current()
        if app:
            app.reload()

    def reverse(self, name: str, *args, **kwargs) -> str:
        route = self._router.named_routes.get(name)
        if not route:
            raise ValueError(f"No route named '{name}'")
        return route.build_path(*args, **kwargs)

    def params(self) -> dict:
        return self._router.current_params

    def query(self) -> dict:
        return self._router.current_params.get("query", {})


def router() -> RouterSignal:
    return RouterSignal(_router_instance)
