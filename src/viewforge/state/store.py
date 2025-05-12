from typing import Any, Callable
from viewforge.state.signal import Signal


class Store:
    __slots__ = ("_signals", "_actions")

    def __init__(self, state: dict[str, Any]):
        self._signals: dict[str, Signal] = {k: Signal(v) for k, v in state.items()}
        self._actions: dict[str, Callable] = {}

    def __getattr__(self, name: str) -> Any:
        if name in self._signals:
            return self._signals[name]()
        if name in self._actions:
            return self._actions[name]
        raise AttributeError(f"No such store attribute or action: '{name}'")

    def __setattr__(self, name: str, value: Any):
        if name in self.__slots__:
            super().__setattr__(name, value)
        elif name in self._signals:
            self._signals[name].set(value)
        else:
            self._signals[name] = Signal(value)

    def signal(self, name: str) -> Signal:
        if name in self._signals:
            return self._signals[name]
        raise KeyError(f"No signal named '{name}'")

    def subscribe(self, name: str, callback: Callable[[Any], None]):
        if name in self._signals:
            self._signals[name].subscribe(callback)
        else:
            raise KeyError(f"No signal named '{name}'")

    def add_action(self, name: str, func: Callable):
        self._actions[name] = func

    def action(self, name: str) -> Callable:
        if name in self._actions:
            return self._actions[name]
        raise KeyError(f"No action named '{name}'")
