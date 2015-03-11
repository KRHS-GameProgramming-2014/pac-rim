import pygame, math
from enemyJaeger import EnemyJaeger

class GipsyDanger(EnemyJaeger):
	def __init__(self, pos):
		image = ("RSC/gispy.png")
        self.maxSpeed = 2
        speedx = random.randint(-self.maxSpeed, self.maxSpeed)
        speedy = random.randint(-self.maxSpeed, self.maxSpeed)
        speed = [speedx, speedy]
        Creature.__init__(self, image, speed, pos)
        self.upImages = [pygame.image.load("RSC/Ghost/GhostUp1.png"),
                            pygame.image.load("RSC/Ghost/GhostUp2.png")]
        self.downImages = [pygame.image.load("RSC/Ghost/GhostDown1.png"),
                            pygame.image.load("RSC/Ghost/GhostDown2.png")]
        self.leftImages = [pygame.image.load("RSC/Ghost/GhostLeft1.png"),
                            pygame.image.load("RSC/Ghost/GhostLeft2.png")]
        self.rightImages = [pygame.image.load("RSC/Ghost/GhostRight1.png"),
                            pygame.image.load("RSC/Ghost/GhostRight2.png")]
        
        if math.fabs(self.speedx) >= math.fabs(self.speedy):
                if self.speedx >= 0:
                    self.facing = "right"
                else:
                    self.facing = "left"
        else:
            if self.speedy >= 0:
                self.facing = "down"
            else:
                self.facing = "up"
        
        self.changed = False
        self.images = self.downImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        
	def update(self, width, height):
        if self.didBounceX or self.didBounceY:
            self.changed = True
            if math.fabs(self.speedx) >= math.fabs(self.speedy):
                if self.speedx >= 0:
                    self.facing = "right"
                else:
                    self.facing = "left"
            else:
                if self.speedy >= 0:
                    self.facing = "down"
                else:
                    self.facing = "up"
        Creature.update(self, width, height)
        self.animate()
        self.changed = False
        
    def collidePlayer(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        pass
        
    def collideDemon(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = False
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = False
                
    def collideLeviathan(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if not self.didBounceX:
                            self.speedx = -self.speedx
                            self.didBouncex = False
                        if not self.didBounceY:
                            self.speedy = -self.speedy
                            self.didBounceY = False
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
        if direction == "down":
            self.facing = "down"
            self.changed = True
        if direction == "left":
           self.facing = "left"
           self.changed = True
        if direction == "right":
            self.facing = "right"
            self.changed = True              


