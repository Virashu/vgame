__all__ = ["Game", "Run", "graphics", "Keys"]

# Hide PyGame welcome message
__import__("os").environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from . import graphics
from .keys import Keys
from .game import Game
from .run import Run
