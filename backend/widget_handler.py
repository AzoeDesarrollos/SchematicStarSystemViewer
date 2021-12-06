from pygame.sprite import LayeredUpdates
from pygame import event, QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame import MOUSEMOTION
from .eventhandler import EventHandler


class WidgetHandler:
    contenido = None

    @classmethod
    def init(cls):
        cls.contenido = LayeredUpdates()

    @classmethod
    def add_widget(cls, widget):
        cls.contenido.add(widget)

    @classmethod
    def del_widget(cls, widget):
        cls.contenido.remove(widget)

    @classmethod
    def update(cls):
        events = event.get([QUIT, KEYDOWN, KEYUP, MOUSEMOTION])
        event.clear()
        dx, dy = 0, 0
        for ev in events:
            if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                EventHandler.trigger('quit', 'WidgetHandler', {'message': 'normal'})

            elif ev.type == KEYUP:
                if ev.key == K_UP or ev.key == K_DOWN:
                    dy = 0
                elif ev.key == K_LEFT or ev.key == K_DOWN:
                    dx = 0

            elif ev.type == KEYDOWN:
                if ev.key == K_UP:
                    dy = +100

                elif ev.key == K_DOWN:
                    dy = -100

                elif ev.key == K_LEFT:
                    dx = +100

                elif ev.key == K_RIGHT:
                    dx = -100
            elif ev.type == MOUSEMOTION:
                if any(ev.buttons):
                    dx, dy = ev.rel

        if dx or dy:
            for widget in cls.contenido.sprites():
                widget.move(dx, dy)

        cls.contenido.update()


WidgetHandler.init()
