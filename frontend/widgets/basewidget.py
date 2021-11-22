from backend import Renderer, WidgetHandler
from pygame.sprite import Sprite


class BaseWidget(Sprite):
    is_visible = True

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if parent is not None:
            self.layer = self.parent.layer + 1

    def on_mousebutton_down(self, event):
        pass

    def on_mousebutton_up(self, event):
        pass

    def on_keydown(self, event):
        pass

    def on_keyup(self, event):
        pass

    def on_mousemotion(self, event):
        pass

    def on_mouseover(self):
        pass

    def show(self):
        self.is_visible = True
        Renderer.add_widget(self)
        WidgetHandler.add_widget(self)

    def hide(self):
        self.is_visible = False
        Renderer.del_widget(self)
        WidgetHandler.del_widget(self)
