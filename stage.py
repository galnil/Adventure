import pygame as pg 

class Stage:
    
    def __init__(self, background, width, height):
        self.background = pg.image.load(background)
        self.object_list = []

        self.height = height
        self.width = width
        self.game_display = pg.display.set_mode((self.width, self.height))
        
        self.add_object(self)

    def add_object(self, obj):
        """
        add object to the object list 
        """
        self.object_list.append(obj)

    def display_objects(self):
        """
        display all the objects in the stage on the screem 
        """
        for obj in self.object_list:
            self.game_display.blit(obj.get_image(), obj.get_pos())
        pg.display.update()

    def get_pos(self):
        """
        return the position of the object
        """
        x = 0 # self.background.get_rect().x
        y = self.height - 60 # self.background.get_rect().y
        
        return x, y

    def get_image(self):
        """
        return the image of the object
        """
        return self.background


class Platform(pg.sprite.Sprite):
    
    def __init__(self, stage, image, start_pos):
        stage.add_object(self) # adds the platform to the relevant stage
        self.image = pg.image.load(image).convert()
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_pos
    
    def get_pos(self):
        """
        return the position of the object
        """
        return self.rect.x, self.rect.y

    def get_image(self):
        return self.image

class Monster(Platform):
    pass


def main():
    """
    test function
    """

    pg.init()

    IMAGES_FOLDER = './assets/'
    BACKGROUND = IMAGES_FOLDER + 'bkgd.png'
    PLATFORME_IMAGE = IMAGES_FOLDER + 'player.png'
    MONSTER_IMAGE = IMAGES_FOLDER + 'ms_monster.png'

    HEIGHT = 600
    WIDTH = 800
    FPS = 60

    clock = pg.time.Clock()
    st = Stage(BACKGROUND, WIDTH, HEIGHT)
    mo = Platform(st, MONSTER_IMAGE, (50, 50))

    st.display_objects()

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
