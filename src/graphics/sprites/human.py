from . import Sprite


class Human(Sprite):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __draw__(self, graphics) -> None:
        graphics.circle((self.x, self.y), 10)
        graphics.line((self.x, self.y), (self.x, self.y + 30))
        graphics.line((self.x, self.y + 10), (self.x - 20, self.y + 20))
        graphics.line((self.x, self.y + 10), (self.x + 20, self.y + 20))

        graphics.line((self.x, self.y + 30), (self.x - 20, self.y + 60))
        graphics.line((self.x, self.y + 30), (self.x + 20, self.y + 60))
