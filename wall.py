import pygame, math

class Wall():
	def __init__(self, tl, br):
		self.image = pygame.image.load("RSC/Background/mapblock.png")
		width = br[0] - tl[0]
		height = br[1] - tl[1]
		self.image = pygame.transform.scale(self.image, [width, height])	
		self.rect = self.image.get_rect(topleft = tl)
		
		
class Shatterdome():
	def __init__(self, tl, br):
		self.image = pygame.image.load("RSC/Background/shatterdome.png")
		width = br[0] - tl[0]
		height = br[1] - tl[1]
		self.image = pygame.transform.scale(self.image, [width, height])
		self.rect = self. image.get_rect(topleft = tl)
