from gllt.tll_main_window import TllMainWindow
from gllt.widgets.button import Button
from gllt.widgets.label import Label
from gllt.widgets.slot import Slot
from gllt.widgets.textbox import TextBox


def on_submit_clicked():
    print(f"Submitted text: {textbox.text}")


def on_text_changed(new_text):
    print(f"Text changed: {new_text}")


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
