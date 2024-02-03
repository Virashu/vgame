"""Package for sprite graphics"""

__all__ = ["Sprite", "Library", "Group"]


from .types import IGraphics, ISprite, ILibrary
from .sprite import Sprite
from .library import Library
from .group import Group
