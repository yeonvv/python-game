import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("YJ GAME")

# 배경 설정
background = pygame.image.load(
    "C:/Users/customer/Desktop/yj/dev.p/python-game/pygame_basic/background.png"
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((0, 0, 255)) # rgb 값으로 채우기
    screen.blit(background, (0, 0))  # 배경 그리기
    pygame.display.update()  # 게임화면을 다시 그리기

pygame.quit()
