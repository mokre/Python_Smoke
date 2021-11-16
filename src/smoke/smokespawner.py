import pygame, random
from smoke import smoke

class smokespawner:
	def __init__(self, x, y, smokeimage):
		self.smokeobjects = []
		self.smokeimage = smokeimage
		self.x = x-5
		self.y = y-5
		self.t = 0

	def draw(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 10, 10))
		for o in self.smokeobjects:
			o.draw(screen)

	def update(self, dt):
		self.t += dt
		for o in self.smokeobjects:
			o.update(dt)
			if o.t >= o.mt:
				self.smokeobjects.remove(o)

		if pygame.mouse.get_pressed(num_buttons=3)[0]:
			self.smokeobjects.append(smoke.smoke(self.x, self.y, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.smokeimage))

	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				self.smokeobjects.append(smoke.smoke(self.x, self.y, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.smokeimage))