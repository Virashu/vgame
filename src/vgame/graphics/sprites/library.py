import pygame

from . import Sprite


class Library:
    def __init__(self) -> None:
        self._data: dict[str, pygame.Surface] = {}
        self._path: str = ""

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, path: str) -> None:
        self._path = path

    def add(self, sprite: Sprite) -> None:
        texture_name = sprite.texture_file
        texture = pygame.image.load(self._path + "/" + texture_name)
        rect = texture.get_rect()
        if sprite.texture_size not in ((0, 0), (rect.w, rect.h)):
            texture = pygame.transform.scale(texture, sprite.texture_size)
            rect.w, rect.h = sprite.texture_size

        sprite._rect = rect

        resource_name = f"{texture_name}_{hash(texture)}"

        self._data[resource_name] = texture
        sprite.set_texture(resource_name)

    def get(self, name: str) -> pygame.Surface:
        if name not in self._data:
            raise KeyError(f"Texture not found: {name}")
        return self._data[name]
