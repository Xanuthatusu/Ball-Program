import pygame,sys
from pygame.locals import *
from ball import *

#main game loop
def gox(ball_list,SCREEN,COLOR,COLOR2,CLOCK,screen_size):
	while True:
		SCREEN.fill(COLOR)
		#event handler
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and event.key == K_k:
				ball_list.append(Ball(screen_size[0],screen_size[1]))
		

		#iterrates through list of balls and does the a function for each one
		for ball in ball_list:
			if ball.alive:
				ball.draw(SCREEN)
				ball.checkEdge()
				for ball2 in ball_list:
					# ball.drawLines(SCREEN,COLOR2,ball,ball_list[l],ball.getAngle(ball,ball_list[l],SCREEN))
					if ball.bounceNextTick and ball2.bounceNextTick:
						ball.bounce(ball2, ball_list)

		pygame.display.update()
		CLOCK.tick(60)
