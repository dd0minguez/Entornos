import pygame
import elementos2

#inicializamos el juego
pygame.init()

#creamos la pantalla
tamanyo = (800, 600)
pantalla = pygame.display.set_mode(tamanyo)

#definiremos un reloj
reloj = pygame.time.Clock()
FPS = 60

#booleano de control
running = True

posicion = (200, 200)
nave = elementos2.Nave(posicion)

##crear un grupo de Sprites
grupo_sprites = pygame.sprite.Group(nave)
#grupo_sprites =pygame.sprite.GroupElementos.Nave((100, 100))
#bucle principal
while running:
    #definiremos el bucle a framerate que hacen definido
    reloj.tick(FPS)

    #gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#finalizamos el juego
pygame.quit()