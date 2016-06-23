import pygame,random,math

#class containing each function for each ball
class Ball():
	#initiate class
	def __init__(self,screenw,screenh):
		self.radius = random.randrange(60,80)
		self.screenw = screenw
		self.screenh = screenh
		self.x = random.randrange(self.radius+1,self.screenw-(self.radius+1))
		self.y = random.randrange(self.radius+1,self.screenh-(self.radius+1))
		self.dx = random.randrange(-10,10)
		self.dy = random.randrange(-10,10)
		self.color = pygame.Color(random.randrange(100,200),random.randrange(100,200),random.randrange(100,200))
		self.surface = pygame.transform.scale(pygame.image.load("papa.png"), (self.radius*2, self.radius*2))
		self.save = self.color
		self.bounceNextTick = False
		self.alive = True
		self.death = False

	#drawing the ball and updating postion
	def draw(self,SCREEN):
		# pygame.draw.circle(SCREEN, self.color, (self.x,self.y), self.radius)
		SCREEN.blit(self.surface, (self.x, self.y))
		self.x += self.dx
		self.y += self.dy
		self.bounceNextTick = False

	#checking to see if the ball is hittting an edge
	def checkEdge(self):
		if self.x + self.dx >= self.screenw-self.radius:
			self.dx = -int(math.fabs(self.dx *- 1))
		if self.x + self.dx <= self.radius:
			self.dx = int(math.fabs(self.dx *- 1))
		if self.y + self.dy >= self.screenh-self.radius:
			self.dy = -int(math.fabs(self.dx *- 1))
		if self.y + self.dy <= self.radius:
			self.dy = int(math.fabs(self.dy *- 1))

	#CopyRight David Dursteler 2015
	#Checks to see if two balls are touching each other
	def areColliding(self, ball2):
		#checks if 2 positions are within colliding distance based on radius using pythagorean theorem
		ball1FutureX = self.x + self.dx
		ball1FutureY = self.y + self.dy
		ball2FutureX = ball2.x + ball2.dx
		ball2FutureY = ball2.y + ball2.dy
		if ((ball1FutureX - ball2FutureX) ** 2 + (ball1FutureY - ball2FutureY) ** 2) ** .5 <= self.radius + ball2.radius:
			self.bounceNextTick = True
			ball2.bounceNextTick = True

	def bounce(self, ball2, ball_list):
		if self.death:
			ball_list.remove(ball2)
			self.radius += 1
		elif ball2.death:
			ball_list.remove(self)
			ball2.radius += 1
		else:
			self.dx *= -1
			self.dy *= -1
			ball2.dx *= -1
			ball2.dy *= -1