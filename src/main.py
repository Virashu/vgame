"""An example Game class implementation"""


from typing import final

from vgame import Game, Run, Keys
from mysprite import MySprite


class MyGame(Game):
    @final
    def load(self):
        self.sx, self.sy = 0, 0
        self.speed = 20

    @final
    def update(self):
        distance = self.speed * self.delta
        if Keys.RIGHT in self.pressed_keys and self.sx < self.width // 20 - 1:
            self.sx += distance
        if Keys.LEFT in self.pressed_keys and self.sx > 0:
            self.sx -= distance
        if Keys.DOWN in self.pressed_keys and self.sy < self.height // 20 - 1:
            self.sy += distance
        if Keys.UP in self.pressed_keys and self.sy > 0:
            self.sy -= distance

    @final
    def draw(self):
        for i in range(20, self.width, 20):
            self.graphics.line((i, 0), (i, self.height), (100, 100, 100))
        for i in range(20, self.height, 20):
            self.graphics.line((0, i), (self.width, i), (100, 100, 100))

        self.graphics.draw_sprite(MySprite(self.sx * 20 + 10, self.sy * 20 + 10))

    @final
    def exit(self):
        print("Goodbye!")


Run(MyGame(width=800, height=600, framerate=30, tickrate=120, title="Test Game"))
