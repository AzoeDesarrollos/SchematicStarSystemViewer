from backend import Renderer, WidgetHandler, EventHandler
from frontend import Background

bg = Background()


while True:
    EventHandler.process()
    WidgetHandler.update()
    Renderer.update()
