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

class Laser:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)

	def draw(self, window):
		window.blit(self.img, (self.x, self.y))

	def move(self, velocity):
		self.y += velocity

	def off_screen(self, height):
		return not(self.y <= height and self.y >= 0)

	def collision(self, obj):
		return collide(obj, self)

class Ship:
	COOLDOWN = 30
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.lasers = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		#pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))
		window.blit(self.ship_img, (self.x, self.y))
		for laser in self.lasers:
			laser.draw(window)

	def move_lasers(self, velocity, obj):
		self.cooldown()
		for laser in self.lasers:
			laser.move(velocity)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			elif laser.collision(obj):
				obj.health -= 10
				self.lasers.remove(laser)

	def cooldown(self):
		if self.cool_down_counter >= self.COOLDOWN:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0:
			self.cool_down_counter += 1

	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x, self.y, self.laser_img)
			self.lasers.append(laser)
			self.cool_down_counter = 1

	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()

class Player(Ship):
	def __init__(self, x, y, health=100):
		#super adds the initailization of values from inherited class
		super().__init__(x, y, health)
		self.ship_img = MAIN_PLAYER
		self.laser_img = PIXEL_LASER_YELLOW
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health

	def move_lasers(self, velocity, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move(velocity)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			else:
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						self.lasers.remove(laser)

class Enemy(Ship):
	COLOR_MAP = {
				"red": (PIXEL_SPACE_SHIP_RED, PIXEL_LASER_RED),
				"green": (PIXEL_SPACE_SHIP_GREEN, PIXEL_LASER_GREEN),
				"blue": (PIXEL_SPACE_SHIP_BLUE, PIXEL_LASER_BLUE)
				}

	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self, velocity):
		self.y += velocity

def collide(obj1, obj2):
	offset_x = obj2.x - obj1.x
	offset_y = obj2.y - obj1.y
	return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None 


def main():
	#if loop will be running or not
	run = True
	#frames per seconds
	FPS = 60
	clock = pygame.time.Clock()
	level = 0
	lives = 5

	lost = False
	lost_count = 0
	player = Player(300, 650)

	main_font = pygame.font.SysFont("comicsans", 50)
	lost_font = pygame.font.SysFont("comicsans", 60)

	enemies = []
	wave_length = 5
	enemy_velocity = 1

	player_velocity = 5
	laser_velocity = 4

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

		for enemy in enemies:
			enemy.draw(WIN)

		ship.draw(WIN)

		pygame.display.update()

	while run:
		#allows consitently by setting clock speed
		clock.tick(FPS)

		if len(enemies) == 0:
			level += 1
			wave_length += 5
			for i in range(wave_length):
				enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
				enemy.append(enemy)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		#if asset desires to be moved with only one key press, add inside event loop, outside loop:multiple key presses, allowing for diagonal movement
		#gets keys being pressed
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and ship.x + player_velocity > 0: #left
			ship.x -= player_velocity

		if keys[pygame.K_d] and ship.x + player_velocity + ship.get_width() < WIDTH: #right
			ship.x += player_velocity

		if keys[pygame.K_w] and ship.y + player_velocity > 0: #up
			ship.y -= player_velocity

		if keys[pygame.K_s] and ship.y + player_velocity + ship.get_height() < HEIGHT: #down
			ship.y += player_velocity

		redraw_window()
main()