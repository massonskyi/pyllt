__all__ = ['BaseWidget']

from abc import ABC, abstractmethod
from OpenGL.GL import glBegin, glEnd
from OpenGL.GLUT import fonts
from OpenGL.raw.GL.VERSION.GL_1_0 import glColor3f, glVertex2f, glRasterPos2f, GL_TRIANGLE_FAN
from OpenGL.raw.GL.VERSION.GL_4_0 import GL_QUADS
from OpenGL.raw.GLUT import GLUT_LEFT_BUTTON, glutBitmapCharacter, GLUT_DOWN, GLUT_UP, glutBitmapWidth


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
    def handle_mouse_move(self, x, y):
        """
        Handle mouse move
        """
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        """
        Draw the widget on the screen
        """
        raise NotImplementedError

    @abstractmethod
    def apply_css(self, css_parser, css_class):
        """
        Apply CSS to the widget
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
