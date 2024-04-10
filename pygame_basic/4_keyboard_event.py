import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("YJ GAME")

background = pygame.image.load(
    "C:/Users/customer/Desktop/yj/dev.p/python-game/pygame_basic/background.png"
)

character = pygame.image.load(
    "C:/Users/customer/Desktop/yj/dev.p/python-game/pygame_basic/character.png"
)
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= 5
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= 5
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += 5
        if event.type == pygame.KEYUP:  # 키를 뗐는지 확인
            if (
                event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT
            ):  # x좌표 이동 후 다시 값 리셋. 이 값이 없으면 아래의 좌표 더셈 코드에 계속해서 to_x 또는 y값이 적용되어 계속 더해진다.
                to_x = 0
            elif (
                event.key == pygame.K_UP or event.key == pygame.K_DOWN
            ):  # y좌표 이동 후 다시 값 리셋
                to_y = 0
    character_x_pos += to_x  # 움직인 값만큼 x좌표 값 변경
    character_y_pos += to_y  # 움직인 값만큼 y좌표 값 변경

    # x축 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos + character_width > screen_width:
        character_x_pos = screen_width - character_width

    # y축경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos + character_height > screen_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
