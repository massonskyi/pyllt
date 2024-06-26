__all__ = ['Slot']

from typing import Callable

from gllt.linux.engine.base_slot import BaseSlot


class Slot(BaseSlot):
    def __init__(self, function: Callable):
        super().__init__(function)
        self.function = function

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
