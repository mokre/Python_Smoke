import pygame, random

class smoke:
	def __init__(self, x, y, image):
		size = random.randint(10, 50)
		rotation = random.randint(0, 360)
		self.image = pygame.transform.rotate(pygame.transform.scale(image, (size, size)), rotation)
		self.x = x
		self.y = y
		self.t = 0

	def draw(self, screen):
		self.image.set_alpha(255-self.t)
		screen.blit(self.image, (self.x, self.y))
		
	def update(self):
		self.t += 1

	def event(self, event):
		return