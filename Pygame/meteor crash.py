import pygame
import random

# intialize pygame
pygame.init()

# window
wn = pygame.display.set_mode((1000, 600))

# title and icon
pygame.display.set_caption('meteor crash')
icon = pygame.image.load('meteor.png')
pygame.display.set_icon(icon)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False