import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (200, 140, 150)
GRAY = (150, 150, 150)   # ✅ 추가
BLACK = (0, 0, 0)        # ✅ 추가
PINK = (255, 150, 150)   # ✅ 추가

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# 위치 변수
x = 400
y = 300

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

    screen.fill(WHITE)

    # ✅ 몸통(얼굴)
    pygame.draw.circle(screen, GRAY, (x, y), 50)

    # ✅ 귀
    pygame.draw.circle(screen, GRAY, (x - 30, y - 40), 20)
    pygame.draw.circle(screen, GRAY, (x + 30, y - 40), 20)

    # ✅ 귀 안쪽
    pygame.draw.circle(screen, PINK, (x - 30, y - 40), 10)
    pygame.draw.circle(screen, PINK, (x + 30, y - 40), 10)

    # ✅ 눈
    pygame.draw.circle(screen, BLACK, (x - 15, y - 10), 5)
    pygame.draw.circle(screen, BLACK, (x + 15, y - 10), 5)

    # ✅ 코
    pygame.draw.circle(screen, PINK, (x, y + 10), 5)

    # fps 표시
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, BLACK)
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()