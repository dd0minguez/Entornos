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

posicion = (200, 200)
nave = elementos2.Nave(posicion)

##crear un grupo de Sprites vacio
grupo_sprites = pygame.sprite.Group()
# añadimos una nave
grupo_sprites.add(nave)
# añadimos otra nave
grupo_sprites.add(elementos2.Nave((100, 100)))

def set_difficulty(value, difficulty):
    #Do the job here !
    pass

def start_the_game():
    # booleano de control
    running = [True]

    global ultimo_enemigo_creado
    global reloj
    global frecuencia_creacion_enemigo
    global grupo_sprites_todos
    global grupo_sprites_enemigos
    global grupo_sprites_balas
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

        if not pausado:
            #creacion de enemigos
            momento_actual = pygame.time.get_ticks()
            if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
                cordX = random.randint(0, pantalla.get_width())
                cordY = -200
                # creamos el enemigo
                enemigo = elementos2.enemigo((cordX, cordY))
                #lo añadimos a los dos grupos: todos y enemigos
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                #actualizamos el momento del ultimo enemigo creado
                ultimo_enemigo_creado = momento_actual

        pantalla.fill((255,255,255))




        # grupo_sprites.update()
        grupo_sprites.draw(pantalla)

        #si pausado, escribirlo
        if pausado:
            texto = font.render("PAUSA", True, "White")
            pantalla.blit(texto, (pantalla.get_width() / 2, pantalla.get_height() / 2))
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