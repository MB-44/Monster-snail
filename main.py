import pygame
from sys import exit 

def displayScore():
    currentTime = int(pygame.time.get_ticks()/1000) - startTime
    scoreSurface = fontType.render("Score: "+str(currentTime),False,(64,64,64))
    scoreRect = scoreSurface.get_rect(center = (400,50))
    screen.blit(scoreSurface,scoreRect)
    return currentTime

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Escape from snail")
clock = pygame.time.Clock()
fontType = pygame.font.Font('font/Pixeltype.ttf',40)
gameActive = False
startTime = 0
score = 0

skySurface = pygame.image.load('imgs/sky.png').convert()
groundSurface = pygame.image.load('imgs/ground.png').convert()

snail = pygame.image.load('imgs/snail.png').convert_alpha()
snailRect = snail.get_rect(bottomright=(600,300))

charWalk = pygame.image.load('imgs/charWalk1.png').convert_alpha()
charWalkRect = charWalk.get_rect(bottomleft=(50,300))
charGravity = 0

charStand = pygame.image.load('imgs/charStand.png').convert_alpha()
charStandRect = charStand.get_rect(center = (400,200))
charJump = pygame.image.load('imgs/charJump.png').convert_alpha()
charJumpRect = charJump.get_rect(center = (500,200))
charWalk2 = pygame.image.load('imgs/charWalk2.png').convert_alpha()
charWalk2Rect = charWalk2.get_rect(center = (300,200))

gameName = fontType.render("Escape from snail",False,"darkgreen")
gameNameRect = gameName.get_rect(center = (400,120))

gameMsg = fontType.render("-- PRESS SPACE TO START --",False,(111,196,169))
gameMsgRect = gameMsg.get_rect(center=(400,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if gameActive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (charWalkRect.collidepoint(event.pos)) and (charWalkRect.bottom >= 301):
                    charGravity = -20

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and (charWalkRect.bottom >= 301):
                    charGravity = -20    

        else: 
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
                gameActive = True
                snailRect.right = 800
                startTime  = int(pygame.time.get_ticks()/1000)

    if gameActive:
        screen.blit(skySurface,(0,0))
        screen.blit(groundSurface,(0,301))   
        score = displayScore()

        snailRect.x -= 5 
        if snailRect.left < 1:
            snailRect.right = 800
        screen.blit(snail,snailRect)

        charGravity += 1
        charWalkRect.y += charGravity
        if charWalkRect.bottom >= 301:
            charWalkRect.bottom = 301
        screen.blit(charWalk,charWalkRect)

        # snail touch the player
        if snailRect.colliderect(charWalkRect):
            gameActive = False

    else: 
        screen.fill((94,129,162))
        screen.blit(charStand,charStandRect)
        screen.blit(charJump,charJumpRect)
        screen.blit(charWalk2,charWalk2Rect)
        screen.blit(gameName,gameNameRect)

        scoreMsg = fontType.render(f"Your Score: {score}",False,("yellow"))
        scoreMsgRect =  scoreMsg.get_rect(center = (400,330))

        if score == 0:
            screen.blit(gameMsg,gameMsgRect)
        else: 
            screen.blit(scoreMsg,scoreMsgRect)

    pygame.display.update()
    clock.tick(60)