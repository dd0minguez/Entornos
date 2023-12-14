from typing import Any
import pygame

class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion) -> None:
        super().__init__()

        #cargamos la imagen
        self.imagenes = [pygame.image.load("nave1.png"), pygame.image.load("nave1.png")]
        self.imagenes_scaled = [pygame.transform.scale(self.imagenes[0], (80, 80)), pygame.transform.scale(self.imagenes[1], (80, 80))]
        self.indice_imagenes = 0
        self.image = self.imagenes_scaled[self.indice_imagenes]

        self.contador_imagen = 0
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posicion del rectangulo para que coincida con posicion
        self.rect.topleft = posicion
        #teclas

    def moveDerecha(self):
        self.rect.x +=1
        pantalla = pygame.display.get_surface()
        limite=pantalla.get_width()
        self.rect.x=min(self.rect.x, limite-self.image.get_width())
    
    #def moverIzquierda(self):
        #self.rect.x -=1
        #pantalla = pygame.display.get_surface()
        #limite=0
        #self.rect.x=max(self.rect.x, limite)
    
        #update
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.contador_imagen = (self.contador_imagen+1) % 40
        # se moveran todas
        self.rect.x -=1
        pantalla = pygame.display.get_surface()
        limite=0
        self.rect.x=max(self.rect.x, limite)
        