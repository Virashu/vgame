"""Graphics class definition"""

import copy
from typing import final

import pygame

from .sprites import (
    AbstractGraphics,
    AbstractLibrary,
    AbstractSprite,
)

from .sprites.texture import Texture


class Graphics(AbstractGraphics):
    """Graphics class"""

    def __init__(
        self,
        surface: pygame.Surface | None = None,
        library: AbstractLibrary | None = None,
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
    def library(self) -> AbstractLibrary:
        """Get the sprite library"""
        return self._library

    @library.setter
    def library(self, library: AbstractLibrary) -> None:
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
        color: tuple[int, int, int] | tuple[int, int, int, int] = (255, 255, 255),
    ) -> None:
        if len(color) == 3 or color[3] == 255:
            pygame.draw.rect(self._surface, color, (xy, size))
        else:
            shape_surf = pygame.Surface(pygame.Rect(xy, size).size, pygame.SRCALPHA)
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            self._surface.blit(shape_surf, (xy, size))

    def _draw_textured_sprites(self, *sprites: AbstractSprite) -> None:
        if len(sprites) == 1:
            target: AbstractSprite = sprites[0]
            texture = self._library.get(target)

            self._surface.blit(texture, target.rect)
        else:
            sprites_info = tuple(
                (self._library.get(sprite), sprite.rect) for sprite in sprites
            )
            self._surface.blits(sprites_info)

    @final
    def draw_sprites(self, *sprites: AbstractSprite) -> None:
        _sprites: set[AbstractSprite] = set(sprites)
        textured = set(
            filter(
                lambda s: hasattr(s, "texture") and isinstance(s.texture, Texture),
                _sprites,
            )
        )
        if any(textured):
            self._draw_textured_sprites(*textured)

        non_textured = _sprites - textured

        for sprite in non_textured:
            sprite.draw(self)

    def text(
        self,
        text: str,
        xy: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
        background: tuple[int, int, int] | None = None,
        font_name: str = "Segoe UI",
        font_size: int = 24,
    ):
        if not pygame.font.get_init():
            pygame.font.init()
        font = pygame.font.SysFont(font_name, font_size)
        text_surface = font.render(text, True, color, background)
        self._surface.blit(text_surface, xy)

    def __deepcopy__(self, _) -> "Graphics":
        return copy.copy(self)
