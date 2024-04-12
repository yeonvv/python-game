# 1. 모든 공을 없애면 게임 종료(성공)
# 2. 캐릭터는 공에 닿으면 게임 종료(실패)
# 3. 시간 제한 초과 시 게임 종료(실패)

import pygame

import os

from random import randint

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

# Font
font = pygame.font.Font(None, 40)
game_result = ""
total_time = 30
start_ticks = pygame.time.get_ticks()


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
        "pos_x": randint(0, screen_width - 160),  # 공의 x 좌표
        "pos_y": 50,  # 공의 y좌표
        "img_idx": 0,  # 공의 이미지 인덱스
        "to_x": 3,  # x축 이동방향, -3이면 왼쪽, 3이면 오른쪽
        "to_y": -6,  # 축 이동방향
        "init_spd_y": ball_speed_y[0],  # y 최초 속도
    }
)

# 사라질 무기, 공 정보 저장 변수
weapon_remove = -1
ball_remove = -1

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

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_x_pos = ball_val["pos_x"]
        ball_y_pos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 방향 변경(튕겨 나오는 효과)
        if ball_x_pos < 0 or ball_x_pos > screen_width - ball_width:
            ball_val["to_x"] *= -1

        # 스테이지에 튕길 떄
        if ball_y_pos >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:  # 그 외의 모든 경우에는 속도를 증가 = 감소한다는 뜻
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리########################################################################

    # 캐릭터 rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_x_pos = ball_val["pos_x"]
        ball_y_pos = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 rect정보 업데이트
        ball_rect = ball[ball_img_idx].get_rect()
        ball_rect.left = ball_x_pos
        ball_rect.top = ball_y_pos

        # 공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            game_result = "You Die"
            running = False
            break

        # 공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_val[0]
            weapon_rect.top = weapon_val[1]

            if weapon_rect.colliderect(ball_rect):
                weapon_remove = weapon_idx
                ball_remove = ball_idx

                # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                if ball_img_idx < 3:
                    # 현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # # 나눠진 공 정보
                    # devide_ball_rect = ball[ball_img_idx + 1].get_rect()
                    # devide_ball_width = devide_ball_rect.size[0]
                    # devide_ball_height = devide_ball_rect.size[1]
                    # 오른쪽으로 튕겨나가는 작은 공
                    balls.append(
                        {
                            "pos_x": ball_x_pos + (ball_width / 2),
                            "pos_y": ball_y_pos,
                            "img_idx": ball_img_idx + 1,
                            "to_x": 3,
                            "to_y": -6,
                            "init_spd_y": ball_speed_y[ball_img_idx + 1],
                        }
                    )
                    # 왼쪽으로 튕겨나가는 작은 공
                    balls.append(
                        {
                            "pos_x": ball_x_pos + (ball_width / 2),
                            "pos_y": ball_y_pos,
                            "img_idx": ball_img_idx + 1,
                            "to_x": -3,
                            "to_y": -6,
                            "init_spd_y": ball_speed_y[ball_img_idx + 1],
                        }
                    )
                break
        else:  # 계속 게임을 진행
            continue  # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
        break  # 안쪽 for문에서 break를 만나면 여기로 진입 가능. 2중 for문을 한번에 탈출

    # for 바깥조건:
    #     바깥동작
    #     for 안쪽조건:
    #         안쪽동작
    #         if 조건:
    #             break
    #     else:
    #         continue
    #     break

    # 충돌된 공 or 무기 없애기
    if ball_remove > -1:
        del balls[ball_remove]
        ball_remove = -1
    if weapon_remove > -1:
        del weapons[weapon_remove]
        weapon_remove = -1

    if not balls:
        game_result = "You Win"
        running = False
    # 5. 화면에 그리기#####################################################################
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_x_pos = val["pos_x"]
        ball_y_pos = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball[ball_img_idx], (ball_x_pos, ball_y_pos))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 경과 시간 계산
    elapsed_time = int((pygame.time.get_ticks() - start_ticks) / 1000)
    timer = font.render(f"Time : {total_time-elapsed_time}", True, (0, 0, 0))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update()

# 게임 오버 메시지
msg = font.render(game_result, True, (255, 0, 0))
msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
