from . import Surface
import pygame


def load_image(path: str) -> pygame.Surface:
    image = pygame.image.load(path)
    sur = Surface(image.get_rect().size)
    sur.blit(image, (0, 0))
    return sur


def make_copyable_surface(surface: pygame.Surface) -> pygame.Surface:
    res = Surface(surface.get_rect().size)
    res.blit(surface, (0, 0))
    return res
