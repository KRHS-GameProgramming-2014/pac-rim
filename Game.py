import pygame, sys, random
from enemyJaeger import enemyJaeger
from playerKaiju import PlayerKaiju

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600
size = width, height

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("RSC/Background/Sheet.png").convert()
bgRect = bgImage.get_rect()

while True:
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
	
    for ball in balls:
		screen.blit(ball.image, ball.rect)
	screen.blit(player.image, player.rect)
	screen.blit(timer.image, timer.rect)
	screen.blit(score.image, score.rect)
	pygame.display.flip()
	clock.tick(60)

