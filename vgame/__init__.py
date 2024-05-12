"""
VGame is a 2D game engine written in Python
"""

__all__ = [
    "graphics",
    "Keys",
    "Runner",
    "Scene",
    "Axis",
]

# Hide PyGame welcome message
# Should be done before importing any modules that use pygame
# __import__("os").environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from . import graphics
from .axis import Axis
from .keys import Keys
from .runner import Runner
from .scene import Scene
