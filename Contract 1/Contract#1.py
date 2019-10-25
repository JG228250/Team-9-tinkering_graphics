## Contract One ##
## -Tarik Sabin ##
import pygame, sys
from pygame.locals import *

pygame.init()

# Set up window.
window_main = pygame.display.set_mode((600, 500), 0 , 32)
pygame.display.set_caption('Contract#1')

# Load tile png.
def load_tile():
    return pygame.image.load('Grass.png').convert()


# decreased blue and green to seem slightly darker and more red/brown like autumn.
def autumn(surface = pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(pixel.r, int(pixel.g * 0.9), int(pixel.b * 0.8)))


# increased blue and decreased red and green so it is like puddles form.
def wet(surface = pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(int(pixel.r * 0.9), int(pixel.g * 0.9), int(pixel.b * 1.1)))


# Increased red and decreased blue to make it look more yellow and dry.
def dried(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(int(pixel.r * 1.1), pixel.g, int(pixel.b * 0.9)))


# Instruction / UI setup.
font = pygame.font.Font('freesansbold.ttf', 18)
message1 = font.render('Press 1 for autumn colouration.', True, (0, 0, 0))
message2 = font.render('Press 2 for wet colouration.', True, (0, 0, 0))
message3 = font.render('Press 3 for dried colouration.', True, (0, 0, 0))
message4 = font.render('Press 4 to reset tile.', True, (0, 0, 0))
message1_rect = message1.get_rect()
message2_rect = message2.get_rect()
message3_rect = message3.get_rect()
message4_rect = message4.get_rect()

# Positions for messages.
message1_rect.center = (300, 200)
message2_rect.center = (300, 240)
message3_rect.center = (300, 280)
message4_rect.center = (300, 320)

# FPS clock stops values of colour from changing too quickly.
FPS = 15
FPSClock = pygame.time.Clock()

grass_tile = load_tile()
running = True

# Main loop.
while running == True:
    # Quit checker.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Checks if a key has been pressed and calls the relevant function.
    # 4 reloads tile to reset colour changes.
    keys = pygame.key.get_pressed()
    if keys[K_1]:
        autumn(grass_tile)
    if keys[K_2]:
        wet(grass_tile)
    if keys[K_3]:
        dried(grass_tile)
    if keys[K_4]:
        grass_tile = load_tile()

    # Clear screen and draw tile.
    window_main.fill((200, 200, 200))
    pygame.Surface.blit(window_main, grass_tile, (280, 50))

    # Display help messages.
    window_main.blit(message1, message1_rect)
    window_main.blit(message2, message2_rect)
    window_main.blit(message3, message3_rect)
    window_main.blit(message4, message4_rect)

    # FPS tick and display update.
    FPSClock.tick(FPS)
    pygame.display.update()

pygame.quit()
