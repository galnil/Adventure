import pygame 

class Player(pygame.sprite.Sprite):
    """
    define a player class 
    """

    def __init__(self, image, pos):

        super().__init__() # initilaized the pygame.sprite.Sprite class 

        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self._v_x, self._v_y = 0, 0 
        

    def move_left(self):
        """
        move the player left 
        """
        self.rect.x -= self.v_x
    
    def move_right(self):
        """
        move the player right
        """
        self.rect.x += self.v_x

    def jump(self):
        """
        jump function 
        """
        self.rect.y += self.v_y

    def fall(self):
        """
        the player fall
        """
        pass

    def get_pos(self):
        """
        return the postion of the player
        """
        return self.rect.x, self.rect.y

    def get_v(self):
        """
        return the velosity of the player 
        """
        return self._v_x, self._v_y

