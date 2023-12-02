from graphics.sprites import Sprite


class Circle(Sprite):
    def __init__(self, x, y, r) -> None:
        self.r = r
        self.x = x
        self.y = y

    def __draw__(self, graphics) -> None:
        graphics.circle((self.x, self.y), self.r)
