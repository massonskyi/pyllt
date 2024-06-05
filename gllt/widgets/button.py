import math
import time

from OpenGL.GL import glBegin, glEnd
from OpenGL.GLUT import fonts
from OpenGL.raw.GL.VERSION.GL_1_0 import glColor3f, glVertex2f, glRasterPos2f, GL_TRIANGLE_FAN
from OpenGL.raw.GL.VERSION.GL_4_0 import GL_QUADS
from OpenGL.raw.GLUT import GLUT_LEFT_BUTTON, glutBitmapCharacter, GLUT_DOWN, GLUT_UP, glutBitmapWidth

from pyllt.gllt.engine.base_widget import BaseWidget
from .signal import Signal


class Button(BaseWidget):
    def __init__(self, x, y, width, height, text, color=(0, 255, 255), corner_radius=10, border_color=(0.0, 0.0, 0.0),
                 border_width=1, font=fonts.GLUT_BITMAP_HELVETICA_18, font_color=(0, 0, 0), font_size=18, margin=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.corner_radius = corner_radius
        self.border_color = border_color
        self.border_width = border_width
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.margin = margin
        self.clicked = Signal()
        self.hovered = Signal()
        self.is_hovered = False
        self.base_color = color
        self.hover_color = (0.8, 0.8, 1.0)
        self.hover_start_time = None

    def handle_mouse_event(self, button, state, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
                self.clicked.emit()
            elif state == GLUT_UP:
                self.is_hovered = True
        else:
            self.is_hovered = False

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

    def handle_key_event(self, key, x, y):
        pass

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

        self.draw_text(self.x + self.margin+ self.border_width, self.y + self.height // 2 - self.font_size // 2- self.border_width, self.text)

    def draw_text(self, x, y, text):
        glColor3f(0, 0, 0)  # Black color for text
        glRasterPos2f(x, y)
        for char in text:
            glutBitmapCharacter(fonts.GLUT_BITMAP_HELVETICA_18, ord(char))

    def draw_rounded_rect(self, x, y, width, height, radius):
        # Draw the four sides
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

    def draw_corner(self, cx, cy, radius, start_angle, end_angle):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        for angle in range(start_angle, end_angle + 1):
            angle_rad = angle * math.pi / 180.0
            glVertex2f(cx + radius * math.cos(angle_rad), cy + radius * math.sin(angle_rad))
        glEnd()

    def calculate_wave_color(self, base_color, hover_color, elapsed_time):
        # This function calculates the color for the wave effect
        wave_speed = 2.0  # Adjust wave speed as needed
        wave_intensity = 0.5  # Adjust wave intensity as needed
        wave_phase = math.sin(elapsed_time * wave_speed) * wave_intensity

        new_color = [
            base_color[i] + (hover_color[i] - base_color[i]) * (0.5 * (wave_phase + 1))
            for i in range(3)
        ]
        return tuple(new_color)