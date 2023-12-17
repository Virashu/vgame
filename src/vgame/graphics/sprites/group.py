import pygame
from pygame.surface import Surface

from . import Sprite, Library, IGraphics


class Group(pygame.sprite.Group):
    def draw(self, graphics: IGraphics, special_flags: int = 0) -> list[pygame.Rect]:
        surface: Surface = graphics.surface
        sprites: list[Sprite] = self.sprites()
        lib: Library = graphics.library

        if hasattr(surface, "blits"):
            sprites_iter = tuple(
                (lib.get(spr.texture), spr.rect, None, special_flags) for spr in sprites
            )
            rects = surface.blits(sprites_iter) # type: ignore
            if rects:
                self.spritedict.update(zip(sprites, rects))
        else:
            for spr in sprites:
                rect = surface.blit(lib.get(spr.texture), spr.rect, None, special_flags)
                self.spritedict[spr] = rect

        self.lostsprites = []
        dirty = self.lostsprites

        return dirty
