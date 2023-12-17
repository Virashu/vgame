from abc import abstractmethod

from . import ISprite

from pygame import sprite


class Sprite(ISprite, sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def update(self, delta: float) -> None:
        ...
