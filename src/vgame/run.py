import pygame

import copy
import threading

from . import Game


class Run:
    __lock = False

    def __new__(cls, *_, **__):
        if cls.__lock:
            raise Exception("Can only create one instance of class")
        cls.__lock = True
        return object.__new__(cls)

    def __del__(self):
        self.__class__.__lock = False

    def __init__(self, game: Game) -> None:
        self.game: Game = game

        pygame.init()

        self.game.load()

        pygame.display.set_caption(self.game.title)

        self.auto_clear = True
        self.running = True

        self.screen: pygame.Surface = pygame.display.set_mode(
            (self.game.width, self.game.height)
        )
        self.game.graphics.set_surface(self.screen)

        # Snapshot is a completed (fully updated) copy of the game
        self.snapshot: Game = self.game

        self._run()

    def _draw_loop(self):
        clock = pygame.time.Clock()

        while self.running:
            if self.auto_clear:
                self.screen.fill((0, 0, 0))

            self.game.graphics_delta = clock.get_time() / 1000  # ms -> s
            self.game.fps = clock.get_fps()

            self.snapshot.draw()

            pygame.display.flip()

            clock.tick(self.game.framerate)

    def _update_loop(self) -> None:
        update_clock = pygame.time.Clock()

        while self.running:
            self.game.delta = update_clock.get_time() / 1000  # ms -> s
            self.game.tps = update_clock.get_fps()

            self.game.update()

            self.snapshot: Game = copy.deepcopy(self.game)
            self.snapshot.graphics.set_surface(self.screen)

            update_clock.tick(self.game.tickrate)
            self._poll_events()

    def _run(self) -> None:
        draw_loop = threading.Thread(target=self._draw_loop, daemon=True)
        draw_loop.start()

        self._update_loop()

        draw_loop.join()

    def _poll_events(self) -> None:
        for e in pygame.event.get():
            if (
                e.type == pygame.QUIT
                or e.type == pygame.KEYDOWN
                and e.key == pygame.K_q
            ):
                self._stop()
            elif e.type == pygame.KEYDOWN:
                self.game.pressed_keys.add(e.key)
            elif e.type == pygame.KEYUP:
                self.game.pressed_keys.discard(e.key)

    def _stop(self) -> None:
        self.running = False
        self.game.exit()
        pygame.quit()
