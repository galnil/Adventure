import pygame
import os
import sys
import random
import time

from classes import *


pygame.init()


clock = pygame.time.Clock()


        

                     

        
def crash():
        game_loop()  

def obj_display(hero):
                '''
                if y + character1_height < 0:
                        gameDisplay.blit(backImg2,(0,0))
                        y = (display_height - character1_height)
                for ob in GameObject.game_objects:
                        gameDisplay.blit(ob.image, (ob.rect.x, ob.rect.y))

                hero.health_bar()
                '''


        


#gameloop

def game_loop():
            stage = Stage(map)
            onada = Hero(boxer_right)#image
            sharmuta = Thing(midget, onada, 10, 0) #  image, hero, health, speed

            gameExit = False

            #'event handling'
            while not gameExit:

                gameDisplay.fill(white)
                onada.health_bar()

                GameObject.all_sprites.draw(gameDisplay)
                GameObject.all_sprites.update()
                pygame.display.update()
                clock.tick(60)
#handling boundries
            if onada.rect.x > display_width or onada.rect.x + onada.width < 0:
                print('x crossover')
                crash()
                        
            if onada.rect.y > display_height or onada.rect.y + onada.height < 0:
                print('y crossover')
                crash()

                # only to check if obj_display(health_bar....) fucking works                       


                
              
game_loop()

pygame.quit()
quit()
