"""Sprite texture library class definition"""

import pygame

from vgame.graphics.sprites import Sprite


class Library:
    """Sprite texture library"""

    def __init__(self) -> None:
        self._data: dict[str, pygame.Surface] = {}
        self._path: str = ""

    @property
    def path(self) -> str:
        """Get the path to the sprite images"""
        return self._path

    @path.setter
    def path(self, path: str) -> None:
        """Set the path to the sprite images"""
        self._path = path

    def add(self, *sprites: Sprite) -> None:
        """Add a sprite to the library"""
        for sprite in sprites:
            self._add(sprite)

    def _add(self, sprite: Sprite) -> None:
        texture_name = sprite.texture_file
        texture = pygame.image.load(self._path + "/" + texture_name)
        rect = texture.get_rect()
        if sprite.texture_size not in ((0, 0), (rect.w, rect.h)):
            texture = pygame.transform.scale(texture, sprite.texture_size)
            rect.w, rect.h = sprite.texture_size

        sprite.set_size(rect)

        resource_name = f"{texture_name}_{hash(texture)}"

        self._data[resource_name] = texture
        sprite.set_texture(resource_name)

    def get(self, name: str) -> pygame.Surface:
        """Get a sprite from the library"""
        if name not in self._data:
            raise KeyError(f"Texture not found: {name}")
        return self._data[name]
