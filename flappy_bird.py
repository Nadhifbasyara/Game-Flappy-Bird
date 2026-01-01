import pygame
import random
import sys

pygame.init()

# Ukuran layar
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird PNG")

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)

clock = pygame.time.Clock()
FPS = 60

# Load gambar burung
bird_img = pygame.image.load("bird.png").convert_alpha()
bird_img = pygame.transform.scale(bird_img, (40, 30))

bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# Pipa
pipe_width = 60
pipe_gap = 150
pipe_velocity = 3
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(150, 400)

# Skor
score = 0
font = pygame.font.SysFont(None, 40)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

def reset_game():
    global bird_y, bird_velocity, pipe_x, pipe_height, score
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity = 0
    pipe_x = SCREEN_WIDTH
    pipe_height = random.randint(150, 400)
    score = 0

running = True
game_over = False

while running:
    clock.tick(FPS)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    bird_velocity = jump_strength
                else:
                    game_over = False
                    reset_game()

    if not game_over:
        # Gerak burung
        bird_velocity += gravity
        bird_y += bird_velocity

        # Gerak pipa
        pipe_x -= pipe_velocity
        if pipe_x < -pipe_width:
            pipe_x = SCREEN_WIDTH
            pipe_height = random.randint(150, 400)
            score += 1

        # Collision
        bird_rect = bird_img.get_rect(topleft=(bird_x, bird_y))
        top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height - pipe_gap)
        bottom_pipe = pygame.Rect(
            pipe_x, pipe_height, pipe_width, SCREEN_HEIGHT - pipe_height
        )

        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
            game_over = True

        if bird_y < 0 or bird_y > SCREEN_HEIGHT:
            game_over = True

    # Gambar burung
    screen.blit(bird_img, (bird_x, bird_y))

    # Gambar pipa
    pygame.draw.rect(screen, GREEN, top_pipe)
    pygame.draw.rect(screen, GREEN, bottom_pipe)

    draw_text(f"Score: {score}", 10, 10)

    if game_over:
        draw_text("GAME OVER", 110, 250)
        draw_text("Press SPACE", 105, 290)

    pygame.display.update()

pygame.quit()
sys.exit()
