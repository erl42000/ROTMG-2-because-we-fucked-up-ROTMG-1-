import pygame
import sys
import os
from time import sleep
from math import asin, acos, sin, cos, pi, sqrt, hypot
from random import randint

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

screen       = pygame.display.set_mode((800, 600))

class Character:

    def __init__(self):

        self.leftCounter = 0
        self.rightCounter = 0
        self.upCounter = 0
        self.downCounter = 0
        self.lastDirection = "right"
        self.characterSprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()

    #def __init__(self, hp, mp, deff, vit, wis, dex, att, spd):
    #    self.hp = hp;
    #    self.mp = mp;
    #    self.deff = deff;
    #    self.vit = vit;
    #    self.wis = wis;
    #    self.dex = dex;
    #    self.att = att;
    #    self.spd = spd;

    #def shoot():
    #    pass
<<<<<<< HEAD
            
    def rightWalk(self):
        
        self.lastDirection = "right"
=======

    def leftWalk(self):

        self.leftCounter += 1
        if self.leftCounter < 10:
            self.characterSprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()
        elif self.leftCounter < 20:
            self.characterSprite = pygame.image.load("ArcherWalkLeft2.png").convert_alpha()
        else:
            self.leftCounter = 0

    def rightWalk(self):

>>>>>>> origin/master
        self.rightCounter += 1
        if self.rightCounter < 10:
            self.characterSprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()
        elif self.rightCounter < 20:
            self.characterSprite = pygame.image.load("ArcherWalkRight2.png").convert_alpha()
        else:
            self.rightCounter = 0

<<<<<<< HEAD
    def leftWalk(self):
        
        self.lastDirection = "left"
        self.leftCounter += 1
        if self.leftCounter < 10:
            self.characterSprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()
        elif self.leftCounter < 20:
            self.characterSprite = pygame.image.load("ArcherWalkLeft2.png").convert_alpha()
        else:
            self.leftCounter = 0
            
    def upWalk(self):
        
        self.lastDirection = "up"
=======
    def upWalk(self):

>>>>>>> origin/master
        self.upCounter += 1
        if self.upCounter < 10:
            self.characterSprite = pygame.image.load("ArcherWalkUp1.png").convert_alpha()
        elif self.upCounter < 20:
            self.characterSprite = pygame.image.load("ArcherWalkUp2.png").convert_alpha()
        else:
            self.upCounter = 0

    def downWalk(self):
<<<<<<< HEAD
        
        self.lastDirection = "down"
=======

>>>>>>> origin/master
        self.downCounter += 1
        if self.downCounter < 10:
            self.characterSprite = pygame.image.load("ArcherWalkDown1.png").convert_alpha()
        elif self.downCounter < 20:
            self.characterSprite = pygame.image.load("ArcherWalkDown2.png").convert_alpha()
        else:
            self.downCounter = 0

    def leftShoot(self):

        self.leftCounter += 1
        if self.leftCounter < 10:
            self.characterSprite = pygame.image.load("ArcherShootLeft1.png").convert_alpha()
        elif self.leftCounter < 20:
            self.characterSprite = pygame.image.load("ArcherShootLeft2.png").convert_alpha()
        else:
            self.leftCounter = 0

    def rightShoot(self):

        self.rightCounter += 1
        if self.rightCounter < 10:
            self.characterSprite = pygame.image.load("ArcherShootRight1.png").convert_alpha()
        elif self.rightCounter < 20:
            self.characterSprite = pygame.image.load("ArcherShootRight2.png").convert_alpha()
        else:
            self.rightCounter = 0

    def upShoot(self):

        self.upCounter += 1
        if self.upCounter < 10:
            self.characterSprite = pygame.image.load("ArcherShootUp1.png").convert_alpha()
        elif self.upCounter < 20:
            self.characterSprite = pygame.image.load("ArcherShootUp2.png").convert_alpha()
        else:
            self.upCounter = 0

    def downShoot(self):

        self.downCounter += 1
        if self.downCounter < 10:
            self.characterSprite = pygame.image.load("ArcherShootDown1.png").convert_alpha()
        elif self.downCounter < 20:
            self.characterSprite = pygame.image.load("ArcherShootDown2.png").convert_alpha()
        else:
            self.downCounter = 0

    def release(self):
        self.leftCounter = 0
        self.rightCounter = 0
        self.downCounter = 0
        self.upCounter = 0

        if self.lastDirection == "right":
            
            self.characterSprite = pygame.image.load("ArcherWalkRight1.png").convert_alpha()

        elif self.lastDirection == "left":
            
            self.characterSprite = pygame.image.load("ArcherWalkLeft1.png").convert_alpha()

        elif self.lastDirection == "up":
            
            self.characterSprite = pygame.image.load("ArcherWalkUp1.png").convert_alpha()
    
        elif self.lastDirection == "down":
            
            self.characterSprite = pygame.image.load("ArcherWalkDown1.png").convert_alpha()


red          = (255,  0,  0)
green        = (  0,255,  0)
blue         = (  0,  0,255)
white        = (255,255,255)
black        = (  0, 0,  0)
grey         = (127,127,127)

tileList    = [black, white, grey, red, green, blue]

sidebar      = 600, 0, 200, 800
character    = Character()
characterXY  = 275, 275, 50, 50

tileLength   = 50

centerX      = 300
centerY      = 300

frame        = 0
shotDelay    = 15
lastClick    = -60

projectileList  = []

map_ = open("ROTMG_Map.txt", "r")
mapList = [line.rstrip('\n') for line in map_]
map_.close()

for i in range(0, len(mapList)):

    mapList[i] = list(mapList[i])

mapWidth  = len(mapList) * tileLength
mapHeight = len(mapList[0]) * tileLength

xPos = (mapWidth) / 2
yPos = (mapHeight) / 2

ended = False

step = 0

while not ended:

    screen.fill(black)

    for x in range(-6,7):

        for y in range(-6,7):

            if (xPos / 50) + x < 0 or (yPos / 50) + y < 0:

                pygame.draw.rect(screen, black, (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), +  tileLength, tileLength))

            else:

                try:

                    pygame.draw.rect(screen, tileList[int(mapList[(xPos / 50) + x][(yPos / 50) + y])], (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), +  tileLength, tileLength))

                except IndexError:

                    pygame.draw.rect(screen, black, (((x + 6) * tileLength) - (xPos % 50), (((y + 6) * tileLength) - (yPos % 50)), +  tileLength, tileLength))

    keyDown = pygame.key.get_pressed()

    if keyDown[pygame.K_w]:

        character.upWalk()

        yPos = max(0, yPos - 5)

    if keyDown[pygame.K_s]:

        character.downWalk()

        yPos = min(mapHeight, yPos + 5)

    if keyDown[pygame.K_a]:

        character.leftWalk()

        xPos = max(0, xPos - 5)

    if keyDown[pygame.K_d]:

        character.rightWalk()

        xPos = min(mapWidth, xPos + 5)

    if keyDown[pygame.K_SPACE]:

        pass

    if pygame.mouse.get_pressed()[0]:

        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseY - 300 >= abs(mouseX - 300):

            character.downShoot()

        elif mouseX - 300 >= abs(mouseY - 300):

            character.rightShoot()

        elif -mouseY + 300 >= abs(mouseX - 300):

            character.upShoot()

        elif -mouseX + 300 >= abs(mouseY - 300):

            character.leftShoot()

        if frame >= lastClick + shotDelay:

            lastClick = frame

            projectile = []

            xLength = centerX - mouseX
            yLength = centerY - mouseY
            distance = hypot(xLength, yLength)

            try:

                angle = acos(xLength / distance)

            except ZeroDivisionError:

                angle = 0

            if yLength < 0:

                angle = 2 * pi - angle

            lifespan = 30

            x = 300
            y = 300

            projectile.append(angle)
            projectile.append(lifespan)
            projectile.append(x)
            projectile.append(y)

            projectileList.append(projectile)

    for i in projectileList:

        pygame.draw.circle(screen, red, (int(i[2]), int(i[3])), 8)

<<<<<<< HEAD
<<<<<<< HEAD
        i[2] -= 10 * cos(i[0])
        i[3] -= 10 * sin(i[0])
=======
        i[2] -= 10 * cos(i[0]) + xPos
        i[3] -= 10 * sin(i[0]) + yPos

>>>>>>> origin/master
=======
        i[2] -= 10 * cos(i[0]) + (((x + 6) * tileLength) - (xPos % 50)
        i[3] -= 10 * sin(i[0]) + (((x + 6) * tileLength) - (yPos % 50)

>>>>>>> parent of 3eb92c6... lots
        i[1] -= 1

        if i[1] <= 0:

            projectileList.remove(i)

    if pygame.mouse.get_pressed()[0]:

        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseY - 300 >= abs(mouseX - 300):

            character.downShoot()
        
        elif mouseX - 300 >= abs(mouseY - 300):

            character.rightShoot()

        elif -mouseY + 300 >= abs(mouseX - 300):

            character.upShoot()

        elif -mouseX + 300 >= abs(mouseY - 300):

            character.leftShoot()

    elif keyDown[pygame.K_w] and keyDown[pygame.K_a]:

        pass

    elif keyDown[pygame.K_w] and keyDown[pygame.K_d]:

        pass

    elif keyDown[pygame.K_s] and keyDown[pygame.K_a]:

        pass

    elif keyDown[pygame.K_s] and keyDown[pygame.K_d]:

        pass

    elif keyDown[pygame.K_w]:

        pass

    elif keyDown[pygame.K_s]:

        pass

    elif keyDown[pygame.K_a]:

        pass

    elif keyDown[pygame.K_d]:

        pass

    else:

        character.release()

    pygame.draw.rect(screen, grey, sidebar)
    screen.blit(character.characterSprite, characterXY)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            ended = True

    pygame.display.flip()

    sleep(1.0/60)

    frame += 1

pygame.quit()
