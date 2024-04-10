import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("YJ GAME")

background = pygame.image.load(
    "C:/Users/customer/Desktop/yj/dev.p/python-game/pygame_basic/background.png"
)

# 캐릭터 불러오기
character = pygame.image.load(
    "C:/Users/customer/Desktop/yj/dev.p/python-game/pygame_basic/character.png"
)
character_size = character.get_rect().size  # 이미지의 크기
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 중간에 배치
character_y_pos = screen_height - character_height  # 화면 아래에 배치

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()

pygame.quit()
