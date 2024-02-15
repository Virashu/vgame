"""Interface classes"""

from abc import ABC, abstractmethod
from typing import Sequence

import pygame


class IGraphics(ABC):
    """Graphics interface"""

    _surface: pygame.Surface
    _library: "ILibrary"

    @property
    def surface(self) -> pygame.Surface:
        """Get the graphics surface"""
        return self._surface

    @property
    def library(self) -> "ILibrary":
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
    def draw_sprite(self, target: "ISprite" | Sequence["ISprite"]) -> None:
        """Draw a sprite"""

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


class ISprite:
    """Sprite interface"""

    texture_size: tuple[int, int]
    texture_file: str
    rect: pygame.Rect

    @abstractmethod
    def set_size(self, rect: pygame.Rect) -> None:
        """Set the sprite size"""

    @abstractmethod
    def draw(self, graphics: "IGraphics") -> None:
        """Draw the sprite"""

    @abstractmethod
    def update(self, delta: float) -> None:
        """Update the sprite"""


class ILibrary:
    """Sprite texture library"""

    _path: str
    _data: dict[str, pygame.Surface]

    @property
    def path(self) -> str:
        """Get the path to the sprite images"""
        return self._path

    @path.setter
    def path(self, path: str) -> None:
        """Set the path to the sprite images"""
        self._path = path

    @abstractmethod
    def load(self, *sprites: ISprite) -> None:
        """Preload sprite to the library"""

    @abstractmethod
    def _add(self, sprite: ISprite) -> None: ...

    @abstractmethod
    def get(self, target: ISprite) -> pygame.Surface:
        """Get a texture from the library"""
