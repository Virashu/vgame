import pygame

import copy
import threading

from . import Game
from .graphics.sprites import Library


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

        self.library = Library()
        self.game.graphics.library = self.library
        self.game.load()

        pygame.display.set_caption(self.game.title)

        self.auto_clear = True
        self.running = True

        self.screen: pygame.Surface = pygame.display.set_mode(
            (self.game.width, self.game.height)
        )

        # Snapshot is a completed (fully updated) copy of the game
        self._snapshot: Game = self.game

        self._snapshot_update_event = threading.Event()

        self.game.graphics.surface = self.screen

        self._run()

    def _draw_loop(self):
        clock = pygame.time.Clock()

        while self.running:
            self._snapshot_update_event.wait()
            snapshot = self._snapshot
            self._snapshot_update_event.clear()

            if self.auto_clear:
                self.screen.fill((0, 0, 0))

            self.game.graphics_delta = snapshot.graphics_delta = (
                clock.get_time() / 1000
            )  # ms -> s
            self.game.fps = snapshot.fps = clock.get_fps()

            snapshot.draw()

            pygame.display.flip()

            clock.tick(self.game.framerate)

    def _update_loop(self) -> None:
        update_clock = pygame.time.Clock()

        while self.running:
            self.game.delta = update_clock.get_time() / 1000  # ms -> s
            self.game.tps = update_clock.get_fps()

            self.game.update()

            if not self._snapshot_update_event.is_set():
                self._snapshot: Game = copy.deepcopy(self.game)
                # self._snapshot.graphics.set_surface(self.screen)
                self._snapshot_update_event.set()

            update_clock.tick(self.game.tickrate)
            self._poll_events()

    def _run(self) -> None:
        self._draw_loop_thread = threading.Thread(target=self._draw_loop, daemon=True)
        self._draw_loop_thread.start()

        self._update_loop()

        self._draw_loop_thread.join()

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
        self._snapshot_update_event.set()
        self.running = False
        self.game.exit()
        pygame.quit()
