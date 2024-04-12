import pygame

import os

# 필수###################################################################################
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pang Game")

clock = pygame.time.Clock()
########################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)############################
fps_value = 30

current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
images_path = os.path.join(current_path, "images")  # images폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(images_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(images_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(images_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height


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
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
