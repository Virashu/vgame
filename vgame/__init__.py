"""
VGame is a 2D game engine written in Python
"""

__all__ = ["Scene", "Runner", "graphics", "Keys"]

# Hide PyGame welcome message
# Should be done before importing any modules that use pygame
# __import__("os").environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from vgame import graphics
from vgame.keys import Keys
from vgame.scene import Scene
from vgame.runner import Runner
