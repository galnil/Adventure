# !/bin/python3.5

import pygame as pg
import sys
import pylint
import pdb
from stage import *
import images
pg.init()

dw = 800
dh = 600
#gameDisplay = pg.display.set_mode((dw, dh))
clock = pg.time.Clock()
FPS = 60
# RGB COLORS
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)

pg.key.set_repeat(1,10) # the get_repeat method sends multiple pygame events while a key is being held down

assets_wd = './assets/'
# importing images

ms_bk = 'bkgd.png' # length - 960 px, height - 60 px

bk_path = assets_wd + ms_bk
#bkgd = pg.image.load(bk_path).convert_alpha()
# floating platforms
img_platform = 'platforms.png'
path_platform = assets_wd + img_platform
#platform = pg.image.load(path_platform).convert_alpha()

# initializing player
#player_rect = pygame.draw.rect(gameDisplay, black, (0, 600, 50, 50))

object_group = pg.sprite.Group() # to add to this group --> object_group.add(object)

def events(player=None):
	#print ('events called')

	""" handles keyboard, exit events """

	for e in pg.event.get():
		if e.type == pg.QUIT or (e.type == pg.KEYDOWN) and (e.key == pg.K_ESCAPE):

			print('exit called')
			pg.quit()
			sys.exit(1)
			
		if e.type == pg.KEYDOWN:
				# call the move player function
			key = pg.key.get_pressed()
				#event_name = pg.key.name(e.key)
				#player.move(event_name)
			if player == None:
				pass
			else:
				if key[pg.K_RIGHT]:
					player.move(1, 0)
				if key[pg.K_LEFT]:
					player.move(-1, 0)
				if key[pg.K_UP]:
					player.move(0, -1)
				if key[pg.K_DOWN]:
					player.move(0, 1)
				
				#print('events fuc e.key: {0}'.format(e.key))
"""
		if e.type == pg.KEYUP:
			player.key_up()
			print('pg.KEYUP CALLED')
"""
class Player(Platform):
	"""
	This Player class defines the movement and actions of the Player

	returns:
		Player object
	"""
	def __init__(self, image, start_pos, width, height):
		super().__init__(image, start_pos)
		"""
		defining the basic features of the Player class
		args:
			width - the width of the player rectangle
			height - the height of the player rectangle
			color - the color of the player rectangle. colors are defined at the top of the file
			img - the sprite image of the player
		
		return value:
	                 None
		"""
                # setting the Player's height, and width
		self._w = width 
		self._h = height
                
    	# image configurations
		"""
		self.image = pg.image.load(img)
		self.image = pg.transform.scale(self.image, (self._w, self._h))
		self.rect = self.image.get_rect(center=(100,100))
		"""
		self._SPEED = 3
		self._x_direction = 1
		self._y_direction = 0
		self._x_change = 0
		self._y_change = 0

	def _show(self):
		"""
		print the rect player to the script at location x,y, width, 
		height = self._w, self._h
		"""
		#print ('showing rect')
                #self._x += self._x_change
		#self._y += self._y_change
		#rect = pg.draw.rect(gameDisplay, white, [self.rect.x, self.rect.y, self._w, self._h])
		#gameDisplay.blit(self.image, (self.rect.x,self.rect.y))

	
	def key_up(self):
		self._x_change = 0
		self._y_change = 0
		self._x_direction = 0
		self._y_direction = 0

	def move(self, dx,dy):
		# pygame.event.event_name(type) --> the event name as string
		"""
		the move functions handles the player movement.
		args:
			dx - indicates the direction to move in relation to the x-axis, 1/-1 (right/left), type: int
			dy - indicate the direction to move in relation to the y-axis, 1/-1 (down/up), type: int
		return Value:
			type:None, no return specified
		"""
		self._x_change += self._SPEED * dx
		self._y_change += self._SPEED * dy
		
		self._update()
		self.key_up()

	def _update(self):

		self.rect.x += self._x_change
		self.rect.y += self._y_change
	
		print('__update__')
		print('x after addition: {0}'.format(self.rect.x))
		print('y after addition: {0}'.format(self.rect.y))

def main():
	print ('main game')
        
	#try:
	#p = Player(100, 100, 'assets/player.png')
	# initialize a stage instance
	stage = Stage(bk_path, dw, dh)
	stage_rect = stage.get_pos()
	print('stage_rect: {0}'.format(stage_rect))
	# fill stage instance
	#stage.game_display.fill(white)
	# adding the platform objects to the stage
	platform1 = Platform(stage, images.platform1_path, (dw/2, dh/2))
	platform2 = Platform(stage, images.platform2_path, (dw/3, dh/3))
	# player initialization, adding player to stage.object_list
	p = Player('assets/player.png', (100, 100), 100, 100)
	#bottom_platform = Platform(stage, images.bottom_platform_path, (dw-60, dh))
	#print(stage.object_list)# make a better representation
	#except Exception as e:
	#print ('could not initialize player')
		
	running = True
	
	while running:
		#gameDisplay.fill(black)
		#gameDisplay.blit(bkgd,(0,dh - 60))
		#gameDisplay.blit(platform, (200, 350))
		
		# fill the stage instance
		stage.game_display.fill(black)
		# adding the platform objects to the stage
		stage.display_objects()
		#p._show()
		events() # argument is an instance of the Player class

	
		pg.display.update()
		clock.tick(FPS)

if __name__ == '__main__':
	main()


