import pygame
pygame.init()
SCREEN_WIDTH , SCREEN_HEIGHT = 400, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image') 
background_image = pygame.transform.scale(
    pygame.image.load('lalal.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)
)
lalal_image = pygame.transform.scale(
    pygame.image.load('lalal.png').convert_alpha(), (200, 200))
lalal_rect = lalal_image.get_rect(center=(SCREEN_WIDTH //2, SCREEN_HEIGHT // 2 - 30))
text_font = pygame.font.Font(None, 36).render('Hello world', True, pygame.Color('black'))
text_rect = text_font.get_rect(center=(SCREEN_WIDTH //2, SCREEN_HEIGHT // 2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(lalal_image, lalal_rect)
        display_surface.blit(text_font, text_rect)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
