import pygame, math

class EnemyJaeger():
	def __init__(self, image, speed = [0,0], pos = [0,0]):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.speedx = speed[0]
		self.speedy = speed[1]
		self.speed = [self.speedx, self.speedy]
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
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
	
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
			#self.image = self.images[self.frame]
		
	def move(self):
		self.rect = self.rect.move(self.speed)
		
	def collideWall(self, width, height):
		if not self.didBounceX:
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = -self.speedx
				self.didBounceX = True
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = -self.speedy
				self.didBounceY = True
						
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
