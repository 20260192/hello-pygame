import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (255, 255, 255)
GRAY = (200, 140, 150)
BLACK = (0, 0, 0)
PINK = (255, 150, 150)
YELLOW = (255, 220, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# 위치 변수
x = 400
y = 300

# ✅ 치즈 리스트
cheeses = []  # 각 치즈는 [x, y, size]
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

    # ✅ 5초마다 새 치즈 추가
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > 5000:
        new_cheese = [
            random.randint(50, 750),
            random.randint(50, 550),
            random.randint(5, 10)
        ]
        cheeses.append(new_cheese)
        last_spawn_time = current_time

    # ✅ 충돌 체크
    for cheese in cheeses[:]:  # 리스트 복사해서 순회
        distance = ((x - cheese[0])**2 + (y - cheese[1])**2) ** 0.5
        if distance < 50 + cheese[2]:
            cheeses.remove(cheese)  # 닿으면 제거

    screen.fill(WHITE)

    # 🧀 모든 치즈 그리기
    for cheese in cheeses:
        pygame.draw.circle(screen, YELLOW, (cheese[0], cheese[1]), cheese[2])

    # 🐭 생쥐
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