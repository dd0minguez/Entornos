from typing import Any
import pygame

class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion) -> None:
        super().__init__()

        #cargamos la imagen
        self.image = pygame.image.load("nave1.png")
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posicion del rectangulo para que coincida con posicion
        self.rect.topleft = posicion
    
        #update
        def update(self, *args: Any, **kwargs: Any) -> None:
            pass