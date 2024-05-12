"""Sprite texture library class definition"""

import logging

import pygame

from .typing import AbstractLibrary, AbstractTexturedSprite

logger = logging.getLogger(__name__)


class Library(AbstractLibrary):
    """Sprite texture library"""

    def __init__(self) -> None:
        self.path: str = ""
        self.save_originals: bool = False

        self._data: dict[str, pygame.Surface] = {}
        self._originals: dict[str, pygame.Surface] = {}

    def load(self, *sprites: AbstractTexturedSprite) -> None:
        """Preload sprite to the library"""
        for sprite in sprites:
            if sprite in self:
                continue

            self._add(sprite)

    def _add(self, sprite: AbstractTexturedSprite) -> None:
        texture_file, texture_size = (
            sprite.texture.file,
            sprite.texture.size,
        )

        logger.info("Loading texture %s %s", texture_file, texture_size)

        texture = pygame.image.load(self.path + "/" + texture_file)
        rect = texture.get_rect()

        if sprite.texture.size not in ((0, 0), (rect.w, rect.h)):
            texture = pygame.transform.scale(texture, sprite.texture.size)
            rect.w, rect.h = sprite.texture.size

        sprite.set_size(rect)

        resource_name = sprite.texture.id

        self._data[resource_name] = texture

    def __contains__(self, sprite: AbstractTexturedSprite) -> bool:
        return sprite.texture.id in self._data

    def get(
        self, target: AbstractTexturedSprite, refresh: bool = False
    ) -> pygame.Surface:
        """Get a texture from the library"""
        texture_id = target.texture.id

        if (not refresh) and (texture := self._data.get(texture_id)):
            return texture

        self._add(target)

        texture = self._data[texture_id]

        return texture


class LibDirectoryNotFoundError(BaseException): ...
