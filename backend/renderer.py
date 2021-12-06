from pygame.sprite import LayeredUpdates
from .contants import WIDTH, HEIGHT
from pygame import display, SCALED, image
from os.path import join
from os import getcwd


class Renderer:
    contenido = None
    bg = None

    @classmethod
    def init(cls):
        cls.contenido = LayeredUpdates()
        display.set_mode([WIDTH, HEIGHT], SCALED)
        cls.bg = image.load(join(getcwd(), 'data', 'estrellas.png'))

    @classmethod
    def add_widget(cls, widget):
        cls.contenido.add(widget)

    @classmethod
    def del_widget(cls, widget):
        cls.contenido.remove(widget)

    @classmethod
    def update(cls):
        fondo = display.get_surface()
        fondo.fill('red')
        rect = cls.contenido.sprites()[0].chunks.draw(fondo)
        display.update(rect)


Renderer.init()
