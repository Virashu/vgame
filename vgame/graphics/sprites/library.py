"""Sprite texture library class definition"""

import pygame

from vgame.graphics.sprites.types import ISprite, ILibrary


class Library(ILibrary):
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

    def load(self, *sprites: ISprite) -> None:
        """Preload sprite to the library"""
        for sprite in sprites:
            self._add(sprite)

    def _add(self, sprite: ISprite) -> None:
        texture_file, texture_size = sprite.texture_file, sprite.texture_size
        texture = pygame.image.load(self._path + "/" + texture_file)
        rect = texture.get_rect()
        if sprite.texture_size not in ((0, 0), (rect.w, rect.h)):
            texture = pygame.transform.scale(texture, sprite.texture_size)
            rect.w, rect.h = sprite.texture_size

        sprite.set_size(rect)

        resource_name = f"{texture_file}_{texture_size}"

        self._data[resource_name] = texture

    def get(self, target: ISprite) -> pygame.Surface:
        """Get a texture from the library"""
        texture_file, texture_size = target.texture_file, target.texture_size
        texture_id = f"{texture_file}_{texture_size}"

        if texture := self._data.get(texture_id):
            return texture

        self._add(target)

        texture = self._data[texture_id]

        return texture
