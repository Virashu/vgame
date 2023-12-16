from abc import abstractmethod


from .graphics import Graphics


class Game:
    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        framerate: int = 60,
        tickrate: int = 60,
        title: str = "Game",
    ) -> None:
        self.height = height
        self.width = width
        self.framerate = framerate  # for draw() method (graphics)
        self.tickrate = tickrate  # for update() method (backend)
        self.title = title

        self.pressed_keys: set = set()
        self.delta: float = 0  # Time delta for tickrate, not framerate; seconds

        # ?
        self.graphics_delta: float = 0
        self.fps: float = 0
        self.tps: float = 0

        self.graphics = Graphics()
        # Then need to call game.graphics.set_surface(...) from runner

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
