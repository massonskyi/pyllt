from OpenGL.raw.GL.VERSION.GL_1_0 import glColor3f, glBegin, GL_QUADS, glVertex2f, glEnd
from OpenGL.raw.GLUT import GLUT_LEFT_BUTTON

from gllt.engine.base_widget import BaseWidget
from gllt.widgets.signal import Signal


class TextBox(BaseWidget):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.active = False
        self.text_changed = Signal()

    def handle_mouse_event(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            self.active = self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def handle_key_event(self, key, x, y):
        if self.active:
            if key == b'\x08':  # Backspace
                self.text = self.text[:-1]
            else:
                self.text += key.decode()
            self.text_changed.emit(self.text)

    def draw(self):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()
        # Placeholder for text rendering
