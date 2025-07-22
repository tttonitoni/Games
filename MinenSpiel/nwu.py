import pygame
import sys

# Initialisieren
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")
clock = pygame.time.Clock()

# Farben
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)

# Spieler
player_width, player_height = 50, 50
player_x, player_y = 100, 500
player_vel_x = 0
player_vel_y = 0
player_speed = 5
jump_force = -15
gravity = 1
on_ground = False

# Plattformen
platforms = [
    pygame.Rect(0, 580, WIDTH, 20),                # Boden
    pygame.Rect(300, 450, 200, 20),
    pygame.Rect(100, 350, 200, 20),
    pygame.Rect(500, 300, 200, 20),
]

def move_player(keys):
    global player_x, player_y, player_vel_x, player_vel_y, on_ground

    # Steuerung
    player_vel_x = 0
    if keys[pygame.K_LEFT]:
        player_vel_x = -player_speed
    if keys[pygame.K_RIGHT]:
        player_vel_x = player_speed
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_force

    # Schwerkraft
    player_vel_y += gravity

    # Bewegung anwenden
    player_x += player_vel_x
    player_y += player_vel_y

    # Kollisionsprüfung
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    on_ground = False

    for platform in platforms:
        if player_rect.colliderect(platform) and player_vel_y >= 0:
            player_y = platform.top - player_height
            player_vel_y = 0
            on_ground = True

# Hauptloop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move_player(keys)

    # Plattformen zeichnen
    for p in platforms:
        pygame.draw.rect(screen, GREEN, p)

    # Spieler zeichnen
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Game Over wenn runtergefallen
    if player_y > HEIGHT:
        print("Game Over")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
