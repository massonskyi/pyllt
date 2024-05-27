from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from gllt.linux.engine.base_widget import BaseWidget
from gllt.linux.widgets.signal import Signal
from OpenGL.GLUT import fonts


class TextBox(BaseWidget):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.active = False
        self.text_changed = Signal()
        self.partial_utf8_char = b''  # For handling partial UTF-8 characters

    def handle_mouse_event(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            self.active = self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def handle_key_event(self, key, x, y):
        if self.active:
            if key == b'\x08':  # Backspace
                self.text = self.text[:-1]
            else:
                try:
                    # Handle potential multi-byte UTF-8 characters
                    utf8_char = (self.partial_utf8_char + key).decode('utf-8')
                    self.text += utf8_char
                    self.partial_utf8_char = b''
                except UnicodeDecodeError:
                    # If a multi-byte character is not fully received, store it
                    self.partial_utf8_char += key
            self.text_changed.emit(self.text)

    def draw(self):
        glColor3f(1, 1, 1)

        # Проверка ошибок перед вызовом glBegin
        error = glGetError()
        if error != GL_NO_ERROR:
            print(f"OpenGL error before glBegin: {gluErrorString(error)}")

        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()

        # Проверка ошибок после вызова glEnd
        error = glGetError()
        if error != GL_NO_ERROR:
            print(f"OpenGL error after glEnd: {gluErrorString(error)}")
            # Draw text inside the box
        self.draw_text(self.x + 5, self.y + self.height - 15, self.text)

    def draw_text(self, x, y, text):
        glColor3f(0, 0, 0)  # Black color for text
        glRasterPos2f(x, y)
        for char in text:
            glutBitmapCharacter(fonts.GLUT_BITMAP_HELVETICA_18, ord(char))
