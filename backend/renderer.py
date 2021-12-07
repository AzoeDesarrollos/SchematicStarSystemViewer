from pygame import display, SCALED, image, Rect
from pygame.sprite import LayeredUpdates
from .contants import WIDTH, HEIGHT
from os.path import join
from os import getcwd


class Renderer:
    contenido = None
    bg = None
    rect = None

    @classmethod
    def init(cls):
        cls.contenido = LayeredUpdates()
        display.set_mode([WIDTH, HEIGHT], SCALED)
        cls.bg = image.load(join(getcwd(), 'data', 'estrellas.png'))
        cls.rect = Rect(0, 0, WIDTH, HEIGHT)

    @classmethod
    def add_widget(cls, widget):
        cls.contenido.add(widget)

    @classmethod
    def del_widget(cls, widget):
        cls.contenido.remove(widget)

    @classmethod
    def update(cls):
        fondo = display.get_surface()
        fondo.fill('black')
        rect = cls.contenido.draw(fondo)
        display.update(rect)

    @classmethod
    def contains(cls, item):
        return cls.rect.colliderect(item.rect)


Renderer.init()
