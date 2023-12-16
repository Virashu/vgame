"""An example Game class implementation"""


from typing import final

from vgame import Game, Run, Keys
from mysprite import MySprite

import pygame


class MyGame(Game):
    @final
    def load(self):
        self.sx, self.sy = 0, 0
        self.speed = 20

        self.sprites = pygame.sprite.Group()
        self.sprites.add(MySprite(self.sx * 20 + 10, self.sy * 20 + 10))

    @final
    def update(self):
        self.print_stats()
        distance = self.speed * self.delta
        if Keys.RIGHT in self.pressed_keys and self.sx <= self.width // 20 - 1:
            self.sx += distance
        if Keys.LEFT in self.pressed_keys and self.sx >= 0:
            self.sx -= distance
        if Keys.DOWN in self.pressed_keys and self.sy <= self.height // 20 - 1:
            self.sy += distance
        if Keys.UP in self.pressed_keys and self.sy >= 0:
            self.sy -= distance

    @final
    def draw(self):
        for i in range(20, self.width, 20):
            self.graphics.line((i, 0), (i, self.height), (100, 100, 100))
        for i in range(20, self.height, 20):
            self.graphics.line((0, i), (self.width, i), (100, 100, 100))

        self.sprites.draw(self.graphics.surface)

    @final
    def exit(self):
        print("\x1b[2J\x1b[0;0H", end="")  # clear screen
        print("Goodbye!")

    def print_stats(self):
        print("\x1b[?25l", end="")  # hide cursor
        print("\x1b[2J\x1b[0;0H", end="")  # clear screen
        print(f"FPS: {self.fps:.2f}")
        print(f"TPS: {self.tps:.2f}")
        print(f"Delta: {self.delta:.4f}")
        print("\x1b[?25h", end="")  # show cursor
        print()


Run(MyGame(width=800, height=600, framerate=120, tickrate=120, title="Test Game"))
