import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Hunter")

font = pygame.font.Font(None, 40)

secret = random.randint(1, 100)
input_text = ""
message = "Guess a number (1-100)"
attempts = 0

running = True

while running:
    screen.fill((30, 30, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                try:
                    guess = int(input_text)
                    attempts += 1

                    if guess < secret:
                        message = "Too Low!"
                    elif guess > secret:
                        message = "Too High!"
                    else:
                        message = f"Correct! Attempts: {attempts}"

                    input_text = ""

                except:
                    message = "Enter a valid number"

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]

            else:
                input_text += event.unicode

    txt = font.render(message, True, (255, 255, 255))
    screen.blit(txt, (50, 100))

    inp = font.render(input_text, True, (0, 255, 0))
    screen.blit(inp, (50, 180))

    pygame.display.flip()

pygame.quit()