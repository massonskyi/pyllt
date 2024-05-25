__all__ = ['BaseSignal']

from typing import List, Callable


class BaseSignal:
    def __init__(self):
        """
        Initialize the signal object
        """
        pass

    def connect(self, slot: object | Callable):
        """
        Connect the slot to the
        """
        raise NotImplementedError

    def emit(self, *args, **kwargs):
        """
        Emit the signal with the arguments
        """
        raise NotImplementedError
