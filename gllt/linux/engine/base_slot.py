__all__ = ['BaseSlot']

from typing import Callable


class BaseSlot:
    def __init__(self, function: Callable):
        """
        Initialize the slot
        """
        pass

    def __call__(self, *args, **kwargs):
        """
        Call the slot with the arguments and keyword arguments
        """
        raise NotImplementedError
