# src/viewforge/router.py

from typing import Callable, Dict

class Router:
    def __init__(self, mode: str = "hash"):
        self.mode = mode
        self.routes: Dict[str, Callable[[], None]] = {}
        self.current_path = "/"
        self.window = None

    def register(self, path: str, handler: Callable[[], None]):
        self.routes[path] = handler

    def navigate(self, path: str):
        if self.window:
            if self.mode == "hash":
                self.window.evaluate_js(f'window.location.hash = "#{path}";')
            elif self.mode == "history":
                self.window.evaluate_js(
                    f'''
                    window.history.pushState(null, "", "/{path}");
                    window.dispatchEvent(new Event("popstate"));
                    '''
                )

    def attach_webview(self, webview_window):
        self.window = webview_window
