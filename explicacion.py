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

##crear un grupo de Sprites vacio
grupo_sprites = pygame.sprite.Group()
# añadimos una nave
grupo_sprites.add(nave)
# añadimos otra nave
grupo_sprites.add(elementos2.Nave((100, 100)))
#limites

#bucle principal
while running:
    #definiremos el bucle a framerate que hacen definido
    reloj.tick(FPS)

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        nave.update()
    if teclas[pygame.K_RIGHT]:
        nave.moveDerecha()
    #gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pantalla.fill((255,255,255))

    # grupo_sprites.update()
    grupo_sprites.draw(pantalla)

    pygame.display.flip()

#finalizamos el juego
pygame.quit()