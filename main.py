# !/bin/python3.5

import pygame
import sys
from player import Player
pygame.init()


dw = 800
dh = 600
gameDisplay = pygame.display.set_mode((dw, dh))
clock = pygame.time.Clock()
FPS = 30

# RGB COLORS
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)

assets_wd = './assets/'

# most bottom platform on the screen
ms_bk = 'bkgd.png'
bk_path = assets_wd + ms_bk
bkgd = pygame.image.load(bk_path).convert_alpha()

# floating platforms
img_platform = 'rplatforms.png'
path_platform = assets_wd + img_platform
platform = pygame.image.load(path_platform).convert_alpha()

# generate the player 
player_picture_path = assets_wd + 'player.png'
player = Player(player_picture_path, (400, 400))

def events():
    """ handles keyboard, exit events """
    while True:
        for e in pygame.event.get(): # e = event
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    pass

def main():
    running = True
    while running:
        gameDisplay.fill(white)
        gameDisplay.blit(bkgd,(0,205))
        gameDisplay.blit(platform, (200, 350))
        gameDisplay.blit(player.image, player.get_pos())
        #pygame.display.flip()
        pygame.display.update()
        events()
        clock.tick(FPS)

main()
