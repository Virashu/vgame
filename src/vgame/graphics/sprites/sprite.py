from abc import abstractmethod
from . import ISprite, IGraphics


class Sprite(ISprite):
    @abstractmethod
    def draw(self, graphics: IGraphics) -> None:
        ...

    @abstractmethod
    def update(self, delta: float) -> None:
        ...
