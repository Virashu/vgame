"""An example Game class implementation"""


from typing import final

from vgame import Scene, Runner, Keys
from vgame.graphics.sprites import Group

from mysprite import MySprite


class MyGame(Scene):
    @final
    def load(self):
        # Directory with textures
        self.graphics.library.path = __file__.replace("\\", "/").rsplit("/", 1)[0]

        self.sx, self.sy = 0, 0
        self.sx1, self.sy1 = 0, 0

        self.speed = 20

        self.sprite = MySprite(20, 20, 30, 70)
        self.sprite1 = MySprite(50, 50, 100, 100)

        self.graphics.library.load(self.sprite, self.sprite1)

        self.group = Group(self.sprite1, self.sprite)

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

        if Keys.D in self.pressed_keys and self.sx1 <= self.width // 20 - 1:
            self.sx1 += distance
        if Keys.A in self.pressed_keys and self.sx1 >= 0:
            self.sx1 -= distance
        if Keys.S in self.pressed_keys and self.sy1 <= self.height // 20 - 1:
            self.sy1 += distance
        if Keys.W in self.pressed_keys and self.sy1 >= 0:
            self.sy1 -= distance

        if Keys.Q in self.pressed_keys:
            self.stop()

        self.sprite.x = self.sx * 20 + 10
        self.sprite.y = self.sy * 20 + 10

        self.sprite1.x = self.sx1 * 20 + 10
        self.sprite1.y = self.sy1 * 20 + 10

        self.group.update(self.delta)

    @final
    def draw(self):
        for i in range(20, self.width, 20):
            self.graphics.line((i, 0), (i, self.height), (100, 100, 100))
        for i in range(20, self.height, 20):
            self.graphics.line((0, i), (self.width, i), (100, 100, 100))

        self.graphics.draw_sprite((self.sprite, self.sprite1))
        self.group.draw(self.graphics)

    @final
    def exit(self):
        print("\x1b[2J\x1b[0;0H", end="")  # clear screen
        print("Goodbye!")

    def print_stats(self):
        print("\x1b[?25l", end="")  # hide cursor
        print("\x1b[2J\x1b[0;0H", end="")  # clear screen
        print(f"FPS:\t{self.fps:.2f}")
        print(f"TPS:\t{self.tps:.2f}")
        print(f"Delta:\t{self.delta:.4f}")
        print("\x1b[?25h", end="")  # show cursor
        print()


class TitleScreen(Scene):
    @final
    def load(self):
        ...

    @final
    def update(self):
        if Keys.RETURN in self.pressed_keys:
            self.stop()

    def draw(self):
        self.graphics.circle((self.width // 2, self.height // 2), 20, (255, 255, 255))


runner = Runner()
runner.run(TitleScreen())
runner.run(
    MyGame(width=800, height=600, framerate=120, tickrate=120, title="Test Game")
)
