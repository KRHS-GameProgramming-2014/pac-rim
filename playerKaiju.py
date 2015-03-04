import pygame

class PlayerKaiju():
	def __init__(self, pos):
		self.upImages = [pygame.image.load("RSC/Kaiju/leatherback.png"),
						pygame.image.load("RSC/Kaiju/leatherback2.png")]
		self.downImages = [pygame.image.load("RSC/Kaiju/leatherback.png"),
						pygame.image.load("RSC/Kaiju/leatherback2.png")]
		self.leftImages = [pygame.image.load("RSC/Kaiju/leatherback.png"),
						pygame.image.load("RSC/Kaiju/leatherback2.png")]
		self.rightImages = [pygame.image.load("RSC/Kaiju/leatherback.png"),
						pygame.image.load("RSC/Kaiju/leatherback2.png")]												
		self.facing = "right"
		self.changed = False
		self.images = self.rightImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect()
		self.maxSpeed = 4
		self.pu = False
		self.speedx = 0
		self.speedy = 0
		self.speed = [self.speedx, self.speedy]
		self.place(pos)
		self.didBounceX = False
		self.didBounceY = False
		self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
		self.living = True
			
	def update(self, width, height):
		self.didBounceX = False
		self.didBounceY = False
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
		self.animate()
		self.facingChanged = False
		
	def collideWall(self, width, height):
		if not self.didBounceX:
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = 0
				self.didBounceX = True
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = 0
				self.didBounceY = True
				
	def collideJaeger(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = False				
		else:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = True					
	
	def place(self, pos):
		self.rect.center = pos
	
	def move(self):
		self.rect = self.rect.move(self.speed)
	
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
	
	def go(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
		elif direction == "down":
			self.facing = "down"
			self.changed = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
			
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0
			
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[1]
		x2 = pt[0]
		y2 = pt[1]
		return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
		
