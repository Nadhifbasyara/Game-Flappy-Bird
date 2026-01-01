import pygame
import random
import sys
import math
import os

# ================= INIT =================
pygame.init()
pygame.mixer.init()

# ================= SCREEN =================
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Deluxe")

clock = pygame.time.Clock()
FPS = 60

# ================= COLORS =================
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)
DARK = (30, 30, 30)

# ================= LOAD ASSETS =================
bird_img = pygame.image.load("bird.png").convert_alpha()
bird_img = pygame.transform.scale(bird_img, (48, 36))

jump_sound = pygame.mixer.Sound("jump.wav")
score_sound = pygame.mixer.Sound("score.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")

jump_sound.set_volume(0.5)
score_sound.set_volume(0.5)
gameover_sound.set_volume(0.6)

# ================= FONT =================
font_title = pygame.font.SysFont(None, 64)
font_medium = pygame.font.SysFont(None, 32)
font_small = pygame.font.SysFont(None, 22)

def draw_text_center(text, font, color, y):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(img, rect)

def draw_text_shadow(text, font, y):
    shadow = font.render(text, True, DARK)
    main = font.render(text, True, WHITE)
    rect = main.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(shadow, (rect.x + 3, rect.y + 3))
    screen.blit(main, rect)

# ================= HIGH SCORE =================
HIGHSCORE_FILE = "highscore.txt"

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read())
    return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))

high_score = load_highscore()

# ================= GAME VARIABLES =================
bird_x = SCREEN_WIDTH // 2 - bird_img.get_width() // 2
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -8

pipe_width = 60
pipe_gap = 150
pipe_velocity = 3
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(150, 400)

score = 0

# ================= GAME STATES =================
MENU = 0
PLAYING = 1
GAME_OVER = 2
game_state = MENU
played_gameover_sound = False

# ================= MENU ANIMATION =================
float_timer = 0
blink_timer = 0

def reset_game():
    global bird_y, bird_velocity, pipe_x, pipe_height, score, played_gameover_sound
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity = 0
    pipe_x = SCREEN_WIDTH
    pipe_height = random.randint(150, 400)
    score = 0
    played_gameover_sound = False

# ================= GAME LOOP =================
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == MENU:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    game_state = PLAYING
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif game_state == PLAYING:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_strength
                    jump_sound.play()

            elif game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    game_state = PLAYING
                if event.key == pygame.K_ESCAPE:
                    game_state = MENU

    # ================= MENU =================
    if game_state == MENU:
        float_timer += 0.05
        blink_timer += 1

        bird_float_y = 230 + math.sin(float_timer) * 15

        draw_text_shadow("FLAPPY BIRD", font_title, 150)
        screen.blit(bird_img, (bird_x, bird_float_y))

        draw_text_center(f"High Score : {high_score}", font_small, WHITE, 400)

        if (blink_timer // 30) % 2 == 0:
            draw_text_center("Press SPACE to Start", font_medium, WHITE, 330)

        draw_text_center("Press ESC to Quit", font_small, WHITE, 370)

    # ================= PLAYING =================
    elif game_state == PLAYING:
        bird_velocity += gravity
        bird_y += bird_velocity

        pipe_x -= pipe_velocity
        if pipe_x < -pipe_width:
            pipe_x = SCREEN_WIDTH
            pipe_height = random.randint(150, 400)
            score += 1
            score_sound.play()

        bird_rect = bird_img.get_rect(topleft=(bird_x, bird_y))
        top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height - pipe_gap)
        bottom_pipe = pygame.Rect(pipe_x, pipe_height, pipe_width, SCREEN_HEIGHT)

        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
            game_state = GAME_OVER

        if bird_y < 0 or bird_y > SCREEN_HEIGHT:
            game_state = GAME_OVER

        screen.blit(bird_img, (bird_x, bird_y))
        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)
        draw_text_center(f"Score : {score}", font_small, WHITE, 30)

    # ================= GAME OVER =================
    elif game_state == GAME_OVER:
        if not played_gameover_sound:
            gameover_sound.play()
            played_gameover_sound = True

            if score > high_score:
                high_score = score
                save_highscore(high_score)

        screen.blit(bird_img, (bird_x, bird_y))
        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)

        draw_text_shadow("GAME OVER", font_title, 220)
        draw_text_center(f"Score : {score}", font_medium, WHITE, 280)
        draw_text_center(f"High Score : {high_score}", font_medium, WHITE, 320)
        draw_text_center("SPACE : Restart", font_small, WHITE, 360)
        draw_text_center("ESC : Menu", font_small, WHITE, 390)

    pygame.display.update()

pygame.quit()
sys.exit()
