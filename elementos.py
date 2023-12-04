import pygame
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