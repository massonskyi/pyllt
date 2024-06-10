from gllt.linux.engine.base_widget import BaseWidget


class Label(BaseWidget):
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def handle_mouse_event(self, button, state, x, y):
        pass

    def handle_key_event(self, key, x, y):
        pass

    def draw(self):
        # Placeholder for text rendering
        pass
