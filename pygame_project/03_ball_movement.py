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

# 캐릭터 이동 방향
character_to_x = 0
# 캐릭터 스피드
character_speed = 0.6

# 무기 만들기
weapon = pygame.image.load(os.path.join(images_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무시 발사 속도
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 따로 처리)
ball = [
    pygame.image.load(os.path.join(images_path, "balloon1.png")),
    pygame.image.load(os.path.join(images_path, "balloon2.png")),
    pygame.image.load(os.path.join(images_path, "balloon3.png")),
    pygame.image.load(os.path.join(images_path, "balloon4.png")),
]

# 공 스피드
ball_speed_y = [-18, -15, -12, -9]  # y축 기준 위로 올라가기 때문에 마이너스 값임

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append(
    {
        "pos_x": 50,  # 공의 x 좌표
        "pos_y": 50,  # 공의 y좌표
        "img_idx": 0,  # 공의 이미지 인덱스
        "to_x": 3,  # x축 이동방향, -3이면 왼쪽, 3이면 오른쪽
        "to_y": -6,  # 축 이동방향
        "init_spd_y": ball_speed_y[0],  # y 최초 속도
    }
)
# ball_size = [ball.get_rect().size for ball in balls]
# ball_width = [ball[0] for ball in ball_size]

# 2. 이벤트 처리 (키보드, 마우스 등)########################################################
running = True
while running:
    dt = clock.tick(fps_value)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = (
                    character_x_pos + (character_width / 2) - (weapon_width / 2)
                )
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 캐릭터 위치 정의##################################################################
    character_x_pos += character_to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 무기 없애기
    weapons = [
        [w[0], w[1]] for w in weapons if w[1] > 0
    ]  # if문에 적합한 요소는 리스트에 남고 적합하지 않게 되면 요소에서 빠진다. 요소를 뺄 생각 안해도 된다는 뜻

    # 4. 충돌 처리########################################################################

    # 5. 화면에 그리기#####################################################################
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
