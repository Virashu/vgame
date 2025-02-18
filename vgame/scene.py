"""Definition of abstract class Scene"""

__all__ = ["Scene"]

from abc import abstractmethod

from .graphics import Graphics


class Scene:
    """Abstract scene class

    Arguments:
        width: int
            Width of window

        height: int
            Height of window

        framerate: int
            Frames per second (draw loop)

        tickrate: int
            Ticks per second (update loop)

        title: str
            Title of window

    """

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        framerate: int = 60,
        tickrate: int = 60,
        title: str = "Game",
        *,
        fullscreen: bool = False,
    ) -> None:
        # Window properties
        self.height = height
        self.width = width
        self.framerate = framerate  # for draw() method (graphics)
        self.tickrate = tickrate  # for update() method (backend)
        self.title = title
        self.fullscreen = fullscreen

        # Input
        self.pressed_keys: set[int] = set()  # Keys that are pressed now
        self.clicked_keys: set[int] = set()  # Keys that were pressed
        self.released_keys: set[int] = set()  # Keys that were released

        # Timing
        self.delta: float = 0  # Time delta for tickrate, not framerate; seconds
        self.graphics_delta: float = 0
        self.fps: float = 0
        self.tps: float = 0

        self.graphics = Graphics()
        # Then need to call game.graphics.set_surface(...) from runner

        self.running = True

    def stop(self) -> None:
        """Stop the game"""
        self.running = False
        self.exit()

    def get_click(self, key: int) -> bool:
        """Check if a key was clicked"""
        state = key in self.clicked_keys
        self.clicked_keys.discard(key)
        return state

    def get_release(self, key: int) -> bool:
        """Check if a key was released"""
        state = key in self.released_keys
        self.released_keys.discard(key)
        return state

    @abstractmethod
    def update(self) -> None:
        """Inheritor-defined abstract update method

        Called as frequent as possible

        Can access delta time using `self.delta` variable
        """

    @abstractmethod
    def draw(self) -> None:
        """Inheritor-defined abstract draw method

        Called according to framerate
        """

    @abstractmethod
    def load(self) -> None:
        """Inheritor-defined abstract load method

        Called after main initialization
        """

    @abstractmethod
    def exit(self) -> None:
        """Inheritor-defined abstract exit method

        Called before application close
        """
