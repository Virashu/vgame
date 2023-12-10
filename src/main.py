"""An example Game class implementation"""


from typing import final

from vgame import Game

from mysprite import MySprite


class MyGame(Game):
    @final
    def load(self):
        self.sx, self.sy = 0, 0
        self.speed = 20

    @final
    def update(self):
        distance = self.speed * self.delta
        if 79 in self.pressed_keys and self.sx < self.width // 20 - 1:
            self.sx += distance
        if 80 in self.pressed_keys and self.sx > 0:
            self.sx -= distance
        if 81 in self.pressed_keys and self.sy < self.height // 20 - 1:
            self.sy += distance
        if 82 in self.pressed_keys and self.sy > 0:
            self.sy -= distance

    @final
    def draw(self):
        for i in range(20, self.width, 20):
            self.graphics.line((i, 0), (i, self.height), (100, 100, 100))
        for i in range(20, self.height, 20):
            self.graphics.line((0, i), (self.width, i), (100, 100, 100))

        # self.graphics.circle((self.sx * 20 + 10, self.sy * 20 + 10), 10)
        self.graphics.draw_sprite(MySprite(self.sx * 20 + 10, self.sy * 20 + 10))

    @final
    def exit(self):
        print("Goodbye!")


game = MyGame(width=800, height=600, framerate=120, tickrate=120, title="Test Game")
game.run()
