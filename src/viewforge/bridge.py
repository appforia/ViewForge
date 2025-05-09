class Bridge:
    def __init__(self):
        self._handlers = {}

    def register(self, name, func):
        self._handlers[name] = func
        return name

    def get_handlers(self):
        return self._handlers

    def handle_event(self, name, *args, **kwargs):
        if name in self._handlers:
            return self._handlers[name](*args, **kwargs)
        raise ValueError(f"No handler registered for event '{name}'")

    def generate_js_stubs(self):
        stubs = []
        for name in self._handlers:
            stubs.append(f"function {name}(...args) {{ window.pywebview.api.{name}(...args); }}")
        return "\n".join(stubs)


# Singleton pattern for global access
_bridge_instance = Bridge()


def register_handler(name, func):
    return _bridge_instance.register(name, func)


def get_handlers():
    return _bridge_instance.get_handlers()


def handle_event(name, *args, **kwargs):
    return _bridge_instance.handle_event(name, *args, **kwargs)


def generate_js_stubs():
    return _bridge_instance.generate_js_stubs()
