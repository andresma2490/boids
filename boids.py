import pygame, sys, random
from pygame.locals import *

pygame.init()
size = width, height = 900, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("1629950 - 2711")

borde = 10
arrayBoids = []
numberoBoids = 25

class Boid (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenBoid = pygame.image.load("circle.png")
        self.rect = self.imagenBoid.get_rect()
        self.rect.x = random.randint(10, width-10)
        self.rect.y = random.randint(10, height-10)
        self.velocidadX = random.randint(3, 6)
        self.velocidadY = random.randint(3, 6)
        

    def dibujar(self, ventana):
        ventana.blit(self.imagenBoid, self.rect)

        self.rect.x += self.velocidadX
        self.rect.y += self.velocidadY

        if self.rect.x < borde and self.velocidadX < 0:
            self.velocidadX = -self.velocidadX 
            
        if self.rect.x > width - borde and self.velocidadX > 0:
            self.velocidadX = -self.velocidadX 
            
        if self.rect.y < borde and self.velocidadY < 0:
            self.velocidadY = -self.velocidadY 
            
        if self.rect.y > height - borde and self.velocidadY > 0:
            self.velocidadY = -self.velocidadY 

for i in range(0, numberoBoids):
	arrayBoids.append(Boid())

while True:
    ventana.fill((0, 0, 0))
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    for boid in arrayBoids:
        boid.dibujar(ventana)

        for otroBoid in arrayBoids:
            if boid != otroBoid:
                if boid.rect.colliderect(otroBoid): #Si chocan dos boids distintos
                    boid.velocidadX = -boid.velocidadX
                    boid.velocidadY = -boid.velocidadY
        

    pygame.display.update()
