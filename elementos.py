import pygame
import math
class Nave:
    def __init__(self) -> None:
       self.x=30
       self.y=30
       imagenes_cargadas=[pygame.image.load("nave1.png"), pygame.image.load("nave2.png")] 
       self.imagenes=[pygame.transform.scale(imagenes_cargadas[0], (80,80)), pygame.transform.scale(imagenes_cargadas[1], (80,80))]
       self.contador=0
    def moveDerecha(self):
        self.x +=1
        pantalla = pygame.display.get_surface()
        limite=pantalla.get_width()
        self.x=min(self.x, limite-self.imagenes[0].get_width())
    
    def moverIzquierda(self):
        self.x -=1
        pantalla = pygame.display.get_surface()
        limite=0
        self.x=max(self.x, limite)

    def dibujar(self):
        # aumento del contador
        self.contador =(self.contador+1) % 40
        # cojo el puntero de la pantalla
        pantalla = pygame.display.get_surface()
        # seleccionar la imagen que toca
        seleccionada = self.contador // 20
        #dibujar imagen
        pantalla.blit(self.imagenes[seleccionada], (self.x, self.y))

class Fondo:
    def __init__(self) -> None:
        #localizar pantalla
        pantalla = pygame.display.get_surface()
        #Cargamos la imagen
        imagen = pygame.image.load("bg.rotado.png")
        # escalar la imagen para que encaje en el ancho de la pantalla
        self.fondo = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        #scroll
        self.scroll = 0
        # cuantas piezas de fondo necesitamos
        self.piezas = math.ceil(pantalla.get_height()/ self.fondo.get_height()) +1

    def dibujar(self):
        #aumentar el scroll
        self.scroll += 4
        #localizar la pantalla
        pantalla = pygame.display.get_surface()
        #resetear el scroll
        if self.scroll > self.fondo.get_height():
            self.scroll = 0
        #dibujamos el fondo
        for i in range(0, self.piezas):
            pantalla.blit(self.fondo, (0, -self.fondo.get_height() + i * self.fondo.get_height() + self.scroll))
class Bala:
    def __init__(self) -> None:
        pass