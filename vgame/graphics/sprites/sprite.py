"""Abstract sprite class definition"""

from abc import abstractmethod

from pygame import Rect
from pygame.sprite import Sprite as PygameSprite

from .texture import Texture
from .typing import AbstractSprite, AbstractTexturedSprite


class Sprite(AbstractSprite, PygameSprite):
    """Base sprite class"""

    def __init__(self) -> None:
        super().__init__()

        self._rect: Rect = Rect(0, 0, 0, 0)

    @property
    def rect(self) -> Rect:
        """Get sprite position and size"""
        return self._rect

    def set_rect(self, rect: Rect) -> None:
        """Set sprite position and size"""
        self._rect = rect

    def set_size(self, rect: Rect) -> None:
        """Set sprite size"""
        self._rect.h = rect.h
        self._rect.w = rect.w

    @abstractmethod
    def update(self, delta: float) -> None:
        """Inheritor-defined abstract update method"""


class TexturedSprite(AbstractTexturedSprite, Sprite):
    """Textured sprite class"""

    def __init__(self, texture_file: str, texture_size: tuple[int, int]) -> None:
        super().__init__()

        self.texture = Texture(texture_file, texture_size)
