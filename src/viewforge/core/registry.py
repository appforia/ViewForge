from typing import Callable

class HandlerRegistry:
    def __init__(self):
        self._handlers = {}

    def register(self, name: str, func: Callable):
        self._handlers[name] = func
        setattr(self, name, func)  # ensures pywebview.api.name is callable
        return name

    def get(self):
        return self._handlers

handler_registry = HandlerRegistry()

def handler(name: str = None):
    def decorator(fn):
        handler_name = name or fn.__name__
        fn._handler_name = handler_name
        handler_registry.get()[handler_name] = fn
        print(f"[handler] Registered: {handler_name}")
        return fn
    return decorator
