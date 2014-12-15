import pygame
from enemyJaeger import enemyJaeger

class PlayerKaiju(enemyJaeger):
	def __init__(self, pos):
		Ball.__init__(self, "RSC/Kaiju/leatherback.png", [0,0], pos)
		self.images = [pygame.image.load("RSC/Kaiju/leatherback.png"),
						 pygame.image.load("RSC/Kaiju/leatherback2.png")]
		self.facing = "right"
		self.changed = False
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.images = self.upImages
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
		self.pu = False
			
	def update(self, width, height):
		Ball.update(self, width, height)
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
	
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += 2
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
			
	def collideJaeger(self, jaeger):
		if self.isPowered:
			if self.rect.right > jaeger.rect.left and self.rect.left < jaeger.rect.right:
				if self.rect.bottom > jaeger.rect.top and self.rect.top < jaeger.rect.bottom:
					if (self.radius + jaeger.radius) > self.distance(jaeger.rect.center):
						self.living = False
		else:
			if self.rect.right > jaeger.rect.left and self.rect.left < jaeger.rect.right:
				if self.rect.bottom > jaeger.rect.top and self.rect.top < jaeger.rect.bottom:
					if (self.radius + jaeger.radius) > self.distance(jaeger.rect.center):
						self.living = True
