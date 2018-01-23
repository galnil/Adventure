import pygame
import os
import sys
import random
import time
import math

pygame.init()
#imageImport
print(os.getcwd())

image_folder_path = os.getcwd()[:-7] + 'assets/'

map = image_folder_path + 'maplestory_map.png'
fireball = image_folder_path + 'fireball.png'
midget = image_folder_path + 'midget.png'
hero2 = image_folder_path + 'hero2.png'
boxer_right = image_folder_path + 'boxer_right.png'
boxer_left = image_folder_path + 'boxer_left.png'

#midget = image_folder_path + 'midget.png'




#RGB red,green,blue ------- ROG ERROR
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue = (0, 0, 255, 255)

#display settings
display_width = 1200
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
title = 'myfuckingameboi'
window_title = pygame.display.set_caption(title)





def quit_game():
    pygame.quit()
    quit()
# Class GameObject
'''
def get_direction(player_pos, target_pos):
    return (target_pos[1] - player_pos[1])/(target_pos[0] - player_pos[0])
'''



class GameObject(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()
    count = 0

    def __init__(self, image, location, size):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(image).convert_alpha()
                    self.image = pygame.transform.scale(self.image, size)
                    self.rect = self.image.get_rect()
                    self.rect.x, self.rect.y = location

                    GameObject.all_sprites.add(self)
                    print('gameObject created. size: {}, rect: {}'.format(size, self.rect))

                    GameObject.count += 1

class Hero(GameObject):
        width = 100
        height = 140
        startx = (display_width / 2)
        starty = (display_height - 170)


        def __init__(self, image):
                super(Hero, self).__init__(image, (Hero.startx, Hero.starty), (Hero.width, Hero.height))
                self.health = 10
                self.speed = 5
                self.x_direction = 1
                self.y_direction = 0
                self.x_change = 0
                self.y_change = 0



                self.health_bar()
                self.attacks = pygame.sprite.Group()


        def attack(self):
            f = Fireball(self)
            self.attacks.add(f)

        def movement(self):


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quit_game()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x_change -= self.speed
                        print('left')
                        self.x_direction = -1
                    if event.key == pygame.K_RIGHT:
                        self.x_change += self.speed
                        self.x_direction = 1
                        print('right')
                    if event.key == pygame.K_DOWN:
                        # self.y_change += self.speed
                        self.y_direction = 1
                        print('down')
                    if event.key == pygame.K_UP:
                        pass
                       # y_change -= self.speed
                       # print('up')
                        self.y_direction = -1
                    if event.key == pygame.K_SPACE:
                        # Hero.attack()
                        print('attack!')
                    if event.key == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.x_change = 0
                        self.y_change = 0
                        self.x_direction = 0
                        self.y_direction = 0
                    print('(x,y):', (self.rect.x, self.rect.y))







        def update(self):
            self.movement()
            self.rect.x += self.x_change
            self.rect.y += self.y_change


        def health_bar(self):
            font = pygame.font.SysFont(None, 35)
            text = font.render("health: "+str(self.health), True, white)
            gameDisplay.blit(text, (0, 0))








class Fireball(GameObject): #if not needed, delete.
    width = 30
    height = 30
    damage = 5
    speed = 1.0
    image = fireball

    def __init__(self, character):
        super(Fireball,self).__init__((Fireball.width, Fireball.height), (character.rect.x, character.rect.y), Fireball.image)
        self.direction, self.step = get_direction((self.rect.x, self.rect.y), target, Fireball.speed)

    def update(self):

        self.rect.x += self.step
        self.rect.y += self.direction*self.step


        if self.rect.x > display_width or self.rect.x + self.width < 0:
            pygame.sprite.Sprite.kill(self)
            print('object has been terminated')
        if self.rect.y > display_height or self.rect.y + self.height < 0:
            pygame.sprite.Sprite.kill(self)
            print('object has been terminated')


class Thing(GameObject):
        width = 50      # w,h need to be changed according to the sprite(Img)
        height = 70
        startx = random.randrange(0, display_width - width)
        starty = random.randrange(0, display_height - height)

        def __init__(self, image, hero, health, speed):
            super(Thing, self).__init__(image, (Thing.startx, Thing.starty), (Thing.width, Thing.height)) # image, location, size
            self.health = health
            self.speed = speed
            self.hero = hero
            self.attacks = pygame.sprite.Group()
            self.counter = 0 #?

        def attack(self):
            pass
            '''
            if self.counter % 500 == -1:
                f = Fireball(self, (self.hero.rect.x, self.hero.rect.y))
                self.attacks.add(f)
            self.counter += 1
            '''
        def update(self):
            pass

            # self.attack()
            if self.rect.x > display_width or self.rect.x + self.width < 0:
                pygame.sprite.Sprite.kill(f)
                print('object has been terminated')
            if self.rect.y > display_height or self.rect.y + self.height < 0:
                pygame.sprite.Sprite.kill(f)
                print('object has been terminated')



class Stage(GameObject):
        width = display_width
        height = display_height

        def __init__(self, image):
                super(Stage, self).__init__(image, (0, 0), (Stage.width, Stage.height))

        def update(self):
                pass


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    #-------- some function i had imported from the car game. message_display needs some modification


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, TextRect)
