"""
VGame is a 2D game engine written in Python
"""

__all__ = ["Game", "Run", "graphics", "Keys"]

# Hide PyGame welcome message
# Should be done before importing any modules that use pygame
__import__("os").environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from vgame import graphics
from vgame.keys import Keys
from vgame.game import Game
from vgame.run import Run
