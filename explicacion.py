import pygame
import elementos2
import pygame_menu
import random

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
#añadimos una bala
#grupo_sprites.add(balas)
#limites

#bucle principal
#while running:
    #definiremos el bucle a framerate que hacen definido
 #   reloj.tick(FPS)

  #  teclas = pygame.key.get_pressed()
   # if teclas[pygame.K_LEFT]:
   #     nave.update()
    #if teclas[pygame.K_RIGHT]:
     #   nave.moveDerecha()
    #gestionar la salida
    #for event in pygame.event.get():
     #   if event.type == pygame.QUIT:
      #      running = False


    #pantalla.fill((255,255,255))

    # grupo_sprites.update()
    #grupo_sprites.draw(pantalla)
    #redibujar la pantalla
    #pygame.display.flip()
def set_difficulty(value, difficulty):
    #Do the job here !
    pass

def start_the_game():
    # booleano de control
    running = [True]

    global ultimo_enemigo_creado
    global reloj
    global frecuencia_
    # Do the job here !
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
        #redibujar la pantalla
        pygame.display.flip()

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(pantalla)
#finalizamos el juego
pygame.quit()