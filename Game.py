import pygame, sys, random
from playerKaiju import PlayerKaiju
from enemyJaeger import EnemyJaeger

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("RSC/Background/Sheet.png").convert()
bgImage = pygame.transform.scale(bgImage, size)
bgRect = bgImage.get_rect()

player = PlayerKaiju([width/2, height/2])

enemy = []
enemy2 = enemy3 = enemy
enemy += [EnemyJaeger("RSC/Jaeger/gispy.png", [5,3], [100,125])]
enemy2 += [EnemyJaeger("RSC/Jaeger/chernoWIP.png", [2,1], [190,125])]
enemy3 += [EnemyJaeger("RSC/Jaeger/strikerWIP.png", [7,9], [134,165])]
run = True

while True:
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("left")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("stop left")
					
		if len(enemy) < 3:
			if random.randint(0, 1*60) == 0:
				 enemy += [EnemyJaeger("RSC/Jaeger/gispy.png", "RSC/Jaeger/chernoWIP", "RSC/Jaeger/strikerWIP.png",
							[random.randint(0,10), random.randint(0,10)],
							[random.randint(100, width-100), random.randint(100, height-100)])
							]
	
		player.update(width, height)
		for enemyJaeger in enemy:
			enemyJaeger.update(width, height)
		
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		for enemyJaeger in enemy:
			screen.blit(enemyJaeger.image, enemyJaeger.rect)
		screen.blit(player.image, player.rect)
		pygame.display.flip()
		clock.tick(60)
