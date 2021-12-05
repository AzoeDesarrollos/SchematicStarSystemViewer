from .widgets.basewidget import BaseWidget
from backend.contants import WIDTH, HEIGHT
from pygame import image, Rect
from os.path import join
from os import getcwd


class Background(BaseWidget):
    sub_right = None
    sub_left = None
    sub_top = None
    sub_bottom = None
    chunk_x = 0
    chunk_y = 0

    def __init__(self, parent=None):
        self.image_base = image.load(join(getcwd(), 'data', 'estrellas.png'))
        self.image = image.load(join(getcwd(), 'data', 'estrellas.png'))
        self.rect = self.image.get_rect()
        super().__init__(parent)
        self.show()

    def __repr__(self):
        return 'Star Bg'

    def move(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)
        px, py = 0, 0
        r = None
        if 0 < self.rect.x or self.rect.x <= -3500:
            self.chunk_x += dx
            if self.chunk_x > 0:
                x = self.image_base.get_width() - self.chunk_x
                px = dx
                r = Rect(x, 0, abs(dx), self.rect.h)

            elif self.chunk_x < 0:
                px = WIDTH
                r = Rect(-self.chunk_x, 0, abs(dx), self.rect.h)

        elif 0 > self.rect.y or self.rect.bottom >= 600:
            self.chunk_y += dy
            if self.chunk_y > 0:
                y = self.image_base.get_height() - self.chunk_y
                py = 0
                r = Rect(0, y, self.rect.w, abs(dy))

            elif self.chunk_y < 0:
                y = -self.chunk_y
                py = HEIGHT
                r = Rect(0, y, self.rect.w, abs(dy))

        try:
            img = self.image_base.subsurface(r).copy()
        except ValueError:
            self.chunk_x = 0
            self.chunk_y = 0
            if dx != 0:
                r = Rect(0, 0, abs(dx), self.rect.h)
            elif dy != 0:
                r = Rect(0, 0, self.rect.w, abs(dy))
            img = self.image_base.subsurface(r).copy()

        Chunk(self, img, px, py)


class Chunk(BaseWidget):
    def __init__(self, parent, img, x, y):
        super().__init__(parent)
        self.image = img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.show()

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)
