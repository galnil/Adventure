import pygame
import sys
import os
pygame.init()

assets_path = os.getcwd()[:-7] + 'assets/'
print assets_path


display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
FPS = 50
# RGB COLORS
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)

bkgd = pygame.image.load(assets_path + 'bkgd.png').convert_alpha()
def game_exit():
    pygame.quit()
    sys.exit()
    quit()

def background_move(x):
    rel_x = x % bkgd.get_rect().width
    gameDisplay.blit(bkgd,(rel_x - bkgd.get_rect().width,0))
    x -= 1
    print rel_x
    if rel_x < display_width:
        gameDisplay.blit(bkgd, (rel_x,0 ))

    pygame.draw.line(gameDisplay, white, (rel_x,0),
                       (rel_x, display_height), 1)             
	
    
def events():
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                game_exit()

# decorate character movement with background_move decorator or
# call the function through its instance. ex. Hero.function(arguments).
# 1 or 2 ? - '' -

def game_loop():
    
    x = 0
    print bkgd
        
    
    while True:
            events()
            
            x -= 5
            gameDisplay.fill(white)
            background_move(x)
             
            '''
            rel_x = x % bkgd.get_rect().width
            gameDisplay.blit(bkgd,(rel_x - bkgd.get_rect().width,0))
            x -= 1
            print rel_x
            if rel_x < display_width:
                gameDisplay.blit(bkgd, (rel_x,0 ))
                pygame.draw.line(gameDisplay, white, (rel_x,0),
                                 (rel_x, display_height), 1)            
            '''
            pygame.display.update()
            clock.tick(FPS)

game_loop()
