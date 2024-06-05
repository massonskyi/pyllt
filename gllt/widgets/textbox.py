import math
import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pyllt.gllt.engine.base_widget import BaseWidget
from pyllt.gllt.widgets.signal import Signal
from OpenGL.GLUT import fonts


class TextBox(BaseWidget):
    def __init__(self, x, y, width, height, color=(1.0, 1.0, 1.0), corner_radius=10,
                 font=fonts.GLUT_BITMAP_HELVETICA_18, font_color=(0, 0, 0), font_size=18, margin=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.active = False
        self.color = color
        self.corner_radius = corner_radius
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.margin = margin
        self.text_changed = Signal()
        self.partial_utf8_char = b''  # For handling partial UTF-8 characters
        self.last_time = time.time()

    def handle_mouse_move(self, x, y):
        pass

    def handle_mouse_event(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            self.active = self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def handle_key_event(self, key, x, y):
        if self.active:
            if key == b'\x08':  # Backspace
                self.text = self.text[:-1]
            else:
                try:
                    utf8_char = (self.partial_utf8_char + key).decode('utf-8')
                    self.text += utf8_char
                    self.partial_utf8_char = b''
                except UnicodeDecodeError:
                    self.partial_utf8_char += key
            self.text_changed.emit(self.text)

    def draw(self):
        glColor3f(*self.color)
        self.draw_rounded_rect(self.x, self.y, self.width, self.height, self.corner_radius)

        self.draw_text(self.x + self.margin, self.y + self.height // 2 - self.font_size // 2, self.text)

        if self.active:
            self.draw_caret(self.x + self.margin + self.get_text_width(self.text),
                            self.y + self.height // 2 - self.font_size // 2)

    def draw_rounded_rect(self, x, y, width, height, radius):
        glBegin(GL_QUADS)
        glVertex2f(x + radius, y)
        glVertex2f(x + width - radius, y)
        glVertex2f(x + width - radius, y + height)
        glVertex2f(x + radius, y + height)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(x, y + radius)
        glVertex2f(x + radius, y + radius)
        glVertex2f(x + radius, y + height - radius)
        glVertex2f(x, y + height - radius)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(x + width - radius, y + radius)
        glVertex2f(x + width, y + radius)
        glVertex2f(x + width, y + height - radius)
        glVertex2f(x + width - radius, y + height - radius)
        glEnd()

        # Draw the four corners
        self.draw_corner(x + radius, y + radius, radius, 180, 270)
        self.draw_corner(x + width - radius, y + radius, radius, 270, 360)
        self.draw_corner(x + width - radius, y + height - radius, radius, 0, 90)
        self.draw_corner(x + radius, y + height - radius, radius, 90, 180)

    def draw_text(self, x, y, text):
        glColor3f(*self.font_color)  # Set font color
        glRasterPos2f(x, y)
        for char in text:
            glutBitmapCharacter(self.font, ord(char))

    def draw_caret(self, x, y):
        current_time = time.time()
        if int(current_time - self.last_time) % 2 == 0:
            glColor3f(*self.font_color)  # Use font color for caret
            glBegin(GL_LINES)
            glVertex2f(x, y)
            glVertex2f(x, y + self.font_size)
            glEnd()

    def get_text_width(self, text):
        width = 0
        for char in text:
            width += glutBitmapWidth(self.font, ord(char))
        return width

    def draw_corner(self, cx, cy, radius, start_angle, end_angle):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        for angle in range(start_angle, end_angle + 1):
            angle_rad = angle * math.pi / 180.0
            glVertex2f(cx + radius * math.cos(angle_rad), cy + radius * math.sin(angle_rad))
        glEnd()
