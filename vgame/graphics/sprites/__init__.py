"""Package for sprite graphics"""

__all__ = ["Sprite", "Library", "Group"]


from vgame.graphics.sprites.types import IGraphics, ISprite, ILibrary
from vgame.graphics.sprites.sprite import Sprite
from vgame.graphics.sprites.library import Library
from vgame.graphics.sprites.group import Group
