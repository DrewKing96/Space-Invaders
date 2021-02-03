import pygame
import os
import time
import random

#Define the width and height for pygame window
WIDTH, HEIGHT = 750, 750

#Establish pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#Defines the name of the pygame window
pygame.display.set_caption("Space Invaders")

#Background
BACKGROUND = pygame.image.load(os.path.join("assets", "background-black.png"))

#Lasers
PIXEL_LASER_BLUE = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
PIXEL_LASER_GREEN = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
PIXEL_LASER_RED = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
PIXEL_LASER_YELLOW = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#Computer Ships
PIXEL_SPACE_SHIP_BLUE = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
PIXEL_SPACE_SHIP_GREEN = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
PIXEL_SPACE_SHIP_RED = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))

#Player Ship
MAIN_PLAYER = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

