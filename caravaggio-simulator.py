import pygame
import os
from pygame import display
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN, QUIT

pygame.init()

# Declare static final variables
GAME_TITLE = "CARAVAGGIO SIMULATOR"

SCREEN_HEIGHT = 512
SCREEN_WIDTH = 608

FPS = 60
FPS_CLOCK = pygame.time.Clock()

# Creates display surface which is essentially the 'window'
displaySurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Directories of the assets
dir_path = os.path.dirname(os.path.realpath(__file__))
assets_path = os.path.join(dir_path, "assets")
background_png_path = os.path.join(assets_path, "tavern.png")


# Declare key classes - I prefer them in separate files in the future commits
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load(background_png_path)
        self.bgY = 0
        self.bgX = 0

    def render(self):
        displaySurface.blit(self.bgimage, (self.bgX, self.bgY))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Bartender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    background = Background()

    running = True

    while running:

        for event in pygame.event.get():
            # This two have to come together otherwise game won't quit due to a bug
            if event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                pass

        background.render()

        pygame.display.update()
        FPS_CLOCK.tick(FPS)
    pygame.quit()
