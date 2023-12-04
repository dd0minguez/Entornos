import pygame
class Nave:
    def __init__(self) -> None:
       self.x=30
       self.y=30
       self.imagen=pygame.image.load("avion.png")
    def moveDerecha(self):
        self.x +=1
    
    def moverIzquierda(self):
        self.x -=1

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))