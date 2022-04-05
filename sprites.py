import pygame.sprite
import random

from settings import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x, self. y = x, y
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(SNAKE_BODY)
        self.rect = self.image.get_rect()

    def body_hit(self):
        if self.x == self.game.head.x and self.y == self.game.head.y:
            return True
        return False

    def update(self):
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUEBERRY)  # Makes the blueberry solid blue
        # Next two codes make the blueberry show up in random places on the screen
        self.rect.x = random.randrange((WIDTH - self.rect.width))
        self.rect.y = random.randrange(HEIGHT - self.rect.width)

    def respawn(self):  # Fruit respawns after it is eaten to another random location
        self.rect.x = random.randrange((WIDTH - self.rect.width))
        self.rect.y = random.randrange((HEIGHT - self.rect.width))

    def update(self):
        pass
