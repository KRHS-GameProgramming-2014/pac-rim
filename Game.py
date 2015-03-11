import pygame, sys, random
from playerKaiju import PlayerKaiju
from enemyJaeger import EnemyJaeger
from wall import Block, Level
from MainMenu import Button
pygame.init()
win = False

clock = pygame.time.Clock()

width = 896
height = 640
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)



bgImage = pygame.image.load("RSC/menues/mainmenu.png").convert()
bgRect = bgImage.get_rect()

playButton = Button([width/2, height-350], 
                                     "RSC/menues/button.png", 
                                     "RSC/menues/buttonpressed.png")

bgImage = pygame.image.load("RSC/Background/Sheet.png").convert()
bgImage = pygame.transform.scale(bgImage, size)
bgRect = bgImage.get_rect()

level = Level("Level", size)

player = level.player

enemy = []
enemy += level.jaegers
run = False
while True:
	
	while not run:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                    run = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            playButton.click(event.pos)
                    if event.type == pygame.MOUSEBUTTONUP:
                            if playButton.release(event.pos):
                                    run = True
            bgColor = r,g,b
            screen.fill(bgColor)
            screen.blit(bgImage, bgRect)
            screen.blit(playButton.image, playButton.rect)
            pygame.display.flip()
            clock.tick(60)
	
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
		"""			
		if len(enemy) < 3:
			if random.randint(0, 1*60) == 0:
				 enemy += [EnemyJaeger("RSC/Jaeger/gispy.png", "RSC/Jaeger/chernoWIP", "RSC/Jaeger/strikerWIP.png",
							[random.randint(0,10), random.randint(0,10)],
							[random.randint(100, width-100), random.randint(100, height-100)])
							]
		"""
		
		player.update(width, height)
		#for enemyJaeger in enemy:
		#	enemyJaeger.update(width, height)
			
		#for EnemyJaeger in enemy:
		#	if not EnemyJaeger.living:
		#		enemy.remove(EnemyJaeger)
		
		for block in level.hardBlocks:
			for playerkaiju in PlayerKaiju:
				if block.playerCollide(player):
					player.go("stop")
		
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		for enemyJaeger in enemy:
			screen.blit(enemyJaeger.image, enemyJaeger.rect)
		for block in level.blocks:
			screen.blit(block.image, block.rect)
		screen.blit(player.image, player.rect)
		pygame.display.flip()
		clock.tick(60)
