import os

from OpenGL.GLUT import glutInit

from gllt.linux.tll_main_window import TllMainWindow
from gllt.linux.widgets.button import Button
from gllt.linux.widgets.label import Label
from gllt.linux.widgets.slot import Slot
from gllt.linux.widgets.textbox import TextBox


def on_submit_clicked():
    print(f"Submitted text: {textbox.text}")


def on_text_changed(new_text):
    print(f"Text changed: {new_text}")


if __name__ == '__main__':
    # Path to the directory containing freeglut.dll
    dll_path = r'/freeglutd.dll'
    os.environ['PATH'] = dll_path + ';' + os.environ['PATH']
    if not glutInit:
        exit(-1)
    # glutInit(sys.argv)
    engine = TllMainWindow("My Custom GUI", 800, 600)
    label = Label(50, 550, "Enter your name:")
    textbox = TextBox(50, 500, 200, 30)
    button = Button(50, 450, 100, 30, "Submit")

    button.clicked.connect(Slot(on_submit_clicked))
    textbox.text_changed.connect(Slot(on_text_changed))

    engine.add_widget(label)
    engine.add_widget(textbox)
    engine.add_widget(button)

    engine.main_loop()
