import pygame


class Surface(pygame.Surface):
    def __deepcopy__(self, memo):
        return self.copy()
