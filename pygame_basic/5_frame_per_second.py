import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("YJ GAME")

# FPS
clock = pygame.time.Clock()

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

to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

running = True
while running:
    dt = clock.tick(
        30
    )  # 게임화면의 초당 프레임 수를 설정. 마지막 프레임 이후 경과한 시간을 밀리초 단위로 반환

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    # 프레임 간의 시간 차이를 고려하여 캐릭터의 이동 속도를 일정하게 유지하기 위함
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos + character_width > screen_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos + character_height > screen_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
