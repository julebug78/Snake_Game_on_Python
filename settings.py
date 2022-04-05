import pygame

# window
WIDTH = 680
HEIGHT = 680
TILE_SIZE = 40
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 10
SNAKE_SPEED = 1

# Colors (R, G, B)
# Define colors
AQUA = pygame.Color(66, 224, 245)
SNAKE_GREEN = pygame.Color(66, 245, 147)
PURPLE = pygame.Color(216, 172, 230)
DK_PURPLE = pygame.Color(111, 32, 176)
BLUEBERRY = pygame.Color(38, 60, 224)
WHITE = pygame.Color(255, 255, 255)
YELLOW = pygame.Color(234, 240, 134)
SNAKE_BODY = pygame.Color(105, 157, 240)
APPLE_RED = pygame.Color(207, 8, 8)
BANANA = pygame.Color(219, 187, 70)
LIME = pygame.Color(41, 255, 76)
BLACK = pygame.Color(0, 0, 0)

pygame.font.init()
FONT = pygame.font.SysFont('arial', 20)
