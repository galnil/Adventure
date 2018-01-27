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


def events(event):
	#print ('events called')

	""" handles keyboard, exit events """
	#while True:
	event()
	"""
	for e in pg.event.get(): # e = event
		if e.type == pg.QUIT:
			print('exit called')
			pg.quit()
			sys.exit(1)
	"""		

class Player(pg.sprite.Sprite):
	"""
	This class is all about the 
	"""
	def __init__(self, width, height, color):
		"""
		defining the basic featues of the Player class
		"""
		self._w = width 
		self._h = width
		self._c = color
		self._x = 0
		self._y = 300
		self._x_speed = 3
		self._y_speed = 3
		
		#self._movement()
	def _show(self):
		"""
		print the rect player to the script at location x,y, width, 
		height = self._w, self._h
		"""
		#print ('showing rect')
		pg.draw.rect(gameDisplay, self._c, [self._x, self._y, self._w, self._h])
	
	def _movement(self):
		#print('movement called')
		"""
		for e in pg.event.get():
			#self._y += 3
			if e.type == pg.KEYDOWN:
				if e.key == pg.K_RIGHT:
					self._x += 5
					
				if e.key == pg.K_LEFT:
					self._x -= 5
				
				if e.key == pg.K_UP:
					self._y -=5
					print('pressed up ')
				
				if e.key == pg.K_DOWN:
					self._y +=5
		"""
		"""
		handling the player movement
		"""
		
		pass


def main():
	falling_speed = 3
	print ('main game')
	try:
		p = Player(50, 50, black)
	except Exception as e:
		print ('could not initialize player')
		
	running = True
	
	while running:
		x_change = 0
		y_change = 0
		#print ('running!')
		gameDisplay.fill(white)
		#pdb.set_trace()
		gameDisplay.blit(bkgd,(0,205))
		gameDisplay.blit(platform, (200, 350))
		
		p._show()
		mouse = pg.mouse.get_pos()
		for e in pg.event.get():
			print (e)
				#p._movement()
			if e.type == pg.QUIT:
				pg.quit()
				sys.exit(1)
			elif e.type == pg.KEYDOWN:
				if e.key == pg.K_RIGHT:
					x_change += p._x_speed
				elif e.key == pg.K_LEFT:
					x_change -= p._x_speed
				elif e.key == pg.K_UP:
					y_change -= p._y_speed
				elif e.key == pg.K_DOWN:
					y_change += p._y_speed
			
			p._x += x_change
			p._y += y_change
			#print (mouse)
		
		pg.display.update()
		clock.tick(FPS)
main()

