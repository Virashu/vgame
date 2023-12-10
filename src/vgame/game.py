# Hide PyGame welcome message
__import__("os").environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from abc import abstractmethod
import typing as t
import threading


from . import graphics


class Game:
    __lock = False

    def __new__(cls, *_, **__) -> t.Self:
        if cls.__lock:
            raise Exception("Can only create one instance of class")
        cls.__lock = True
        return object.__new__(cls)

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        framerate: int = 60,
        tickrate: int = 60,
        title: str = "Game",
    ) -> None:
        # Pygame init
        pygame.init()
        pygame.display.set_caption(title)

        # Variables
        self.height: int = height
        self.width: int = width
        self.framerate: int = framerate  # for draw() method (graphics)
        self.tickrate: int = tickrate  # for update() method (backend)
        self.running = True
        self.auto_clear = True

        self.screen: pygame.Surface = pygame.display.set_mode((width, height))

        self.graphics = graphics.Graphics(self.screen)

        # Future variables
        self.pressed_keys: tuple = ()
        self.delta: float = 0  # Time delta for tickrate, not framerate; seconds

    @abstractmethod
    def update(self):
        """Inheritor-defined abstract update method

        Called as frequent as possible

        Can access delta time using `self.delta` variable
        """
        ...

    @abstractmethod
    def draw(self):
        """Inheritor-defined abstract draw method

        Called according to framerate
        """
        ...

    @abstractmethod
    def load(self):
        """Inheritor-defined abstract load method

        Called after main initialization
        """
        ...

    @abstractmethod
    def exit(self):
        """Inheritor-defined abstract exit method

        Called before application close
        """
        ...

    def _draw_loop(self):
        clock = pygame.time.Clock()

        while self.running:
            if self.auto_clear:
                self.screen.fill((0, 0, 0))

            self.draw()

            pygame.display.flip()
            clock.tick(self.framerate)

    def _update_loop(self):
        clock = pygame.time.Clock()

        while self.running:
            self._poll_events()
            self.pressed_keys = tuple(
                i for i, k in enumerate(pygame.key.get_pressed()) if k
            )

            # pygame's get_time() method returns time in milliseconds for some reason
            self.delta = clock.get_time() / 1000  # ms -> s

            self.update()

            clock.tick(self.tickrate)

    @t.final
    def run(self):
        self.load()

        # update_loop = threading.Thread(target=self._update_loop, daemon=True)
        draw_loop = threading.Thread(target=self._draw_loop, daemon=True)

        # update_loop.start()
        draw_loop.start()

        self._update_loop()

        # update_loop.join()
        draw_loop.join()

    def _poll_events(self):
        for e in pygame.event.get():
            if (
                e.type == pygame.QUIT
                or e.type == pygame.KEYDOWN
                and e.key == pygame.K_q
            ):
                self._stop()

    def _stop(self):
        self.exit()
        self.running = False
        pygame.quit()
