from .widgets.basewidget import BaseWidget
from backend.contants import WIDTH, HEIGHT
from pygame.sprite import LayeredUpdates
from pygame import image, Surface
from random import choice
from os.path import join
from os import getcwd


class Background(BaseWidget):
    layer = 0
    chunk_x = 0
    chunk_y = 0

    def __init__(self, parent=None):
        self.image_base = image.load(join(getcwd(), 'data', 'estrellas.png'))
        imagen = image.load(join(getcwd(), 'data', 'estrellas.png'))
        chunk = Chunk(self, imagen)
        self.chunks = LayeredUpdates(chunk)

        super().__init__(parent)
        self.show()

    def __repr__(self):
        return 'Star Bg'

    def move(self, dx=0, dy=0):
        if dx < 0:
            # if not self.chunks.get_sprites_at([WIDTH, 0]):
            chunk_image = self.select_chunk(width=dx)
            self.chunks.add(Chunk(self, chunk_image, right=WIDTH))
        if dx > 0:
            # if not self.chunks.get_sprites_at([-dx, 0]):
            chunk_image = self.select_chunk(width=dx)
            self.chunks.add(Chunk(self, chunk_image, left=0))
        if dy < 0:
            # if not self.chunks.get_sprites_at([0, HEIGHT]):
            chunk_image = self.select_chunk(height=dy)
            self.chunks.add(Chunk(self, chunk_image, bottom=HEIGHT))
        if dy > 0:
            # if not self.chunks.get_sprites_at([0, -dy]):
            chunk_image = self.select_chunk(height=dy)
            self.chunks.add(Chunk(self, chunk_image, top=0))

    def select_chunk(self, width=WIDTH, height=HEIGHT):
        w = abs(width)
        h = abs(height)
        choices_h = [self.image_base.subsurface(i, 0, w, h) for i in range(0, WIDTH, w)]
        choices_v = [self.image_base.subsurface(0, i, w, h) for i in range(0, HEIGHT, h)]
        chosen = None
        if width != WIDTH:
            chosen = choice(choices_h)
        elif height != HEIGHT:
            chosen = choice(choices_v)

        return chosen


class Chunk(BaseWidget):
    def __init__(self, parent, img, **kwargs):
        super().__init__(parent)
        imag = Surface(img.get_rect().size)
        imag.blit(img, (0, 0))
        self.image = imag
        self.rect = self.image.get_rect(**kwargs)
        self.show()

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)
