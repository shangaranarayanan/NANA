import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Blocks")

# Colors
WHITE = (200, 200, 255)
YELLOW = (255, 255,0)
CYAN= (0, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player settings
player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 7

# Falling block settings
block_size = 30
block_x = random.randint(block_size, WIDTH - block_size)
block_y = -block_size
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

running = True

while running:
    clock.tick(120)
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move block
    block_y += block_speed

    # Reset block if it falls off screen
    if block_y > HEIGHT:
        block_x = random.randint(block_size, WIDTH - block_size)
        block_y = -block_size

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    block_rect = pygame.Rect(block_x, block_y, block_size, block_size)

    if player_rect.colliderect(block_rect):
        
        score += 1
        block_x = random.randint(block_size, WIDTH - block_size)
        block_y = -block_size

    # Draw player
    pygame.draw.rect(screen,YELLOW, player_rect)

    # Draw block
    pygame.draw.rect(screen,CYAN, block_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

pygame.quit()
