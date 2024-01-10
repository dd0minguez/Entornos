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
class Fondo (pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        #cargamos la imagen
        imagen_cargada = pygame.image.load("bg.rotado.png")
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(
            imagen_cargada, (pantalla.get_width(), imagen_cargada.get_height()))
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posicion del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: Any, **kwarhgs: Any) -> None:
        self.rect.y += 1
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if self.rect.y >= pantalla.get_height():
            self.rect.y = - pantalla.get_height()

class Bala (pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        #creamos un rectangulo
        self.image = pygame.Surface((5,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = posicion
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y = 5
    
        