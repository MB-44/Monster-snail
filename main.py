import pygame
from settings import *
from sys import exit 

def displayScore():
    currentTime = int(pygame.time.get_ticks()/1000) - startTime
    scoreSurface = fontType.render("Score: "+str(currentTime),False,(64,64,64))
    scoreRect = scoreSurface.get_rect(center = (400,50))
    screen.blit(scoreSurface,scoreRect)
    return currentTime

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape from snail")
clock = pygame.time.Clock()
fontType = pygame.font.Font('font/Pixeltype.ttf', FONT_SIZE)
gameActive = False
startTime = 0
score = 0

skySurface = pygame.image.load('imgs/sky.png').convert()
groundSurface = pygame.image.load('imgs/ground.png').convert()

snail = pygame.image.load('imgs/snail.png').convert_alpha()
snailRect = snail.get_rect(bottomright=(SNAIL_POSITION_X, SNAIL_POSITION_Y))

playerWalk = pygame.image.load('./imgs/charWalk1.png').convert_alpha()
playerWalkRect = playerWalk.get_rect(bottomleft=(PLAYER_POSITION_X, PLAYER_POSITION_Y))
playerGravity = 0

playerStand = pygame.image.load('imgs/charStand.png').convert_alpha()
playerStandRect = playerStand.get_rect(center = (PLAYER_STAND_POSITION_X, PLAYER_STAND_POSITION_Y))

playerJump = pygame.image.load('imgs/charJump.png').convert_alpha()
playerJumpRect = playerJump.get_rect(center = (PLAYER_JUMP_POSITION_X, PLAYER_JUMP_POSITION_Y))

playerWalk2 = pygame.image.load('imgs/charWalk2.png').convert_alpha()
playerWalk2Rect = playerWalk2.get_rect(center = (300, 200))

gameName = fontType.render("Escape from snail", False, "darkgreen")
gameNameRect = gameName.get_rect(center = (400, 120))

gameMsg = fontType.render("-- PRESS SPACE TO START --", False, (111, 196, 169))
gameMsgRect = gameMsg.get_rect(center=(400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if gameActive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (playerWalk.collidepoint(event.pos)) and (playerWalk.bottom >= 301):
                    playerGravity = -20

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and (playerWalk.bottom >= 301):
                    playerGravity = -20    

        else: 
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
                gameActive = True
                snailRect.right = 800
                startTime  = int(pygame.time.get_ticks()/1000)

    if gameActive:
        screen.blit(skySurface,(0, 0))
        screen.blit(groundSurface,(0, 301))   
        score = displayScore()

        snailRect.x -= 5 
        if snailRect.left < 1:
            snailRect.right = 800
        screen.blit(snail, snailRect)

        playerGravity += 1
        playerWalk.y += playerGravity
        if playerWalk.bottom >= 301:
            playerWalk.bottom = 301
        screen.blit(playerWalk, playerWalk)

        # snail touch the player
        if snailRect.colliderect(playerWalk):
            gameActive = False

    else: 
        screen.fill((94, 129, 162))
        screen.blit(playerStand, playerStandRect)
        screen.blit(playerJump, playerJumpRect)
        screen.blit(playerWalk2, playerWalk2Rect)
        screen.blit(gameName, gameNameRect)

        scoreMsg = fontType.render(f"Your Score: {score}", False, ("yellow"))
        scoreMsgRect =  scoreMsg.get_rect(center = (400, 330))

        if score == 0:
            screen.blit(gameMsg, gameMsgRect)
        else: 
            screen.blit(scoreMsg, scoreMsgRect)

    pygame.display.update()
    clock.tick(FPS)