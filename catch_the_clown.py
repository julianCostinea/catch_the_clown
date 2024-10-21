import pygame
import random

# Initialize the game
pygame.init()

# Set up the screen
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

# Set clock
FPS = 60
clock = pygame.time.Clock()

# Set game variables
PLAYER_STARTING_LIVES = 3
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = 0.5

score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# Set up the colors
BLUE = (1, 175, 255)
YELLOW = (255, 231, 28)

# Set up the fonts
font = pygame.font.Font('Franxurter.ttf', 32)

# Set up text
title_text = font.render('Catch the Clown', True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render('Score: ' + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render('Lives: ' + str(player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render('Game Over', True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render('Click anywhere to continue', True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)

# Set sound and music
click_sound = pygame.mixer.Sound('click_sound.wav')
miss_sound = pygame.mixer.Sound('miss_sound.wav')
pygame.mixer.music.load('ctc_background_music.wav')

# Set up the images
background_image = pygame.image.load('background.png')
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

clown_image = pygame.image.load('clown.png')
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# The main game loop
pygame.mixer.music.play(-1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # A click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # check if the clown is caught
            if clown_rect.collidepoint(mouse_x, mouse_y):
                score += 1
                score_text = font.render('Score: ' + str(score), True, YELLOW)
                clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                clown_velocity = CLOWN_STARTING_VELOCITY
                clown_dx = random.choice([-1, 1])
                clown_dy = random.choice([-1, 1])
                click_sound.play()

    # move the clown
    clown_rect.x += clown_velocity * clown_dx
    clown_rect.y += clown_velocity * clown_dy

    # bounce the clown off the walls
    if clown_rect.right >= WINDOW_WIDTH or clown_rect.left <= 0:
        clown_dx *= -1

    if clown_rect.bottom >= WINDOW_HEIGHT or clown_rect.top <= 0:
        clown_dy *= -1

        # background should be blitted first
    # Blit the background
    display_surface.blit(background_image, background_rect)

    # Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    # Blit assets
    display_surface.blit(clown_image, clown_rect)

    # Update the display
    pygame.display.update()
    clock.tick(FPS)

# Quit the game
pygame.quit()
