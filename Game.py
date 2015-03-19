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

playButton = Button([width/2, height-425], 
                                     "RSC/menues/button.png", 
                                     "RSC/menues/buttonpressed.png")

bgImage = pygame.image.load("RSC/menues/mainmenu.png").convert()
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
		
		player.update(width, height)
		for enemyJaeger in enemy:
			enemyJaeger.update(width, height)
		
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
