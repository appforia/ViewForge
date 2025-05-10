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
    def decorator(func: Callable):
        func_name = name or f"on_{func.__name__}"
        func._handler_name = func_name
        handler_registry.register(func_name, func)
        return func
    return decorator
