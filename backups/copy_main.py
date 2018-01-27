import pygame
import sys
pygame.init()


dw = 800
dh = 600
gameDisplay = pygame.display.set_mode((dw, dh))
clock = pygame.time.Clock()
FPS = 30
# RGB COLORS
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)


assets_wd = '~/Desktop/online-game/assets'
ms_bk = '/maplestory_map2copy.png'
bk_path = assets_wd + ms_bk


def game_exit():
    pygame.quit()
    sys.exit()


def events():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    game_exit()

def game_loop():
    running = True
    while running:
            gameDisplay.fill(white)
            gameDisplay.blit(bk_path, (0,dh))
            events()
            pygame.display.update()
            clock.tick(FPS)

game_loop()
