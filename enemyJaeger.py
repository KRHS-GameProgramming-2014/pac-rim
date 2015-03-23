import pygame, math, random

class EnemyJaeger():
	def __init__(self, image, speed = [0,0], pos = [0,0]):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.speedx = speed[0]
		self.speedy = speed[1]
		self.speed = [self.speedx, self.speedy]
		if self.speedx > 0:
			self.facing = "right"
		elif self.speedy < 0:
			self.facing = "left"
		elif self.speedy > 0:
			self.facing = "down"
		else:
			self.facing = "up"
		self.place(pos)
		self.didBounceX = False
		self.didBounceY = False
		self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
		self.living = True
		
	def place(self, pos):
		self.rect.center = pos
		
	def update(self, width, height):
		self.didBounceX = False
		self.didBounceY = False
		if self.facing == "right":
			self.speed = [5,0]
		elif self.facing == "left":
			self.speed = [-5,0]
		elif self.facing == "up":
			self.speed = [0,-5]
		elif self.facing == "down":
			self.speed = [0,5]
		self.speedx = self.speed[0]
		self.speedy = self.speed[1]
		self.move()
		#self.collideWall(width, height)
	
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += .55
		else:
			self.waitCount = 0
			self.facingChanged = True
			if self.frame < self.maxFrame:
				self.frame += 1
			else:
				self.frame = 0
			self.image = self.images[self.frame]
		
	def move(self):
		self.speed = [self.speedx, self.speedy]
		self.rect = self.rect.move(self.speed)
		
	def collideBlock(self, other):
		if (self.rect.right > other.rect.left and self.rect.left < other. rect.right):
			if (self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom):
				self.speedx = -self.speedx
				self.speedy = -self.speedy
				self.move()
				self.move()
				num = random.randint(0,1)
				if self.facing == "up" or self.facing == "down":
					if num == 0:
						self.facing = "right"
					else:
						self.facing = "left"
				if self.facing == "right" or self.facing == "left":
					if num == 0:
						self.facing = "up"
					else:
						self.facing = "down"
				self.collideWall = True
		return False
						
	def collidePlayer(self, other):
		if PlayerKaiju.isPowered:
			if self.rect.right > PlayerKaiju.rect.left and self.rect.left < PlayerKaiju.rect.right:
				if self.rect.bottom > PlayerKaiju.rect.top and self.rect.top < PlayerKaiju.rect.bottom:
					if (self.radius + PlayerKaiju.radius) > self.distance(PlayerKaiju.rect.center):
						self.living = True
		
		else:
			if self.rect.right > PlayerKaiju.rect.left and self.rect.left < PlayerKaiju.rect.right:
				if self.rect.bottom > PlayerKaiju.rect.top and self.rect.top < PlayerKaiju.rect.bottom:
					if (self.radius + PlayerKaiju.radius) > self.distance(PlayerKaiju.rect.center):
						self.living = True
						PlayerKaiju.living = False
	
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[1]
		x2 = pt[0]
		y2 = pt[1]
		return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
