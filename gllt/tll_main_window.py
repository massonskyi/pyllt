import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pyllt.gllt.engine.base_widget import BaseWidget


class TllMainWindow:
    def __init__(self, title, width, height, color=(1.0, 1.0, 1.0)):
        self.width = width
        self.height = height
        self.widgets = []
        self.color = color

        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow(title.encode("ascii"))
        glutDisplayFunc(self.render)
        glutIdleFunc(self.render)
        glutKeyboardFunc(self.key_pressed)
        glutMouseFunc(self.mouse_clicked)
        glutPassiveMotionFunc(self.mouse_moved)

    def add_widget(self, widget: BaseWidget):
        self.widgets.append(widget)

    def main_loop(self):
        glutMainLoop()

    def render(self):
        glClearColor(*self.color, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glOrtho(0, self.width, 0, self.height, -1, 1)

        for widget in self.widgets:
            widget.draw()

        glutSwapBuffers()
        error = glGetError()
        if error != GL_NO_ERROR:
            print(f"OpenGL error during render: {gluErrorString(error)}")

    def key_pressed(self, key, x, y):
        for widget in self.widgets:
            widget.handle_key_event(key, x, y)

    def mouse_clicked(self, button, state, x, y):
        if state == GLUT_DOWN:
            for widget in self.widgets:
                widget.handle_mouse_event(button, state, x, self.height - y)

    def mouse_moved(self, x, y):
        for widget in self.widgets:
            widget.handle_mouse_move(x, self.height - y)