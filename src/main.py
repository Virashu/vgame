import framework as game
from graphics.sprites import Human


sx = sy = 0

for r in game.run():
    delta, pressed_keys = r

    # Draw grid
    for i in range(20, game.width, 20):
        game.graphics.line((i, 0), (i, game.height), (100, 100, 100))

    for i in range(20, game.height, 20):
        game.graphics.line((0, i), (game.width, i), (100, 100, 100))

    # Draw circle
    # game.graphics.circle((game.sx * 20 + 10, game.sy * 20 + 10), 10)
    game.graphics.draw_sprite(Human(sx * 20 + 10, sy * 20 + 10))

    # Movement
    if 79 in pressed_keys and sx < game.width // 20 - 1:
        sx += 1
    if 80 in pressed_keys and sx > 0:
        sx -= 1
    if 81 in pressed_keys and sy < game.height // 20 - 1:
        sy += 1
    if 82 in pressed_keys and sy > 0:
        sy -= 1
print("Goodbye!")
