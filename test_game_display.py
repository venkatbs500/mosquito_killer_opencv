import pygame
import sys
from settings import *
from game import Game

pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

mainClock = pygame.time.Clock()

game = Game(SCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.update()
    pygame.display.update()
    mainClock.tick(FPS)

