from OpenGL.raw.GL.VERSION.GL_1_0 import glColor3f, glBegin, GL_QUADS, glVertex2f, glEnd
from OpenGL.raw.GLUT import GLUT_LEFT_BUTTON

from gllt.engine.base_widget import BaseWidget
from .signal import Signal


class Button(BaseWidget):
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = Signal()

    def handle_mouse_event(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.clicked.emit()

    def handle_key_event(self, key, x, y):
        pass

    def draw(self):
        glColor3f(0.8, 0.8, 0.8)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()
        # Placeholder for text rendering
