from viewforge.state.signal import Signal

class Store:
    def __init__(self, state: dict):
        self._signals = {k: Signal(v) for k, v in state.items()}
        self._actions = {}

    def __getattr__(self, name):
        if name in self._signals:
            return self._signals[name]()
        raise AttributeError(f"No such store attribute: {name}")

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        elif name in self._signals:
            self._signals[name].set(value)
        else:
            self._signals[name] = Signal(value)

    def signal(self, name):
        return self._signals[name]

    def subscribe(self, name, callback):
        if name in self._signals:
            self._signals[name].subscribe(callback)
        else:
            raise KeyError(f"No signal named '{name}'")

    def add_action(self, name, func):
        self._actions[name] = func

    def action(self, name):
        return self._actions[name]
