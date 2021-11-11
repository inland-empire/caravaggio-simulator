import pygame,sys,os
from pygame import display
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT

pygame.init()

#Declare static final variables
GAME_TITLE = "CARAVAGGIO SIMULATOR"

SCREEN_HEIGHT = 512
SCREEN_WIDTH = 608

FPS = 60
FPS_CLOCK = pygame.time.Clock()

#Creates display surface which is essentially the 'window'
displaySurface = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
pygame.display.set_caption( GAME_TITLE )

#Directories of the assets
dir_path = os.path.dirname(os.path.realpath(__file__))
assets_path = dir_path + "\\assets\\"
background_png_path = assets_path + "tavern.png"



#Declare key classes - I prefer them in separate files in the future commits
class Background( pygame.sprite.Sprite ):
	def _init_( self ):
		super().__init__()
		self.bgimage = pygame.image.load(background_png_path)
		self.bgY = 0
		self.bgX = 0
	def render(self):
		#This doesn't work if I tried to pass in 'self.bgimage'
		displaySurface.blit(pygame.image.load(background_png_path), (0, 0))

class Player( pygame.sprite.Sprite ):
	def _init_( self ):
		super().__init__()

class Bartender( pygame.sprite.Sprite ):
	def _init_( self ):
		super().__init__()


background = Background()

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
	
	background.render()

	pygame.display.update()
	FPS_CLOCK.tick(FPS)
