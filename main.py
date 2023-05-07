"""
Galaga game
"""

import pymunk.pygame_util
from game.game_directors import *
import itertools


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Create physics space
space = pymunk.Space()
space.gravity = settings.GRAVITY_X, settings.GRAVITY_Y

# Create game objects
game_object_factory = GameObjectFactory(space)
player = game_object_factory.create_player(Player.STARTING_X, Player.STARTING_Y)
enemies = [game_object_factory.create_enemy(rank, settings.SCREEN_FILE[0]) for rank in settings.SCREEN_RANK[::2]]

# Create screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

# Draw options
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Game directors
game_logic = GameLogic(space, player, enemies)
game_renderer = GameRenderer(screen, space, draw_options)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()

    # Update game state
    game_logic.update(keys)

    # Render game
    game_renderer.render(player, enemies, player.projectiles)

    # Clock
    clock.tick(settings.FRAMES_PER_SECOND)

# Clean up
pygame.quit()
