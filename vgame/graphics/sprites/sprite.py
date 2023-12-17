from abc import abstractmethod

from . import ISprite

from pygame import sprite, rect


class Sprite(ISprite, sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.texture_file: str = ""
        self.texture: str = ""
        self.texture_size: tuple[int, int] = (0, 0)
        self._rect: rect.Rect = rect.Rect(0, 0, 0, 0)

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect.h = rect.h
        self._rect.w = rect.w

    @property
    def image(self):
        return

    def set_texture(self, id: str) -> None:
        self.texture = id

    @abstractmethod
    def update(self, delta: float) -> None:
        ...
