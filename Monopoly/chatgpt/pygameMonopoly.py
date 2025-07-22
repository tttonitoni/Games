import pygame
from random import randint

pygame.init()

# Fenster erstellen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Monopoly")

# Farben und Schrift
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Spielfeld
def draw_board():
    pygame.draw.rect(screen, white, (50, 50, 700, 700), 3)
    pygame.draw.line(screen, black, (50, 150), (750, 150), 3)
    # Weitere Linien und Felder...

# Würfel
def roll_dice():
    return randint(1, 6)

running = True
while running:
    screen.fill(white)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                result = roll_dice()
                print(f"Würfelwurf: {result}")

    pygame.display.flip()

pygame.quit()
