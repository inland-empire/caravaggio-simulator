import pygame
import os
from pygame import Vector2, display
from pygame.constants import K_LEFT, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from enum import Enum

pygame.init()

# Declare static final variables
GAME_TITLE = "CARAVAGGIO SIMULATOR"

SCREEN_HEIGHT = 512
SCREEN_WIDTH = 608

FPS = 60
FPS_CLOCK = pygame.time.Clock()
SPEED = 400

# Creates display surface which is essentially the 'window'
displaySurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# Directories of the assets
dir_path = os.path.dirname(os.path.realpath(__file__))
assets_path = os.path.join(dir_path, "assets")
background_png_path = os.path.join(assets_path, "tavern.png")
player_png_path = os.path.join(assets_path, "cara.png")


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
        img = pygame.image.load(player_png_path)
        img_height = img.get_height()
        img_width = img.get_width()
        scale = 0.25
        self.image = pygame.transform.scale(img, (int(img_width * scale), int(img_height * scale)))
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        # Player's current position on the surface
        self.pos = Vector2(340, 240)
        # Player's walking / running speed
        self.velocity = Vector2(0.0, 0.0)
        self.accelerate = Vector2(0.0)
        # Direction our player is currentlyfacing
        # class Direction(Enum):
        #     UP = 1
        #     DOWN = 2
        #     LEFT = 3
        #     RIGHT = 4
        # self.direction = Direction.RIGHT

    def move(self):
        displacement = self.velocity / FPS 
        self.rect = self.rect.move(int(displacement.x), int(displacement.y))

    def update(self):
        self.move() # move to new position
        print(self.velocity)
        print(self.rect)
        displaySurface.blit(self.image, self.rect) # draw new player

# This will be the method to make enemy angry and can provoke a fight
    def provoke(self):
        pass

    def attack(self):
        pass


class Bartender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    player = Player()
    background = Background()

    running = True

    while running:

        for event in pygame.event.get():
            # This two have to come together otherwise game won't quit due to a bug
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.velocity.x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * SPEED
        player.velocity.y = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * SPEED
        background.render()
        player.update()

        pygame.display.update()
        FPS_CLOCK.tick(FPS)
    pygame.quit()
