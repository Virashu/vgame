import pygame

from graphics.sprites import Sprite


class Graphics:
    def __init__(self, screen) -> None:
        self.screen = screen

    def circle(
        self, xy: tuple[int, int], r: int, color: tuple[int, int, int] = (255, 255, 255)
    ):
        pygame.draw.circle(self.screen, color, xy, r)

    def line(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        pygame.draw.line(self.screen, color, start, end)

    def draw_sprite(self, sprite: Sprite) -> None:
        sprite.__draw__(self)
