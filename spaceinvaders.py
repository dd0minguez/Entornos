import pygame
from elementos import Nave, Fondo

pygame.init()
pantalla= pygame.display.set_mode((800,600))
clock=pygame.time.Clock
FPS=60

#imagen_avion =pygame.image.load("avion.png")
#avion=pygame.transform.scale(imagen_avion, (90,30))
#avion_rect = avion.get_rect()
posIzda =30
posTop=30
salir= False

nave = Nave()
fondo = Fondo()

while not salir:
    #gestionar eventos dentro de juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT    :
            salir = True
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        nave.moverIzquierda()
    if teclas[pygame.K_RIGHT]:
        nave.moveDerecha()
    #if teclas[pygame.K_UP]:
    #    posTop -=1
    #if teclas[pygame.K_DOWN]:
    #    posIzda += 1
    #gestionar cambios
    pantalla.fill((255,255,255))

    fondo.dibujar()
    #pygame.draw.rect(pantalla, (255,255,255), pygame.Rect(posIzda,posTop,60,60))
    #pantalla.blit(avion, (posTop, posIzda))
    nave.dibujar()
    #redibujar el juego
    pygame.display.flip()
pygame.quit()