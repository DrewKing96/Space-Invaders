import pygame
import os
import time
import random

pygame.font.init()

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

	level = 1
	lives = 5
	main_font = pygame.font.SysFont("comicsans", 50)

	#handles drawing of window
	def redraw_window():
		#blit adds image to window at defined location (0,0)->top left in pygame
		WIN.blit(BACKGROUND, (0,0))

		#drawing text
		lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
		level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

		#Add labels to screen
		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH-level_label.get_width() - 10, 10))
		pygame.display.update()

	while run:
		#allows consitently by setting clock speed
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

main()