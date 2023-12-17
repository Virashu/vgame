import pygame

from .sprites import Sprite, IGraphics, Library
import copy

from typing import Sequence


class Graphics(IGraphics):
    def __init__(
        self, surface: pygame.Surface | None = None, library: Library | None = None
    ) -> None:
        if surface:
            self._surface = surface
        if library:
            self._library = library

    @property
    def surface(self) -> pygame.Surface:
        return self._surface

    @surface.setter
    def surface(self, surface: pygame.Surface) -> None:
        self._surface = surface

    @property
    def library(self) -> Library:
        return self._library

    @library.setter
    def library(self, library: Library) -> None:
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
    ) -> None:
        pygame.draw.rect(self._surface, color, (xy, size))

    def draw_sprite(self, target: Sprite | Sequence[Sprite]) -> None:
        if isinstance(target, Sprite):
            texture = self._library._data[target.texture]
            rect = target.rect

            self._surface.blit(texture, rect)
        elif isinstance(target, Sequence):
            self._surface.blits(
                [
                    (self._library._data[sprite.texture], sprite.rect)
                    for sprite in target
                ]
            )
        else:
            raise ValueError(f"Unsupported type: {type(target)}")

    def __deepcopy__(self, _) -> "Graphics":
        return copy.copy(self)
