from typing import Callable, Optional


class HandlerRegistry:
    __slots__ = ("_handlers", "__dict__")

    def __init__(self):
        self._handlers: dict[str, Callable] = {}

    def register(self, name: str, func: Callable) -> str:
        if name in self._handlers:
            print(f"[handler] Overwriting existing handler: {name}")
        self._handlers[name] = func
        setattr(self, name, func)
        return name

    def unregister(self, name: str):
        if name in self._handlers:
            del self._handlers[name]
            if hasattr(self, name):
                delattr(self, name)
            print(f"[handler] Unregistered: {name}")

    def get(self) -> dict[str, Callable]:
        return self._handlers

    def call(self, name: str, *args):
        if name in self._handlers:
            return self._handlers[name](*args)
        raise ValueError(f"[handler] No handler named '{name}'")

    def __contains__(self, name: str) -> bool:
        return name in self._handlers

    def __getitem__(self, name: str) -> Callable:
        return self._handlers[name]


# Singleton instance
handler_registry = HandlerRegistry()


def handler(name: Optional[str] = None):
    def decorator(fn: Callable):
        handler_name = name or fn.__name__
        fn._handler_name = handler_name
        handler_registry.register(handler_name, fn)
        print(f"[handler] Registered: {handler_name}")
        return fn
    return decorator
