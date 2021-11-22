from .widgets.basewidget import BaseWidget
from pygame import image, Rect, Surface
from os.path import join
from os import getcwd


class Background(BaseWidget):
    sub_right = None
    sub_left = None
    sub_top = None
    sub_bottom = None

    def __init__(self, parent=None):
        self.image_base = image.load(join(getcwd(), 'data', 'estrellas.png'))
        self.image = image.load(join(getcwd(), 'data', 'estrellas.png'))
        self.rect = self.image.get_rect()
        self.sub_top = Rect(0, 0, 1000, 0)
        self.sub_bottom = Rect(0, 0, 1000, 0)
        self.sub_left = Rect(0, 0, 0, 600)
        self.sub_right = Rect(0, 0, 0, 600)

        super().__init__(parent)
        self.show()

    def __repr__(self):
        return 'Star Bg'

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)
        if self.rect.x < - 3500:
            r = Rect(0, 0, abs(dx), self.rect.h)
            img = self.image_base.subsurface(r)
            canvas = Surface(self.rect.size)
            canvas.fill('white')
            canvas.blit(self.image_base, (dx, 0))
            canvas.blit(img, (self.rect.w, 0))
            self.image = canvas
