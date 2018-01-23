# !/bin/python3.5

import pygame as pg
import sys
import pylint
import pdb
pg.init()

dw = 800
dh = 600
gameDisplay = pg.display.set_mode((dw, dh))
clock = pg.time.Clock()
FPS = 60
# RGB COLORS
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)



assets_wd = './assets/'
# importing images
# most bottom platform on the screen
ms_bk = 'bkgd.png' # 0,520 --> coordinates
bk_path = assets_wd + ms_bk
bkgd = pg.image.load(bk_path).convert_alpha()
# floating platforms
img_platform = 'rplatforms.png'
path_platform = assets_wd + img_platform
platform = pg.image.load(path_platform).convert_alpha()

# initializing player
#player_rect = pygame.draw.rect(gameDisplay, black, (0, 600, 50, 50))

object_group = pg.sprite.Group() # to add to this group --> object_group.add(object)

def events(e):
	#print ('events called')

	""" handles keyboard, exit events """
	#while True
	if e.type == pg.QUIT:
		print('exit called')
		pg.quit()
		sys.exit(1)


class Player(pg.sprite.Sprite):
	"""
	This Player class defines the movement and actions of the Player

	returns:
		Player object
	"""
	def __init__(self, width, height, img):
		"""
		defining the basic featues of the Player class
		args:
			width - the width of the player rectangle
			height - the height of the player rectangle
			color - the color of the player rectangle. colors are defined at the top of the file
			img - the sprite image of the player
		
		return value:
			None
		"""
		self._w = width 
		self._h = width
		self.rect.x = 0
		self.rect.y = 300
		self._SPEED = 3
		self._x_direction = 1
		self._y_direction = 0
		self._x_change = 0
		self._y_change = 0

		# image configurations
		self.image = pg.image.load(img)
		self.image = pg.transform.image(self._w, self._h)
		self.rect = pg.get_rect(self.image)
	def _show(self):
		"""
		print the rect player to the script at location x,y, width, 
		height = self._w, self._h
		"""
		#print ('showing rect')
		#self._x += self._x_change
		#self._y += self._y_change
		rect = pg.draw.rect(gameDisplay, self._c, [self._x, self._y, self._w, self._h])
	
	def _movement(self):
		print('movement called')

		for e in pg.event.get():
			#mouse = pg.mouse.get_pos()
			#print(mouse)
			if e.type == pg.QUIT:
				events(e.type)
			if e.type == pg.KEYDOWN:
				if e.key == pg.K_RIGHT:
					self._x_change += self._SPEED
					self.x_direction = 1
				
				if e.key == pg.K_LEFT:
					self._x_change -= self._SPEED
					self_x_direction = -1

				
				if e.key == pg.K_UP:
					self._y_change -= self._SPEED
					self._y_direction = -1
					print('pressed up ')
				
				if e.key == pg.K_DOWN:
					self._y_change += self._SPEED
					self._y_direction = 1
					
			if e.type == pg.KEYUP:
				if e.key in ['K_RIGHT, K_LEFT, K_UP, K_DOWN']:
				#if e.key == 'K_RIGHT' or e.key == 'K_LEFT' or e.key == 'K_UP' or e.key == 'K_DOWN':
					self._x_change = 0
					self._y_change = 0
					self._x_direction = 0 
					self._y_direction = 0
				#print('Player x,y: {0} {1}').format(self._x,self._y)
		"""
		handling the player movement
		"""
		pass
	
	def _move(self, direction):
		"""
		the move functions handles the player movement.
		args:
			direction - indicates the direction the player should be moved to
		"""
		pass
		
		
	def _update(self):
		print ('update called')
		#try:
		self._movement()
		#except Exception as e:
			#print('self.movement func error')
		#finally:

		self._x += self._x_change
		self._y += self._y_change
		print(self._x)
		print(self._y)
		

def main():
	print ('main game')
	try:
		p = Player(50, 50, 'assets/player.png')
	except Exception as e:
		print ('could not initialize player')
		
	running = True
	
	while running:
		#print ('running!')
		gameDisplay.fill(white)
		#pdb.set_trace()
		gameDisplay.blit(bkgd,(0,205))
		gameDisplay.blit(platform, (200, 350))
		p._show()
		#try:
		p._update()
			
		for e in pg.event.get():
				#p._movement()
			if e.type == pg.QUIT:
				pg.quit()
				sys.exit(1)
				"""
				if e.type == pg.KEYDOWN:
					if e.key == pg.K_RIGHT:
						p._x_change += p._x_speed
					if e.key == pg.K_LEFT:
						p._x -= p._x_speed
					if e.key == pg.K_UP:
						p._y -= p._y_speed
					if e.key == pg.K_DOWN:
						p._y += p._y_speed
			
				"""
			
			if p._y < 500 and p._y + p._SPEED > 500:
				p._y = 499
				#print (p._y)
			else: 
				p._y += p._SPEED
			
		
		#except Exception as e:
			#print('main loop: something is not working')
		pg.display.update()
		clock.tick(FPS)

if __name__ == '__main__':
	main()

