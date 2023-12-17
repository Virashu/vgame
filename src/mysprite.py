"""An example sprite"""


from vgame.graphics.sprites import Sprite, IGraphics
from vgame.graphics import load_image, make_copyable_surface
import pygame


class MySprite_shapes(Sprite):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def draw_shapes(self, graphics: IGraphics) -> None:
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


class MySprite(Sprite):
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.x = x
        self.y = y

        # 🩼🩼🩼

        # self.image = load_image("test_sprite.jpg")
        # self.image = make_copyable_surface(
        #     pygame.transform.scale(self.image, (100, 100))
        # )

        self.image = pygame.image.load("test_sprite.jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = int(self.x - self.rect.width / 2)
        self.rect.y = int(self.y - self.rect.height / 2)

    def update(self, delta: float) -> None:
        self.rect.x = int(self.x - self.rect.width / 2)
        self.rect.y = int(self.y - self.rect.height / 2)
