"""
 Pygame base template for opening a window
 Pygame documentation: https://www.pygame.org/docs/genindex.html
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PURPLE=(172,7,227)
TEAL=(39,245,193)
MAGENTA=(245,39,149)
LTBLUE=(39,207,245)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Part 1")

xspeed= random.randint(-10,15)
yspeed=random.randint(-10,15)
xspeed2= random.randint(-5,20)
yspeed2=random.randint(-5,20)
xloc=350
yloc=250
xloc2=250
yloc2=150
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    colors=[BLACK,RED,WHITE,BLUE,GREEN,GREY,PURPLE,TEAL,MAGENTA,LTBLUE]
    colors_length=len(colors)
    choice=random.randint(0,colors_length-1)
    randcolor=colors[choice]
    screen.fill(TEAL)

    # --- Drawing code should go here
    radius=random.randint(20,80)
    radius2=random.randint(10,40)
    circle=pygame.draw.circle(screen, randcolor, (xloc,yloc),radius)
    circle=pygame.draw.circle(screen, WHITE, (xloc2,yloc2),radius2)

    # --- Go ahead and update the screen with what we've drawn.



    if xloc > SCREEN_WIDTH-radius:
        xspeed=xspeed*-1

    if xloc < radius:
        xspeed=xspeed*-1

    if yloc > SCREEN_HEIGHT-radius:
        yspeed=yspeed*-1

    if yloc <radius:
        yspeed=yspeed*-1


    if xloc2 > SCREEN_WIDTH-radius2:
                xspeed2=xspeed2*-1

    if xloc2 < radius2:
                xspeed2=xspeed2*-1

    if yloc2 > SCREEN_HEIGHT-radius2:
                yspeed2=yspeed2*-1

    if yloc2 <radius2:
                yspeed2=yspeed2*-1

    xloc+=xspeed
    yloc+=yspeed
    xloc2+=xspeed2
    yloc2+=yspeed2
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
