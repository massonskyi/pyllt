import math

from pyllt.gllt.engine.css_parser import CSSParser, color_to_gl
from pyllt.gllt.tll_main_window import TllMainWindow
from pyllt.gllt.widgets.button import Button
from pyllt.gllt.widgets.label import Label
from pyllt.gllt.widgets.slot import Slot
from pyllt.gllt.widgets.textbox import TextBox

i = 0


def on_submit_clicked():
    global i
    i += 1
    text_box3.text = f"Counter: {i}"
    text_box2.text = f"Counter: {i + 1}"
    text_box1.text = f"Counter: {i + 2}"
    text_box.text = f"Counter: {i + 3}"


def on_text_changed(new_text):
    print(f"Text changed: {new_text}")


# Создание CSS-парсера
css_parser = CSSParser('/home/user064/repo/pyrepo/pyllt/pyllt/gllt/styles/main.css')
engine = TllMainWindow("My Custom GUI", 800, 600)

label = Label(50, 450, 200, 50, "Counters", css_parser=css_parser)
text_box = TextBox(50, 50, 200, 50, css_parser=css_parser)
text_box1 = TextBox(50, 150, 200, 50, css_parser=css_parser)
text_box2 = TextBox(50, 250, 200, 50, css_parser=css_parser)
text_box3 = TextBox(50, 350, 200, 50, css_parser=css_parser)
button = Button(450, 350, 200, 50, "Click Me", css_parser=css_parser)

button.clicked.connect(Slot(on_submit_clicked))
text_box.text_changed.connect(Slot(on_text_changed))
text_box1.text_changed.connect(Slot(on_text_changed))
text_box2.text_changed.connect(Slot(on_text_changed))
text_box3.text_changed.connect(Slot(on_text_changed))

engine.add_widget(label)
engine.add_widget(text_box)
engine.add_widget(text_box1)
engine.add_widget(text_box2)
engine.add_widget(text_box3)
engine.add_widget(button)

engine.main_loop()
