import pygame, random
import math

class smoke:
	def __init__(self, x, y, mousex, mousey, image):
		size = random.randint(10, 50)
		rotation = random.randint(0, 360)
		self.image = pygame.transform.rotate(pygame.transform.scale(image, (size, size)), rotation)
		self.x = x - size/2
		self.y = y - size/2
		self.v = 0.2																#velocity
		self.t = 0																	#timealive
		self.mt = 1200																#maximum life time
		n = math.sqrt(math.pow(abs(mousex - x), 2) + math.pow(abs(mousey - y), 2))	#norm
		self.dx = (mousex - x)/n													#directionx
		self.dy = (mousey - y)/n													#directionx


	def draw(self, screen):
		self.image.set_alpha(self.mt-self.t)
		screen.blit(self.image, (self.x, self.y))
		
	def update(self, dt):
		self.t += dt
		self.x += (self.dx * self.v / (self.t*0.0002))
		self.y += (self.dy * self.v / (self.t*0.0002))-1

	def event(self, event):
		return