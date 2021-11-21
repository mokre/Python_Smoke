import pygame, random
import math

class smoke:
	def __init__(self, x, y, mousex, mousey, image):
		self.size = random.randint(10, 50)
		self.rotation = random.randint(0, 360)
		self.image = pygame.transform.rotate(pygame.transform.scale(image, (self.size, self.size)), self.rotation)
		self.x = x
		self.y = y 
		self.alpha = random.randint(0, 255)
		self.t = 0																	#timealive
		self.mt = 4000																#maximum life time
		n = math.sqrt(math.pow(abs(mousex - x), 2) + math.pow(abs(mousey - y), 2))	#norm
		self.dx = (mousex - x)/n													#directionx
		self.dy = (mousey - y)/n													#directionx


	def draw(self, screen):
		self.image.set_alpha(self.alpha - (self.alpha * self.t / self.mt))
		#more realistic but resource intensive
		#screen.blit(pygame.transform.scale(self.image, (self.size, self.size)), (self.x - self.size/2, self.y - self.size/2))
		screen.blit(self.image, (self.x - self.size/2, self.y - self.size/2))
		
	def update(self, dt):
		self.t += dt
		#position
		v = 50 / self.t 
		self.x += (self.dx * v * dt)
		self.y += (self.dy * v * dt) - 0.2
		#orientation more realistic but resource intensive
		#self.size = random.randint(self.size, self.size + 1)

	def event(self, event):
		return