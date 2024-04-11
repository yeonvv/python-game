import pygame

# 필수###################################################################################
pygame.init()

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Name")

clock = pygame.time.Clock()
########################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)############################
fps_value = 30

# 2. 이벤트 처리 (키보드, 마우스 등)########################################################
running = True
while running:
    dt = clock.tick(fps_value)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 캐릭터 위치 정의##################################################################

    # 4. 충돌 처리########################################################################

    # 5. 화면에 그리기#####################################################################

    pygame.display.update()

pygame.quit()
