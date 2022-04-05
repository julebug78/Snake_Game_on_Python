from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Game by Mrs. Griffiths')
        self.running = True
        self.playing = True
        self.score_value = 0
        self.font_name = pygame.font.match_font('arial')
        self.all_sprites = pygame.sprite.Group()
        self.head = Snake(self, 5, 5)
        self.fruit = Fruit()
        self.direction = 'right'
        self.vx = 0
        self.vy = 0
        self.snake_parts = []

    def new(self):
        self.score_value = 0
        self.all_sprites.add(self.head)
        self.snake_parts.append(Snake(self, 4, 5))
        self.snake_parts.append(Snake(self, 3, 5))
        self.all_sprites.add(self.fruit)

    def run(self):  # Game Loop
        while self.playing:
            CLOCK.tick(FPS)
            self.events()
            self.updates()
            self.draw()

    def events(self):
        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not self.direction == 'down':
                        self.direction = 'up'
                if event.key == pygame.K_DOWN:
                    if not self.direction == 'up':
                        self.direction = 'down'
                if event.key == pygame.K_LEFT:
                    if not self.direction == 'right':
                        self.direction = 'left'
                if event.key == pygame.K_RIGHT:
                    if not self.direction == 'left':
                        self.direction = 'right'

            #  If head reaches edge of screen or 'wall', game ends.
            if self.head.rect.right > WIDTH or self.head.rect.left < 0:
                self.head.kill()
                self.show_game_over_screen()

            #  Second part of code. Code was too long for one line.
            if self.head.rect.top < 0 or self.head.rect.bottom > HEIGHT:
                self.head.kill()
                self.show_game_over_screen()

            #  check to see if snake hits itself
            for body in self.snake_parts:
                if body.body_hit():
                    self.playing = False

    def draw(self):
        SCREEN.fill(PURPLE)
        self.all_sprites.draw(SCREEN)
        self.draw_grid()
        self.draw_score()
        pygame.display.flip()

    def updates(self):
        # Check for if snake eats fruit
        if self.head.rect.colliderect(self.fruit):
            self.score_value += 5
            self.snake_parts.append(Snake(self, self.snake_parts[-1].x, self.snake_parts[-1].y))
            self.fruit.respawn()

        # Update all sprites
        self.all_sprites.update()

        #  Track and move the body parts
        x, y = self.head.x, self.head.y
        for body in self.snake_parts:
            temp_x, temp_y = body.x, body.y
            body.x, body.y = x, y
            x, y = temp_x, temp_y

        if self.direction == 'right':
            self.head.x += 1
        elif self.direction == 'up':
            self.head.y -= 1
        elif self.direction == 'left':
            self.head.x -= 1
        elif self.direction == 'down':
            self.head.y += 1

    def draw_grid(self):
        for row in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(SCREEN, DK_PURPLE, (row, 0), (row, HEIGHT))
        for col in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(SCREEN, DK_PURPLE, (0, col), (WIDTH, col))

    def wait_for_key(self):
        waiting = True
        while waiting:
            CLOCK.tick(FPS)
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                    self.playing = False
                if key[pygame.K_SPACE]:
                    waiting = False
                elif key[pygame.K_ESCAPE]:  # Esc to quit
                    waiting = False
                    self.running = False
                    self.playing = False

    def draw_score(self):
        self.font = pygame.font.SysFont('Arial', 30)
        self.message = self.font.render(str(self.score_value), True, YELLOW)
        SCREEN.blit(self.message, (10, 10))

    def draw_text(self, text, size, color, x, y):
        self.font = pygame.font.SysFont(self.font_name, size)
        self.text_surface = self.font.render(text, True, color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (x, y)
        SCREEN.blit(self.text_surface, self.text_rect)

    def show_start_screen(self):
        SCREEN.fill(AQUA)
        self.draw_text('SNAKE GAME', 100, YELLOW, WIDTH / 2, HEIGHT * 1/4)
        self.draw_text('Arrows to Move', 50, YELLOW, WIDTH / 2, HEIGHT / 2)
        self.draw_text('Press Space Bar to Play', 50, YELLOW, WIDTH / 2, HEIGHT * 3/4)
        pygame.display.flip()
        self.wait_for_key()

    def show_game_over_screen(self):
        # Game over screen at end of game. Includes play again?
        SCREEN.fill(BLACK)
        self.draw_text('GAME OVER', 100, YELLOW, WIDTH / 2, HEIGHT * 1 / 4)
        self.draw_text('Press "ESC" to quit', 50, YELLOW, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()

pygame.quit()

#  Many thanks for Tech & Gaming YouTube Channel for the instructions
# Special Thanks to Woowoodabestgnh and Chris Bradfield from  KidsCanCode
