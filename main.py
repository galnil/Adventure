# !/bin/python3.5

import pygame as pg
import sys
import pylint
import pdb
from stage import *
pg.init()

dw = 800
dh = 600
gameDisplay = pg.display.set_mode((dw, dh))
clock = pg.time.Clock()
FPS = 60
# RGB COLORS
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)

pg.key.set_repeat(1,10) # the get_repeat method sends multiple pygame events while a key is being held down

assets_wd = './assets/'
# importing images
		# most bottom platform on the screen
ms_bk = 'bkgd.png' # 0,520 --> coordinates

bk_path = assets_wd + ms_bk
bkgd = pg.image.load(bk_path).convert_alpha()
# floating platforms
img_platform = 'platforms.png'
path_platform = assets_wd + img_platform
platform = pg.image.load(path_platform).convert_alpha()

# initializing player
#player_rect = pygame.draw.rect(gameDisplay, black, (0, 600, 50, 50))

object_group = pg.sprite.Group() # to add to this group --> object_group.add(object)

def events(player):
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
class Player(pg.sprite.Sprite):
	"""
	This Player class defines the movement and actions of the Player

	returns:
		Player object
	"""
	def __init__(self, width, height, img):
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
		self.image = pg.image.load(img)
		self.image = pg.transform.scale(self.image, (self._w, self._h))
		self.rect = self.image.get_rect(center=(100,100))
		self.rect.x = 0
		self.rect.y = 300
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
		gameDisplay.blit(self.image, (self.rect.x,self.rect.y))

	
	def key_up(self):
		self._x_change = 0
		self._y_change = 0
		self._x_direction = 0
		self._y_direction = 0

	def _movement(self):
		print('movement called')

		"""
			if e.type == pg.QUIT:
				events(e.type)
			if e.type == pg.KEYDOWN:
				if e.key == pg.K_RIGHT:
					self._x_change += self._SPEED
					self.x_direction = 1
					print('pressed right')
					self.key_up()
				if e.key == pg.K_LEFT:
					self._x_change -= self._SPEED
					self_x_direction = -1
					print('pressed left')
					self.key_up()
				if e.key == pg.K_UP:
					self._y_change -= self._SPEED
					self._y_direction = -1
					print('pressed up')
					self.key_up()
				if e.key == pg.K_DOWN:
					self._y_change += self._SPEED
					self._y_direction = 1
					print('pressed down')
					self.key_up()
			
			if e.type == pg.KEYUP:
				#if e.key in ['K_RIGHT, K_LEFT, K_UP, K_DOWN']:
				if e.key == 'K_RIGHT' or e.key == 'K_LEFT' or e.key == 'K_UP' or e.key == 'K_DOWN':
					self.key_up()
				#print('Player x,y: {0} {1}').format(self._x,self._y)
				"""
		"""
		handling the player movement
		"""
	
	def move(self, dx,dy):
		# pygame.event.event_name(type) --> the event name as string
		"""
		the move functions handles the player movement.
		args:
			event_key - the event key indicates the name of the key pressed by the user
		"""
		'''
		moves = {'right': ('x', 1), 'left': ('x', -1), 'up': ('y', -1), 'down':('y', 1)} # RIGHT, LEFT, UP, DOWN
		# k = keyboard key, v = (axis_direction, sign)
		if event_name in moves:
			"move the player to the direction indicated by the event_key"
			axis, sign = moves[event_name]

			if axis == 'x':
				self._x_change += sign*self._SPEED
				self._x_direction = sign
				
			if axis == 'y':
				self._y_change += sign*self._SPEED
				self._y_direction = sign
			
			self._update()
			self.key_up()
		'''
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
	p = Player(100, 100, 'assets/player.png')
	#except Exception as e:
	#print ('could not initialize player')
		
	running = True
	
	while running:
		gameDisplay.fill(black)
		gameDisplay.blit(bkgd,(0,205))
		gameDisplay.blit(platform, (200, 350))
		p._show()
		#p._update()
		events(p) # p is an instance of the Player class

	
		pg.display.update()
		clock.tick(FPS)

if __name__ == '__main__':
	main()


