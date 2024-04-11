import pygame

from random import randint

# 필수###################################################################################
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기 게임")

clock = pygame.time.Clock()
########################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)############################
fps_value = 30

font = pygame.font.Font(None, 40)


background = pygame.image.load("pygame_basic/background.jpg")

character = pygame.image.load("pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
char_speed = 0.6

enemy = pygame.image.load("pygame_basic/ddong.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0 - enemy_height
enemy_speed = 10

to_x = 0
to_y = 0

count = 0
# 2. 이벤트 처리 (키보드, 마우스 등)########################################################
running = True
while running:
    dt = clock.tick(fps_value)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= char_speed
            elif event.key == pygame.K_RIGHT:
                to_x += char_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    # 3. 캐릭터 위치 정의##################################################################
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_x_pos = randint(0, screen_width - enemy_width)
        enemy_y_pos = 0 - enemy_height
        count += 1

    color = (0, 0, 0)

    elapsed_time = pygame.time.get_ticks() / 1000

    timer = font.render(
        str(int(elapsed_time)),
        True,
        color,
    )

    score = font.render(str(f"Score : {count}"), True, color)

    # 4. 충돌 처리########################################################################
    char_rect = character.get_rect()
    char_rect.top = character_y_pos
    char_rect.left = character_x_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.top = enemy_y_pos
    enemy_rect.left = enemy_x_pos

    if char_rect.colliderect(enemy_rect):
        print("게임 오버")
        running = False
    # 5. 화면에 그리기#####################################################################

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))
    screen.blit(score, (screen_width - 130, 10))

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
