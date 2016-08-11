"""
 Pygame documentation: https://www.pygame.org/docs/genindex.html
"""
import pygame
import random
from scroller import Scroller

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
PINK = (227, 23, 105)
LIME_GREEN = (156, 227, 23)
PURPLE = (101, 16, 158)
DARK_BLUE = (0, 0, 30)
LTYELLOW=(245,238,137)
CLOUDWHITE=(223,241,247)
ORANGE=(250,187,52)
MIDDLE_SCROLLER_COLOR = LTYELLOW
BACK_SCROLLER_COLOR = ORANGE
BACKGROUND_COLOR = pygame.image.load("bgimage.jpg")
FRONT_SCROLLER_COLOR = CLOUDWHITE

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("City Scroller")

# loop until the user clicks the close button
done = False

# used to manage how fast the screen updates
clock = pygame.time.Clock()

front_scroller = Scroller(SCREEN_WIDTH, 400, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
# list of scroller objects we will use in the main loop
scrollers = [back_scroller, middle_scroller, front_scroller]
class airplane (pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("airplane4.png")
        self.image=pygame.transform.scale(self.image,(150,150))

        self.rect= self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image,self.rect)

class coin(airplane):
    def __init__(self,color,width,height,collect):
        aiplane.__init__(self,color,width,height)
        self.collect=collect
class book(airplane):
    def __init__(self,color,width,height,hit):
        airplane.__init__(self,color,width,height)
        self.hit=hit



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BACKGROUND_COLOR,(0,0))



    # --- Drawing code should go here
    for scroller in scrollers:
        scroller.draw_buildings(screen)
        scroller.move_buildings()

    player=airplane(BLACK,20,30)

    player.draw(screen)



    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
exit() # Needed when using IDLE
