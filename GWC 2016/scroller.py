import pygame
import random

class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(→).
            A negative integer draws the building left to right (←).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up ↑
            A negative integer draws the building down ↓
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn
    """
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width   = width
        self.height  = height
        self.color   = color

    """
    uses pygame and the global screen variable to draw the building on the screen
    """
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

    """
    Takes in an integer that represents the speed at which the building is moving
        A positive integer moves the building to the right →
        A negative integer moves the building to the left  ←
    Moves the building horizontally across the screen by changing the position of the
    x_point by the speed
    """
    def move(self, speed):
        self.x_point -= speed

class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """
    def __init__(self, width, height, base, color, speed):
        self.width  = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings = []
        self.add_buildings() # Add builings each time a new instance is created

    """
    Will add a randomly generated building that fits within the width and height
    of the scroller
    """
    def add_buildings(self):
        current_width = 0 # How wide the scroller is right now
        while current_width <= self.width:
            self.add_building(current_width)
            current_width += self.buildings[-1].width
            self.scroll_end = current_width

    """
    takes in an x_location, an integer, that represents where along the x-axis to
    put a buildng.
    Adds a building to list of buildings.
    """
    def add_building(self, x_location):
        # The building width will be a random integer between 1/20th and 1/4th of the width
        building_width = random.randint((self.width // 20), (self.width // 4))

        max_height = self.base - self.height # this sets the maximum height each building can be

        # The building width will be a random integer between 1/4th and just under the max_height
        building_height = random.randint((max_height // 4), (max_height - 1))

        y_location = self.base - building_height # This tells the building where along the y-axis to draw itself

        self.buildings.append(Building(x_location, y_location, building_width, building_height, self.color))

    """
    This calls the draw method on each building.
    """
    def draw_buildings(self, screen):
        for building in self.buildings:
            building.draw(screen)

    """
    This calls the move method on each building passing in the speed variable
    As the buildings move off the screen a new one is added.
    """
    def move_buildings(self):
        for building in self.buildings:
            building.move(self.speed)

        #gets the x_point of the last building and adds it's width to place the new building right next to it.
        new_building_location = self.buildings[-1].x_point + self.buildings[-1].width

        self.add_building(new_building_location)
