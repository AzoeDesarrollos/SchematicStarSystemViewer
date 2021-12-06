from pygame.sprite import LayeredUpdates
from .contants import WIDTH, HEIGHT
from pygame import display, SCALED


class Renderer:
    contenido = None

    @classmethod
    def init(cls):
        cls.contenido = LayeredUpdates()
        display.set_mode([WIDTH, HEIGHT], SCALED)

    @classmethod
    def add_widget(cls, widget):
        cls.contenido.add(widget)

    @classmethod
    def del_widget(cls, widget):
        cls.contenido.remove(widget)

    @classmethod
    def update(cls):
        fondo = display.get_surface()
        fondo.fill((0, 0, 0))
        rect = cls.contenido.sprites()[0].chunks.draw(fondo)
        display.update(rect)


Renderer.init()
