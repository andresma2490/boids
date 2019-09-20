import sys, pygame, random, math
from pygame.locals import *

pygame.init()
size = width, height = 900, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("1629950 - 2711")

borde = 20
arrayBoids = []
numeroBoids = 40

class Boid(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("circle.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)
        self.rect.y = random.randint(0, height)
        self.velocidadX = random.randint(1, 10) 
        self.velocidadY = random.randint(1, 10) 

    def distancia(self, boid):
        distX = self.rect.x - boid.rect.x
        distY = self.rect.y - boid.rect.y
        return math.sqrt(distX **2 + distY **2)

    def cohesion(self, arrayCercanos): #Ir al centro 
        promedioPosX = 0
        promedioPosY = 0
        if len(arrayCercanos) > 0:
            for boid in arrayCercanos:
                if boid.rect.x != self.rect.x and boid.rect.y != self.rect.y:
                    promedioPosX += (self.rect.x - boid.rect.x)
                    promedioPosY += (self.rect.y - boid.rect.y)

            promedioPosX /= len(arrayCercanos)
            promedioPosY /= len(arrayCercanos)

        self.velocidadX -= (promedioPosX / 100)
        self.velocidadY -= (promedioPosY / 100)
    
    def separacion(self, arrayCercanos):     
        distanciaX = 0
        distanciaY = 0
        distanciaMin = 10
        if len(arrayCercanos) > 0:
            for boid in arrayCercanos:
                if self.distancia(boid) < distanciaMin:
                    distanciaX -= boid.rect.x - self.rect.x 
                    distanciaY -= boid.rect.y - self.rect.y

                    self.velocidadX = distanciaX 
                    self.velocidadY = distanciaY 

    def alineacion(self, arrayCercanos): #Moverse en funcion de otros
        if len(arrayCercanos) > 0:
            promedioVelX = 0
            promedioVelY = 0

            for boid in arrayCercanos:
                promedioVelX += boid.velocidadX
                promedioVelY += boid.velocidadY

            promedioVelX /= len(arrayCercanos)
            promedioVelY /= len(arrayCercanos)

            self.velocidadX -= (promedioVelX / 8)
            self.velocidadY -= (promedioVelY / 8) 


# Crea a todos los boids
for i in range(numeroBoids):
    boid = Boid()
    arrayBoids.append(boid)

# Ejecución del programa
run = True
while run:
    ventana.fill((0,0,0))
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    for boid in arrayBoids:
        boidsCercanos = []
        for otroBoid in arrayBoids:
            if boid != otroBoid and boid.distancia(otroBoid) < 200:
                boidsCercanos.append(otroBoid)
    
        # Reglas
        boid.cohesion(boidsCercanos)
        boid.separacion(boidsCercanos)
        boid.alineacion(boidsCercanos)

        # Bordes de la ventana
        if boid.rect.x < borde and boid.velocidadX < 0:
            boid.velocidadX = -boid.velocidadX

        if boid.rect.x > width - borde and boid.velocidadX > 0:
            boid.velocidadX = -boid.velocidadX 

        if boid.rect.y < borde and boid.velocidadY < 0:
            boid.velocidadY = -boid.velocidadY 

        if boid.rect.y > height - borde and boid.velocidadY > 0:
            boid.velocidadY = -boid.velocidadY 

        # Movimiento de los boids
        boid.rect.x += boid.velocidadX
        boid.rect.y += boid.velocidadY

    # Dibuja los boids en la ventana
    for i in arrayBoids:
        ventana.blit(i.image, i.rect)

    pygame.display.update()
