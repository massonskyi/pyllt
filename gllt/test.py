from pyllt.gllt.tll_main_window import TllMainWindow
from pyllt.gllt.widgets.button import Button
from pyllt.gllt.widgets.label import Label
from pyllt.gllt.widgets.slot import Slot
from pyllt.gllt.widgets.textbox import TextBox

i = 0


def on_submit_clicked():
    global i
    i += 1
    text_box.text = f"Counter: {i}"


def on_hover():
    print("Hover")


def on_text_changed(new_text):
    print(f"Text changed: {new_text}")


engine = TllMainWindow("My Custom GUI", 800, 600)
# label = Label(50, 550, "Enter your name:")
text_box = TextBox(300, 300, 200, 50, color=(0, 255, 255), corner_radius=15, font_color=(0, 0, 0), font_size=18)
button = Button(50, 50, 200, 200, text="Click Me", color=(0, 255, 255),
                corner_radius=45, border_color=(0, 0, 0), border_width=1, font_color=(255, 100, 0), font_size=2,
                margin=29)
button.hovered.connect(Slot(on_hover))
button.clicked.connect(Slot(on_submit_clicked))
text_box.text_changed.connect(Slot(on_text_changed))

# engine.add_widget(label)
engine.add_widget(text_box)
engine.add_widget(button)

engine.main_loop()
