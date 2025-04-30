# src/viewforge/state.py

from typing import Any, Callable, Dict, Set

class GlobalState:
    def __init__(self):
        self._state: Dict[str, Any] = {}
        self._subscribers: Dict[str, Set[Callable[[Any], None]]] = {}

    def get(self, key: str, default: Any = None) -> Any:
        return self._state.get(key, default)

    def set(self, key: str, value: Any):
        old_value = self._state.get(key)
        self._state[key] = value
        if old_value != value:
            self._notify(key, value)

    def subscribe(self, key: str, callback: Callable[[Any], None]):
        if key not in self._subscribers:
            self._subscribers[key] = set()
        self._subscribers[key].add(callback)

    def unsubscribe(self, key: str, callback: Callable[[Any], None]):
        if key in self._subscribers:
            self._subscribers[key].discard(callback)

    def _notify(self, key: str, value: Any):
        for callback in self._subscribers.get(key, []):
            callback(value)

# Singleton instance
state = GlobalState()
