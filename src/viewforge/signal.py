from typing import Callable, Any, List


class Signal:
    def __init__(self, value: Any):
        self._value = value
        self._subscribers: List[Callable[[Any], None]] = []

    def __call__(self) -> Any:
        return self._value

    def set(self, new_value: Any):
        self._value = new_value
        for callback in self._subscribers:
            callback(new_value)

    def subscribe(self, callback: Callable[[Any], None]):
        self._subscribers.append(callback)


class Computed:
    def __init__(self, compute_fn: Callable[[], Any]):
        self._compute_fn = compute_fn
        self._cached = compute_fn()

    def __call__(self) -> Any:
        return self._compute_fn()
