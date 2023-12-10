from . import Sprite, IGraphics


class Circle(Sprite):
    def __init__(self, x: float, y: float, r: float) -> None:
        self.r = r
        self.x = x
        self.y = y

    def draw(self, graphics: IGraphics) -> None:
        graphics.circle((self.x, self.y), self.r)
