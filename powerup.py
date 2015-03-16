import pygame

class PowerUp():
	def __init__(self, image, pos = [0,0]):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		
		
	def collidePlayer(self, other):
		if PlayerKaiju.isPowered:
			if self.rect.right > PlayerKaiju.rect.left and self.rect.left < PlayerKaiju.rect.right:
				if self.rect.bottom > PlayerKaiju.rect.top and self.rect.top < PlayerKaiju.rect.bottom:
					if (self.radius + PlayerKaiju.radius) > self.distance(PlayerKaiju.rect.center):
						self.living = False
		else:
			if self.rect.right > PlayerKaiju.rect.left and self.rect.left < PlayerKaiju.rect.right:
				if self.rect.bottom > PlayerKaiju.rect.top and self.rect.top < PlayerKaiju.rect.bottom:
					if (self.radius + PlayerKaiju.radius) > self.distance(PlayerKaiju.rect.center):
						self.living = True
		
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
