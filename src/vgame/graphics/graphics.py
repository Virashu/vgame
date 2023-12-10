import pygame

from .sprites import Sprite, IGraphics


class Graphics(IGraphics):
    def __init__(self, surface: pygame.Surface) -> None:
        self.surface = surface

    def circle(
        self,
        xy: tuple[float, float],
        r: float,
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        pygame.draw.circle(self.surface, color, xy, r)

    def line(
        self,
        start: tuple[float, float],
        end: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        pygame.draw.line(self.surface, color, start, end)

    def draw_sprite(self, sprite: Sprite) -> None:
        sprite.draw(self)
