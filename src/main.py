import pygame, sys, os
from smoke import smoke
from smoke import smokespawner

def main():
	screenSize = (720, 420)
	dt = 0
	running = True
	objects = []

	pygame.init()
	pygame.display.set_caption("Python Smoke by Moritz Kress")
	pygame.display.set_icon(pygame.image.load('../res/python_smoke_logo.png'))
	screen = pygame.display.set_mode(screenSize)
	clock = pygame.time.Clock()
	smokeimage = pygame.image.load(os.path.join(sys.path[0], '../res/smoke.png'))

	while running:
		screen.fill((0, 0, 0))

		#handle events
		for event in pygame.event.get():
			#close the game when the player closes the window
			if event.type == pygame.QUIT:
				running = False
			#if player presses left mouse button
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 3:
					objects.append(smokespawner.smokespawner(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], smokeimage))

			#handle events for objects
			for o in objects:
				o.event(event)
		
		#loop through objects
		for o in objects:
			o.update(dt)
			o.draw(screen)
		
		screen.blit(pygame.font.SysFont("Arial", 10).render(str(int(clock.get_fps())), 1, pygame.Color(255, 255, 255)), (0,0))
		dt = clock.tick(6000)
		pygame.display.flip()

	pygame.quit()
	return

if __name__ == "__main__":
	main()