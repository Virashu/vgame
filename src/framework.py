import pygame

import sys
from abc import abstractmethod
from typing import Callable, final

import graphics


clock = pygame.time.Clock()
_lock = [False]


class Game:
    def __init__(
        self, width: int = 800, height: int = 600, framerate: int = 60
    ) -> None:
        if _lock[0]:
            raise Exception("Can only create one instance of class")
        _lock[0] = True
        self.height = height
        self.width = width
        self.framerate = framerate

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.graphics = graphics.Graphics(self.screen)
        self.delta: int = 0
        self.auto_clear = True
        self.pressed_keys = ()

    @abstractmethod
    def update(self):
        # Not implemented: Need multithreading 😕
        ...

    @abstractmethod
    def draw(self):
        ...

    @abstractmethod
    def load(self):
        ...

    @abstractmethod
    def exit(self):
        ...

    @final
    def run(self):
        self.load()

        while True:
            self._poll_events()
            self.pressed_keys = tuple(
                i for i, k in enumerate(pygame.key.get_pressed()) if k
            )

            self.delta = clock.get_time()

            if self.auto_clear:
                self.screen.fill((0, 0, 0))

            self.draw()
            pygame.display.flip()

            clock.tick(self.framerate)

    def _poll_events(self):
        for e in pygame.event.get():
            if (
                e.type == pygame.QUIT
                or e.type == pygame.KEYDOWN
                and e.key == pygame.K_q
            ):
                self.exit()
                pygame.quit()
                sys.exit()
