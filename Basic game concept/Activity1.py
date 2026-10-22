from ast import For, While

import pygame
def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("color changing sprite")
    color = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'Lavender': pygame.Color('lavender'),
        'Maroon': pygame.Color('maroon'),
        'white': pygame.Color('white')
    }
    current_color = color['red']
    x,y = 30,30
    sprite_width, sprite_height = 60, 60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-= 3
        if pressed[pygame.K_RIGHT]: x+= 3
        if pressed[pygame.K_UP]: y-= 3 
        if pressed[pygame.K_DOWN]: y+= 3
        x = min(max(x, 0), screen_width - sprite_width)
        y = min(max(y, 0), screen_height - sprite_height)
        if x == 0: current_color = color['red']
        elif x == screen_width - sprite_width: current_color = color['yellow']
        elif y == 0: current_color = color['red']
        elif y == screen_height - sprite_height: 
            current_color = color['white']
        else:
            current_color = color['green']
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, 
              (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__ == "__main__":
    main()