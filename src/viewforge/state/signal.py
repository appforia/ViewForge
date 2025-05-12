from typing import Callable, Any, List


class Signal:
    """A reactive signal holding a single value and notifying subscribers on change."""
    _subscriber_stack: List[Callable[[Any], None]] = []

    def __init__(self, value: Any):
        self._value = value
        self._subscribers: List[Callable[[Any], None]] = []

    def __call__(self) -> Any:
        # Track current subscriber if in tracking context
        if Signal._subscriber_stack:
            subscriber = Signal._subscriber_stack[-1]
            if subscriber not in self._subscribers:
                self._subscribers.append(subscriber)
        return self._value

    def set(self, new_value: Any):
        if self._value != new_value:
            self._value = new_value
            for callback in self._subscribers:
                callback(new_value)

    def subscribe(self, callback: Callable[[Any], None]):
        if callback not in self._subscribers:
            self._subscribers.append(callback)

    @staticmethod
    def begin_tracking(subscriber: Callable[[Any], None]):
        Signal._subscriber_stack.append(subscriber)

    @staticmethod
    def end_tracking():
        if Signal._subscriber_stack:
            Signal._subscriber_stack.pop()


class Computed:
    """A read-only reactive signal derived from other signals."""
    def __init__(self, compute_fn: Callable[[], Any]):
        self._compute_fn = compute_fn
        self._cached = None
        self._setup()

    def _setup(self):
        def recalculate(_=None):
            self._cached = self._compute_fn()

        Signal.begin_tracking(recalculate)
        self._cached = self._compute_fn()
        Signal.end_tracking()

    def __call__(self) -> Any:
        return self._cached
