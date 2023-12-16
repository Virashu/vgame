import pygame

from .sprites import Sprite, IGraphics


class Graphics(IGraphics):
    def __init__(self, surface: pygame.Surface | None = None) -> None:
        if surface:
            self.surface = surface

    def set_surface(self, surface: pygame.Surface) -> None:
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

    def polygon(
        self,
        points: tuple[tuple[float, float]],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        pygame.draw.polygon(self.surface, color, points)

    def rectangle(
        self,
        xy: tuple[float, float],
        size: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        pygame.draw.rect(self.surface, color, (xy, size))

    def draw_sprite(self, sprite: Sprite) -> None:
        sprite.draw(self)

    def __deepcopy__(self, _) -> "Graphics":
        return Graphics()
