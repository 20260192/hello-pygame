import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)  # ✅ 추가: 글자 폰트 생성

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (400, 300), 50)

    # ✅ 추가: FPS 계산 및 텍스트 생성
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (0, 0, 0))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()