"""An example Game class implementation"""

from typing import final

from vgame import Scene, Runner, Keys, Axis
from vgame.graphics.sprites import Group

from mysprite import MySprite


class MyGame(Scene):
    @final
    def load(self):
        # Directory with textures
        self.graphics.library.path = __file__.replace("\\", "/").rsplit("/", 1)[0]

        self.sx1, self.sy1 = 0, 0
        self.sx2, self.sy2 = 0, 0

        self.speed = 400

        self.sprite1 = MySprite(20, 20, 30, 70)
        self.s1x = Axis(Keys.LEFT, Keys.RIGHT)
        self.s1y = Axis(Keys.UP, Keys.DOWN)

        self.sprite2 = MySprite(50, 50, 100, 100)
        self.s2x = Axis(Keys.A, Keys.D)
        self.s2y = Axis(Keys.W, Keys.S)

        self.graphics.library.load(self.sprite1, self.sprite2)

        self.group = Group(self.sprite1, self.sprite2)

    @final
    def update(self):
        self.print_stats()

        self.s1x.update(self.pressed_keys)
        self.s1y.update(self.pressed_keys)

        self.s2x.update(self.pressed_keys)
        self.s2y.update(self.pressed_keys)

        distance = self.speed * self.delta

        self.sx1 += self.s1x.axis * distance
        self.sy1 += self.s1y.axis * distance

        self.sx2 += self.s2x.axis * distance
        self.sy2 += self.s2y.axis * distance

        # clamp
        self.sx1 = max(0, min(self.width - self.sprite1.rect.w, self.sx1))
        self.sy1 = max(0, min(self.height - self.sprite1.rect.h, self.sy1))

        self.sx2 = max(0, min(self.width - self.sprite2.rect.w, self.sx2))
        self.sy2 = max(0, min(self.height - self.sprite2.rect.h, self.sy2))

        if self.get_click(Keys.ESCAPE):
            self.stop()

        self.sprite1.x = self.sx1 + 10
        self.sprite1.y = self.sy1 + 10

        self.sprite2.x = self.sx2 + 10
        self.sprite2.y = self.sy2 + 10

        self.group.update(self.delta)

    @final
    def draw(self):
        for i in range(20, self.width, 20):
            self.graphics.line((i, 0), (i, self.height), (100, 100, 100))
        for i in range(20, self.height, 20):
            self.graphics.line((0, i), (self.width, i), (100, 100, 100))

        self.group.draw(self.graphics)

        self.graphics.text("Hello, world!", (0, 0))

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
    def load(self): ...

    @final
    def update(self):
        if self.get_click(Keys.RETURN):
            self.stop()

    @final
    def draw(self):
        self.graphics.circle((self.width // 2, self.height // 2), 20, (255, 255, 255))


runner = Runner()
runner.run(TitleScreen())
runner.run(
    MyGame(
        width=800,
        height=600,
        framerate=120,
        tickrate=120,
        title="Test Game",
        fullscreen=False,
    )
)
