import math
import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pyllt.gllt.engine.base_widget import BaseWidget
from pyllt.gllt.engine.css_parser import color_to_gl
from pyllt.gllt.widgets.signal import Signal
from OpenGL.GLUT import fonts


class TextBox(BaseWidget):
    def __init__(self, x, y, width, height, css_parser=None, css_class='textbox'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.active = False

        self.text_changed = Signal()
        self.partial_utf8_char = b''  # For handling partial UTF-8 characters
        self.last_time = time.time()

        self.hovered = Signal()
        self.is_hovered = False

        # Default styles
        self.color = color_to_gl((255, 255, 255))
        self.corner_radius = 0
        self.border_color = color_to_gl((0, 0, 0))
        self.border_width = 1
        self.font = fonts.GLUT_BITMAP_HELVETICA_18
        self.font_color = color_to_gl((0, 0, 0))
        self.font_size = 12
        self.margin = 5
        self.padding = 5
        self.base_color = self.color
        self.hover_color = color_to_gl((155, 155, 155))
        self.hover_start_time = None

        # Apply CSS styles if a parser is provided
        if css_parser:
            self.apply_css(css_parser, css_class)

    def handle_mouse_move(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            if not self.is_hovered:
                self.is_hovered = True
                self.hover_start_time = time.time()
                self.hovered.emit()
        else:
            if self.is_hovered:
                self.is_hovered = False
                self.hover_start_time = None

    def handle_mouse_event(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON:
            self.active = self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def apply_css(self, css_parser, css_class):
        styles = css_parser.get_styles(f'.{css_class}')
        if 'color' in styles:
            self.color = color_to_gl(styles['color'])
            self.base_color = color_to_gl(styles['color'])
        if 'border-color' in styles:
            self.border_color = color_to_gl(styles['border-color'])
        if 'border-width' in styles:
            self.border_width = int(styles['border-width'].replace('px', ''))
        if 'font-color' in styles:
            self.font_color = color_to_gl(styles['font-color'])
        if 'font-size' in styles:
            self.font_size = int(styles['font-size'].replace('px', ''))
        if 'margin' in styles:
            self.margin = int(styles['margin'].replace('px', ''))
        if 'padding' in styles:
            self.padding = int(styles['padding'].replace('px', ''))
        if 'corner-radius' in styles:
            self.corner_radius = int(styles['corner-radius'].replace('px', ''))

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
        if self.is_hovered and self.hover_start_time is not None:
            elapsed_time = time.time() - self.hover_start_time
            self.color = self.calculate_wave_color(self.base_color, self.hover_color, elapsed_time)
        else:
            self.color = self.base_color

        # Draw the border
        if self.border_width > 0:
            glColor3f(*self.border_color)
            self.draw_rounded_rect(self.x, self.y, self.width, self.height, self.corner_radius)

        # Draw the button inside the border
        glColor3f(*self.color)
        self.draw_rounded_rect(self.x + self.border_width, self.y + self.border_width,
                               self.width - 2 * self.border_width, self.height - 2 * self.border_width,
                               self.corner_radius)

        # Draw the text inside the button with padding
        self.draw_text(
            self.x + self.padding + self.margin,
            self.y + self.height // 2 - self.font_size // 2,
            self.text
        )

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

    def calculate_wave_color(self, base_color, hover_color, elapsed_time):
        wave_speed = 2  # Adjust wave speed as needed
        wave_intensity = 0.5  # Adjust wave intensity as needed
        wave_phase = math.sin(elapsed_time * wave_speed) * wave_intensity

        new_color = [
            base_color[i] + (hover_color[i] - base_color[i]) * (0.5 * (wave_phase + 1))
            for i in range(3)
        ]
        return tuple(new_color)
