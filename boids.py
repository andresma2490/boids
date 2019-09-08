import pygame, sys, random
from pygame.locals import *

pygame.init()
size = width, height = 600, 400
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("1629950 - 2711")

class Boid (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenBoid = pygame.image.load("circle.png")
        self.rect = self.imagenBoid.get_rect()
        self.rect.x = random.randint(0, 500)
        self.rect.y = random.randint(0, 300)
        self.velocidadX = random.randint(3, 6)
        self.velocidadY = random.randint(3, 6)

    def dibujar(self, ventana):
        pygame.time.delay(10)
        ventana.blit(self.imagenBoid, self.rect)
        
        self.rect.x += self.velocidadX
        self.rect.y += self.velocidadY

        if self.rect.centerx < 5 or self.rect.centerx > width-5:
            self.velocidadX = -self.velocidadX
        if self.rect.centery < 5 or self.rect.centery > height-5:
            self.velocidadY = -self.velocidadY


bird = Boid()

while True:
    ventana.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    bird.dibujar(ventana)

    pygame.display.update()
