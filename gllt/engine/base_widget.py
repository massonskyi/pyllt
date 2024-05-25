__all__ = ['BaseWidget']

from abc import ABC, abstractmethod


class BaseWidget(ABC):
    @abstractmethod
    def handle_key_event(self, key, x, y):
        """
        Handle key presses
        """
        raise NotImplementedError

    @abstractmethod
    def handle_mouse_event(self, button, state, x, y):
        """
        Handle mouse
        """
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        """
        Draw the widget on the screen
        """
        raise NotImplementedError
