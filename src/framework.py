import pygame
import sys

from graphics import Graphics

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))


def Game():
    delta = 0
    pressed_keys = ()
    draw, load, exit = None, None, None
    graphics = Graphics(screen)

    def get_graphics():
        return graphics

    def set_draw(new_draw):
        nonlocal draw
        draw = new_draw

    def set_load(new_load):
        nonlocal load
        load = new_load

    def set_exit(new_exit):
        nonlocal exit
        exit = new_exit

    def get_pressed_keys():
        return pressed_keys

    def get_delta():
        return delta

    def run():
        nonlocal draw, load, exit, delta, pressed_keys

        if load:
            load()

        while True:
            delta = clock.get_time()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    if exit:
                        exit()
                    pygame.quit()
                    sys.exit()
            screen.fill((0, 0, 0))
            pressed_keys = tuple(i for i, k in enumerate(pygame.key.get_pressed()) if k)
            if draw:
                draw()
            pygame.display.flip()
            clock.tick(60)

    return {
        "get_graphics": get_graphics,
        "set_draw": set_draw,
        "set_load": set_load,
        "set_exit": set_exit,
        "get_pressed_keys": get_pressed_keys,
        "get_delta": get_delta,
        "run": run,
    }
