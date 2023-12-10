__all__ = [
    "Sprite",
    "Circle",
    "Human",
]
import pygame


class ISprite:
    def draw(self, graphics: "IGraphics") -> None:
        ...

    def update(self, delta: float) -> None:
        ...


class IGraphics:
    def __init__(self, screen: pygame.Surface) -> None:
        ...

    def circle(
        self,
        xy: tuple[float, float],
        r: float,
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        ...

    def line(
        self,
        start: tuple[float, float],
        end: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        ...

    def draw_sprite(self, sprite: ISprite) -> None:
        ...


from .sprite import Sprite
from .circle import Circle
from .human import Human
