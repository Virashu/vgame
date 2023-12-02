from abc import abstractmethod


class Sprite:
    @abstractmethod
    def __draw__(self, graphics) -> None:
        ...
