import pygame

from graphics import Graphics

width, height, framerate = 800, 600, 120
auto_clear = True

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
graphics = Graphics(screen)


def run():
    running = True
    # load()

    while running:
        pressed_keys = tuple(i for i, k in enumerate(pygame.key.get_pressed()) if k)

        delta = clock.get_time()

        if auto_clear:
            screen.fill((0, 0, 0))

        # draw()

        yield delta, pressed_keys

        pygame.display.flip()

        clock.tick(framerate)
        for e in pygame.event.get():
            if (
                e.type == pygame.QUIT
                or e.type == pygame.KEYDOWN
                and e.key == pygame.K_q
            ):
                # self.exit()
                pygame.quit()
                running = False


class Game:
    def __init__(
        self, width: int = 800, height: int = 600, framerate: int = 60
    ) -> None:
        self.height = height
        self.width = width
        self.framerate = framerate

        self.delta: int = 0

        self.pressed_keys = ()
