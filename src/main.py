from framework import Game
from graphics.sprites import Human
from constants import *


def MyGame():
    game = Game()
    sx, sy = 0, 0

    def load():
        print("Hello!")

    def draw():
        nonlocal sx, sy
        graphics = game["get_graphics"]()

        # Draw grid
        for i in range(20, 800, 20):
            graphics.line((i, 0), (i, 600), (100, 100, 100))

        for i in range(20, 600, 20):
            graphics.line((0, i), (800, i), (100, 100, 100))

        # Draw circle
        graphics.draw_sprite(Human(sx * 20 + 10, sy * 20 + 10))

        pressed_keys = game["get_pressed_keys"]()

        # Movement
        if 79 in pressed_keys and sx < 800 // 20 - 1:
            sx += 1
        if 80 in pressed_keys and sx > 0:
            sx -= 1
        if 81 in pressed_keys and sy < 600 // 20 - 1:
            sy += 1
        if 82 in pressed_keys and sy > 0:
            sy -= 1

    def exit():
        print("Goodbye!")

    game["set_draw"](draw)
    game["set_load"](load)
    game["set_exit"](exit)

    return game


game = MyGame()
game["run"]()
