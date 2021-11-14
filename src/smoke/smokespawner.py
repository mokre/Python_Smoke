import pygame, random
from smoke import smoke

class smokespawner:
	def __init__(self, x, y, smokeimage):
		self.smokeobjects = []
		#self.image = pygame.transform.scale(image, (size, size))
		self.smokeimage = smokeimage
		self.x = x
		self.y = y
		self.t = 0

	def draw(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 10, 10))
		for o in self.smokeobjects:
			o.update()
			o.draw(screen)

	def update(self):
		self.t += 1

	def event(self, event):
		#if player presses left mouse button
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				self.smokeobjects.append(smoke.smoke(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.smokeimage))