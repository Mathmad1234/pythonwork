import Pygame
import random

# intialize pygame
Pygame.init()

# window
wn = Pygame.display.set_mode((600, 800))

# main game loop
running = True
while running:
    for event in Pygame.event.get():
        if Pygame.type == Pygame.QUIT:
            running = False