import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.velocity = [random.randint([1, 1]), random.randint([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit = False
        pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
        pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self, color):
        self.image.fill(random.choice([ YELLOW, MAGENTA, ORANGE, WHITE]))
    def change_background_color():
        global bg_color
        bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])
all_sprites = pygame.sprite.Group()
spl = Sprite(WHITE, 20, 30)
spl.rect.x = random.randint(0, 480)
spl.rect.y = random.randint(0, 370)
all_sprites.add(spl)
screen = pygame.display.set_mode([500, 400])
pygame.display.set_caption("Boundary Sprite")
bg_color = BLUE
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            spl.change_color(random.choice([ YELLOW, MAGENTA, ORANGE, WHITE]))
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            Sprite.change_background_color()
    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()

