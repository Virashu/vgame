"""Scene runner class definition"""

import copy
import pathlib
import threading

import pygame
import pygame.constants as pg_constants

from .graphics.sprites import LibDirectoryNotFoundError, Library
from .scene import Scene
from .singleton import Singleton


class Runner(Singleton):
    """Scene runner class"""

    def __init__(self) -> None:
        self.auto_clear = True
        self._snapshot_update_event = threading.Event()

        pygame.init()

        self.scene: Scene
        self.screen: pygame.Surface
        self._snapshot: Scene

        self.running = True

    def run(self, scene: Scene) -> None:
        """Run a scene"""
        if not self.running:
            return

        self.scene = scene

        self.scene.graphics.library = Library()
        self.scene.load()

        if not pathlib.Path(self.scene.graphics.library.path).exists():
            msg = (
                "Sprite library path does not exist or not set: "
                f"{self.scene.graphics.library.path}\n"
                "Please use:\n"
                '\tself.graphics.library.path = "<path>"'
            )
            raise LibDirectoryNotFoundError(msg)

        pygame.display.set_caption(self.scene.title)

        self._run()

    def _draw_loop(self) -> None:
        clock = pygame.time.Clock()

        screen_flags = 0
        screen_flags |= pygame.constants.FULLSCREEN if self.scene.fullscreen else 0

        self.screen = pygame.display.set_mode(
            (self.scene.width, self.scene.height), flags=screen_flags
        )

        # Snapshot is a completed (fully updated) copy of the game
        self._snapshot = self.scene

        self.scene.graphics.surface = self.screen

        self._poll_events()
        while self.scene.running:
            if self._snapshot_update_event.is_set():
                snapshot = self._snapshot
                self._snapshot_update_event.clear()

                if self.auto_clear:
                    self.screen.fill((0, 0, 0))

                self.scene.graphics_delta = snapshot.graphics_delta = (
                    clock.get_time() / 1000
                )  # ms -> s
                self.scene.fps = snapshot.fps = clock.get_fps()

                snapshot.draw()

                pygame.display.flip()

            self._poll_events()
            clock.tick(self.scene.framerate)

    def _update_loop(self) -> None:
        update_clock = pygame.time.Clock()

        while self.scene.running:
            self.scene.delta = update_clock.get_time() / 1000  # ms -> s
            self.scene.tps = update_clock.get_fps()

            self.scene.update()

            if not self._snapshot_update_event.is_set():
                self._snapshot = copy.deepcopy(self.scene)

                # self._snapshot.graphics.set_surface(self.screen)
                self._snapshot_update_event.set()

            update_clock.tick(self.scene.tickrate)

    def _run(self) -> None:
        # draw_thread = threading.Thread(target=self._draw_loop, daemon=True)
        # draw_thread.start()
        update_thread = threading.Thread(target=self._update_loop, daemon=True)
        update_thread.start()

        # self._update_loop()
        self._draw_loop()

        # draw_thread.join()
        update_thread.join()

    def _poll_events(self) -> None:
        for e in pygame.event.get():
            if e.type == pg_constants.QUIT:
                self._stop()

            elif e.type == pg_constants.KEYDOWN:
                self.scene.pressed_keys.add(e.key)
                self.scene.clicked_keys.add(e.key)

            elif e.type == pg_constants.KEYUP:
                self.scene.pressed_keys.discard(e.key)
                self.scene.released_keys.add(e.key)

            # elif e.type == pg_constants.

    def _stop(self) -> None:
        self._snapshot_update_event.set()
        self.scene.stop()
        self.scene.exit()
        self.running = False
        pygame.quit()
