"""Interface classes"""

from __future__ import annotations

__all__ = [
    "AbstractGraphics",
    "AbstractLibrary",
    "AbstractSprite",
    "AbstractTexturedSprite",
]

from abc import ABC, abstractmethod

from .texture import Texture

import pygame


class AbstractGraphics(ABC):
    """Graphics interface"""

    _surface: pygame.Surface
    _library: AbstractLibrary

    @property
    def surface(self) -> pygame.Surface:
        """Get the graphics surface"""
        return self._surface

    @property
    def library(self) -> AbstractLibrary:
        """Get the sprite library"""
        return self._library

    @abstractmethod
    def __init__(self, screen: pygame.Surface) -> None: ...

    @abstractmethod
    def circle(
        self,
        xy: tuple[float, float],
        r: float,
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        """Draw a circle"""

    @abstractmethod
    def line(
        self,
        start: tuple[float, float],
        end: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        """Draw a line"""

    @abstractmethod
    def polygon(
        self,
        points: tuple[tuple[float, float]],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        """Draw a polygon"""

    @abstractmethod
    def rectangle(
        self,
        xy: tuple[float, float],
        size: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        """Draw a rectangle"""

    @abstractmethod
    def text(
        self,
        text: str,
        xy: tuple[float, float],
        color: tuple[int, int, int] = (255, 255, 255),
        background: tuple[int, int, int] | None = None,
        font_name: str = "Segoe UI",
        font_size: int = 24,
    ):
        """Draw a text string"""

    @abstractmethod
    def draw_sprites(self, *sprites: AbstractSprite) -> None:
        """Draw a sprite"""


class AbstractLibrary(ABC):
    """Sprite texture library"""

    path: str

    _data: dict[str, pygame.Surface]

    @abstractmethod
    def load(self, *sprites: AbstractTexturedSprite) -> None:
        """Preload sprite to the library"""

    @abstractmethod
    def _add(self, sprite: AbstractTexturedSprite) -> None: ...

    @abstractmethod
    def get(self, target: AbstractTexturedSprite) -> pygame.Surface:
        """Get a texture from the library"""


class AbstractSprite(ABC):
    """Sprite interface"""

    _rect: pygame.Rect

    @abstractmethod
    def set_size(self, rect: pygame.Rect) -> None:
        """Set the sprite size"""

    @abstractmethod
    def draw(self, graphics: AbstractGraphics) -> None:
        """Draw the sprite"""

    @abstractmethod
    def update(self, delta: float) -> None:
        """Inheritor-defined abstract update method"""

    @property
    @abstractmethod
    def rect(self) -> pygame.Rect:
        """Get the sprite rect"""


class AbstractTexturedSprite(AbstractSprite, ABC):
    """Textured sprite interface"""

    texture: Texture
