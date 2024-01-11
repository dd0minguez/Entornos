import pygame
#import
import pygame_menu
import random

#inicialización del juego
pygame.init()

#Pantalla
tamanyo = (850, 478)
pantalla = pygame.display.set_mode(tamanyo)

#Reloj
reloj = pygame.time.Clock()
FPS = 60

posicion = (200, 200)

#Sprites
grupo_sprites = pygame.sprite.Group()
