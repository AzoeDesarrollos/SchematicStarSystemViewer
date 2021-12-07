from pygame import event, QUIT, KEYDOWN, K_ESCAPE
from pygame.sprite import LayeredUpdates
from .eventhandler import EventHandler
from pygame import MOUSEMOTION


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
    def cap(cls, n):
        if n != 0:
            val = abs(n)
            sign = n / n
            if val >= 500:
                n = 500 * sign
        return n

    @classmethod
    def update(cls):
        events = event.get([QUIT, KEYDOWN, MOUSEMOTION])
        event.clear()
        dx, dy = 0, 0
        for ev in events:
            if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                EventHandler.trigger('quit', 'WidgetHandler', {'message': 'normal'})

            if ev.type == MOUSEMOTION:
                if any(ev.buttons):
                    dx, dy = ev.rel
                    dx = cls.cap(dx)
                    dy = cls.cap(dy)

        if dx or dy:
            for widget in cls.contenido.sprites():
                widget.move(dx, dy)

        cls.contenido.update()


WidgetHandler.init()
