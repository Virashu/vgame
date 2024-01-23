"""Package for sprite graphics"""

__all__ = [
    "Sprite",
    "Library",
    "Group",
    "IGraphics",
    "ISprite",
]

from abc import abstractmethod
from typing import Sequence

import pygame


class ISprite:
    """Sprite interface"""

    @abstractmethod
    def draw(self, graphics: "IGraphics") -> None:
        """Draw the sprite"""

    @abstractmethod
    def update(self, delta: float) -> None:
        """Update the sprite"""


class IGraphics:
    """Graphics interface"""

    _surface: pygame.Surface
    _library: "Library"

    @property
    def surface(self) -> pygame.Surface:
        ...

    @property
    def library(self) -> "Library":
        ...

    @abstractmethod
    def __init__(self, screen: pygame.Surface) -> None:
        ...

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
    def draw_sprite(self, target: ISprite | Sequence[ISprite]) -> None:
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


from vgame.graphics.sprites.sprite import Sprite
from vgame.graphics.sprites.library import Library
from vgame.graphics.sprites.group import Group
