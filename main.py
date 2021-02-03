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
BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH, HEIGHT))
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

def main():
	#if loop will be running or not
	run = True
	#frames per seconds
	FPS = 60
	clock = pygame.time.Clock()

	#handles drawing of window
	def redraw_window():
		#blit adds image to window at defined location (0,0)->top left in pygame
		WIN.blit(BACKGROUND, (0,0))
		pygame.display.update()

	while run:
		#allows consitently by setting clock speed
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

main()