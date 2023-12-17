"""An example sprite"""


from vgame.graphics.sprites import Sprite


class MySprite(Sprite):
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.x = x
        self.y = y

        self.texture_file = "test_sprite.png"
        self.texture_size = (32, 32)

        self._rect.x = int(self.x - self._rect.width / 2)
        self._rect.y = int(self.y - self._rect.height / 2)

    def update(self, delta: float) -> None:
        self._rect.x = int(self.x - self._rect.width / 2)
        self._rect.y = int(self.y - self._rect.height / 2)
