import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Chaos Arena")

clock = pygame.time.Clock()

COLORS = [
    (255, 80, 80),
    (80, 255, 120),
    (80, 150, 255),
    (255, 255, 80),
    (255, 100, 255)
]

player_radius = 30
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_color = random.choice(COLORS)
player_speed = 7

blocks = []
block_speed = 5

font = pygame.font.SysFont(None, 40)
score = 0

def spawn_block():
    size = 60
    x = random.randint(0, WIDTH - size)
    color = random.choice(COLORS)
    rect = pygame.Rect(x, 0, size, size)
    return rect, color

running = True
while running:
    screen.fill((20, 20, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_color = random.choice(COLORS)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_radius:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_radius:
        player_x += player_speed

    if random.randint(1, 25) == 1:
        blocks.append(spawn_block())

    for block in blocks[:]:
        rect, color = block
        rect.y += block_speed

        if rect.y > HEIGHT:
            blocks.remove(block)
            score += 1

        player_rect = pygame.Rect(
            player_x - player_radius,
            player_y - player_radius,
            player_radius * 2,
            player_radius * 2
        )

        if rect.colliderect(player_rect):
            if color == player_color:
                blocks.remove(block)
                score += 5
            else:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, color, rect)

    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(60)
