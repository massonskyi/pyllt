__all__ = ['Signal']

from typing import List, Callable
from gllt.engine.base_signal import BaseSignal


class Signal(BaseSignal):
    def __init__(self):
        super().__init__()
        self._slots: List[object | Callable] = []

    def connect(self, slot: object | Callable):
        self._slots.append(slot)

    def emit(self, *args, **kwargs):
        for slot in self._slots:
            slot(*args, **kwargs)
