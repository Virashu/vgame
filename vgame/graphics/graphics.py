"""Graphics class definition"""

import copy
from typing import Sequence

import pygame

from .sprites import Sprite, IGraphics, ILibrary


class Graphics(IGraphics):
    """Graphics class"""

    def __init__(
        self, surface: pygame.Surface | None = None, library: ILibrary | None = None
    ) -> None:
        if surface:
            self._surface = surface
        if library:
            self._library = library

    @property
    def surface(self) -> pygame.Surface:
        """Get the graphics surface"""
        return self._surface

    @surface.setter
    def surface(self, surface: pygame.Surface) -> None:
        """Set the graphics surface"""
        self._surface = surface

    @property
    def library(self) -> ILibrary:
        """Get the sprite library"""
        return self._library

    @library.setter
    def library(self, library: ILibrary) -> None:
        """Set the sprite library"""
        self._library = library

    def circle(
        self,
        xy: tuple[float, float],
        r: float,
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        pygame.draw.circle(self._surface, color, xy, r)

    def line(
        self,
        start: tuple[float, float],
        end: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        pygame.draw.line(self._surface, color, start, end)

    def polygon(
        self,
        points: tuple[tuple[float, float]],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        pygame.draw.polygon(self._surface, color, points)

    def rectangle(
        self,
        xy: tuple[float, float],
        size: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
        alpha: int = 255,
    ) -> None:
        if alpha == 255:
            pygame.draw.rect(self._surface, color, (xy, size))
        else:
            shape_surf = pygame.Surface(pygame.Rect(xy, size).size, pygame.SRCALPHA)
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            self._surface.blit(shape_surf, (xy, size))

    def draw_sprite(self, target: Sprite | Sequence[Sprite]) -> None:
        if isinstance(target, Sprite):
            texture = self._library.get(target)

            self._surface.blit(texture, target.rect)
        else:
            self._surface.blits(
                [(self._library.get(sprite), sprite.rect) for sprite in target]
            )

    def text(
        self,
        text: str,
        xy: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
        background: tuple[int, int, int] | None = None,
        font_name: str = "Segoe UI",
    ):
        if not pygame.font.get_init():
            pygame.font.init()
        font = pygame.font.SysFont(font_name, 30)
        text_surface = font.render(text, True, color, background)
        self._surface.blit(text_surface, xy)

    def __deepcopy__(self, _) -> "Graphics":
        return copy.copy(self)
