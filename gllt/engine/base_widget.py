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

    @abstractmethod
    def draw_corner(self, cx, cy, radius, start_angle, end_angle):
        """
        Draw a corner on the screen
        """
        raise NotImplementedError

    @abstractmethod
    def draw_rounded_rect(self, x, y, width, height, radius):
        """
        Draw a rounded rectangle on the screen
        """
        raise NotImplementedError

    @abstractmethod
    def draw_text(self, x, y, text):
        """
        Draw text on the screen
        """
        raise NotImplementedError
