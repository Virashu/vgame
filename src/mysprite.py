"""An example sprite"""


from vgame.graphics.sprites import Sprite, IGraphics


class MySprite(Sprite):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def draw(self, graphics: IGraphics) -> None:
        graphics.line(
            (self.x - 10, self.y - 10),
            (self.x, self.y),
        )
        graphics.line(
            (self.x + 10, self.y - 10),
            (self.x, self.y),
        )

        graphics.circle((self.x, self.y), 10)

        graphics.line((self.x, self.y), (self.x, self.y + 30))

        graphics.line((self.x, self.y + 10), (self.x - 20, self.y + 20))
        graphics.line((self.x, self.y + 10), (self.x + 20, self.y + 20))

        graphics.line((self.x, self.y + 30), (self.x - 20, self.y + 60))
        graphics.line((self.x, self.y + 30), (self.x + 20, self.y + 60))
