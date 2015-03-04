import pygame, math
from enemyJaeger import EnemyJaeger

class GipsyDanger(EnemyJaeger):
	def __init__(self, pos):
		EnemyJaeger.__init__(self, "RSC/gispy.png", [0,0], pos)
        self.speedx = 0
        self.speedy = 2
        self.upImages = [pygame.image.load("RSC/Jaeger/gispy2.png"),
                            pygame.image.load("RSC/Jaeger/gispy3.png")]
        self.downImages = [pygame.image.load("RSC/Jaeger/gispy2.png"),
                            pygame.image.load("RSC/Jaeger/gispy3.png")]
        self.leftImages = [pygame.image.load("RSC/Jaeger/gispy2.png"),
                            pygame.image.load("RSC/Jaeger/gispy3.png")]
        self.rightImages = [pygame.image.load("RSC/Jaeger/gispy2.png"),
                            pygame.image.load("RSC/Jaeger/gispy3.png")]

RSC/Jaeger/gispy3.png
