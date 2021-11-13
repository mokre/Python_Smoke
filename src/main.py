import pygame

def main():
	screenSize = (720, 420)
	running = True

	pygame.init()
	pygame.display.set_caption("Python Smoke")
	screen = pygame.display.set_mode(screenSize)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	pygame.quit()
	return

if __name__ == "__main__":
	main()