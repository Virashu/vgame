"""An example sprite"""

from vgame.graphics.sprites import TexturedSprite, AbstractGraphics


class MySprite(TexturedSprite):
    def __init__(self, x: float, y: float, w: int, h: int) -> None:
        super().__init__(
            "test_sprite.png",
            (w, h),
        )

        self.x = x
        self.y = y

        self._rect.x = int(self.x - self._rect.width / 2)
        self._rect.y = int(self.y - self._rect.height / 2)

    def update(self, delta: float) -> None:
        self._rect.x = int(self.x - self._rect.width / 2)
        self._rect.y = int(self.y - self._rect.height / 2)

    def draw(self, graphics: AbstractGraphics) -> None:
        graphics.draw_sprites(self)
