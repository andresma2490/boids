import pygame, sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("1629950 - 2711")

boid = pygame.image.load("circle.png")
posX, posY, velocidadX, velocidadY = 10, 10, 5, 5

while True:
    pygame.time.delay(15)
    ventana.fill((0,0,0))
    ventana.blit(boid, (posX, posY))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    if posX > 580 and velocidadX > 0:
        velocidadX *= -1
    if posX < 0 and velocidadX < 0:
        velocidadX *= -1
    if posY > 380 and velocidadY > 0:
        velocidadY *= -1
    if posY < 0 and velocidadY < 0:
        velocidadY *= -1
        
    posX += velocidadX
    posY += velocidadY

    pygame.display.update()
