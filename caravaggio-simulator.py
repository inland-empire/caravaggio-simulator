import pygame,sys
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT

pygame.init()

#Declare static final variables
GAME_TITLE = "CARAVAGGIO SIMULATOR"

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

FPS = 60
FPS_CLOCK = pygame.time.Clock()

#Creates display surface which is essentially the 'window'
displaySurface = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
pygame.display.set_caption( GAME_TITLE )

#Declare key classes - I prefer them in separate files in the future commits
class Background( pygame.sprite.Sprite ):
    def _init_( self ):
        super().__init__()

class Player( pygame.sprite.Sprite ):
    def _init_( self ):
        super().__init__()

class Bartender( pygame.sprite.Sprite ):
    def _init_( self ):
        super().__init__()


while True:

    for event in pygame.event.get():
        #This two have to come together otherwise game won't quit due to a bug
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
            pass


        