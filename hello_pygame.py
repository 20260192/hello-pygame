import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30) # 글자폰트생성

# ✅ 추가: 원의 위치 변수
x = 200
y = 300

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ✅ 추가: 키 입력 처리
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
    
    # ✅ 수정: 고정값 → 변수 사용
    pygame.draw.circle(screen, BLUE, (x, y), 50)
    
    # fps 계산 및 텍스트 생성
    fps = clock.get_fps() 
    fps_text = font.render(f"FPS: {fps:.2f}", True, (0, 0, 0))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()