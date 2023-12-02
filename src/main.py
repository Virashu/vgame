from typing import final
from framework import Game


class MyGame(Game):
    @final
    def load(self):
        self.sx, self.sy = 0, 0

    @final
    def draw(self):
        # Draw grid
        for i in range(20, self.width, 20):
            self.graphics.line((i, 0), (i, self.height), (100, 100, 100))

        for i in range(20, self.height, 20):
            self.graphics.line((0, i), (self.width, i), (100, 100, 100))

        # Draw circle
        self.graphics.circle((self.sx * 20 + 10, self.sy * 20 + 10), 10)

        # Movement
        if 79 in self.pressed_keys and self.sx < self.width // 20 - 1:
            self.sx += 1
        if 80 in self.pressed_keys and self.sx > 0:
            self.sx -= 1
        if 81 in self.pressed_keys and self.sy < self.height // 20 - 1:
            self.sy += 1
        if 82 in self.pressed_keys and self.sy > 0:
            self.sy -= 1

    @final
    def exit(self):
        print("Goodbye!")


game = MyGame(width=800, height=600, framerate=120)
game.run()
