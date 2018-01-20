# !/bin/python3.5

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



assets_wd = './assets/'

# most bottom platform on the screen
ms_bk = 'bkgd.png'
bk_path = assets_wd + ms_bk
bkgd = pygame.image.load(bk_path).convert_alpha()
# floating platforms
img_platform = 'rplatforms.png'
path_platform = assets_wd + img_platform
platform = pygame.image.load(path_platform).convert_alpha()


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
			pygame.display.update()
			events()
			clock.tick(FPS)

main()
