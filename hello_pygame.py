import pygame
import sys
import random  # ✅ 추가

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (255, 255, 255)
GRAY = (200, 140, 150)
BLACK = (0, 0, 0)
PINK = (255, 150, 150)
YELLOW = (255, 220, 0)  # ✅ 치즈 색

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# 위치 변수
x = 400
y = 300

# ✅ 치즈 관련 변수
cheese_x = random.randint(50, 750)
cheese_y = random.randint(50, 550)
cheese_size = random.randint(5, 10)
last_spawn_time = pygame.time.get_ticks()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    # ✅ 5초마다 치즈 재생성
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > 5000:
        cheese_x = random.randint(50, 750)
        cheese_y = random.randint(50, 550)
        cheese_size = random.randint(5, 10)
        last_spawn_time = current_time

    # ✅ 충돌 체크 (간단 거리 계산)
    distance = ((x - cheese_x) ** 2 + (y - cheese_y) ** 2) ** 0.5
    if distance < 50 + cheese_size:
        cheese_x = random.randint(50, 750)
        cheese_y = random.randint(50, 550)
        cheese_size = random.randint(5, 10)
        last_spawn_time = current_time

    screen.fill(WHITE)

    # 🧀 치즈
    pygame.draw.circle(screen, YELLOW, (cheese_x, cheese_y), cheese_size)

    # 🐭 얼굴
    pygame.draw.circle(screen, GRAY, (x, y), 50)
    pygame.draw.circle(screen, GRAY, (x - 30, y - 40), 20)
    pygame.draw.circle(screen, GRAY, (x + 30, y - 40), 20)
    pygame.draw.circle(screen, PINK, (x - 30, y - 40), 10)
    pygame.draw.circle(screen, PINK, (x + 30, y - 40), 10)
    pygame.draw.circle(screen, BLACK, (x - 15, y - 10), 5)
    pygame.draw.circle(screen, BLACK, (x + 15, y - 10), 5)
    pygame.draw.circle(screen, PINK, (x, y + 10), 5)

    # fps 표시
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, BLACK)
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()