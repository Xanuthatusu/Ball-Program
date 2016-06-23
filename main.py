import pygame, sys
from pygame.locals import *
from ball import Ball
from loop import *

#initiation for pygame
pygame.init()
SCREENWIDTH = 1800
SCREENHEIGHT = 900
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
CLOCK = pygame.time.Clock()
NUMBALLS = 3

#color assignments
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
BLUE = pygame.Color(0,255,0)
GREEN = pygame.Color(0,0,255)


ball_list = []
for i in range(NUMBALLS):
	ball = Ball(SCREENWIDTH,SCREENHEIGHT)
	if i == 0:
		ball.death = True
		ball.color = BLACK
	ball_list.append(ball)

#main function
def main():
	gox(ball_list,SCREEN,WHITE,RED,CLOCK,(SCREENWIDTH,SCREENHEIGHT))

#calling the main function
main()