"""Sprite group class definition"""

import pygame

from .typing import AbstractGraphics, AbstractSprite


class Group(pygame.sprite.Group):
    """Sprite group class"""

    def draw(self, graphics: AbstractGraphics, special_flags: int = 0) -> None:
        """Draw all sprites in group"""
        sprites: list[AbstractSprite] = self.sprites()

        if hasattr(graphics.surface, "blits"):
            sprites_iter = tuple(
                (graphics.library.get(spr), spr.rect, None, special_flags)
                for spr in sprites
            )
            rects = graphics.surface.blits(sprites_iter)  # type: ignore
            if rects:
                self.spritedict.update(zip(sprites, rects))
        else:
            for spr in sprites:
                rect = graphics.surface.blit(
                    graphics.library.get(spr), spr.rect, None, special_flags
                )
                self.spritedict[spr] = rect
