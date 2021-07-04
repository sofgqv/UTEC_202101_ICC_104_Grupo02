# Instalación de PyGame: pip install pygame
import sys

import pygame

#Inicialización
pygame.init()
#Colores
rgb_rojo = (255,0,0)
rgb_blanco = (255,255,255)
rgb_verde = (0,255,0)
rgb_azul = (0,0,255)
#Pantalla de 800x600
pantalla_x= 800
pantalla_y= 600
pantalla=pygame.display.set_mode((pantalla_x,pantalla_y))
#Coordenadas del círculo
circulo1_x= 200
circulo1_y= 50
radio_circulo1 = 50
#Coordenadas del rectángulo
rectángulo1_x = 200
rectángulo1_y = 200
ancho_rectángulo1=150
#Movimiento del círculo
mov_circulo1= 5
#Movimiento del rectángulo
mov_rectángulo1= -5
# Frames por segundo
reloj = pygame.time.Clock()
#Juegos suelen tener bucles prolongados para mantener activo el juego
while True:
    #Gestión de Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    # Dibujo: Fondo
    pantalla.fill(rgb_blanco)
    #Dibujo: 10 es el grosor de la línea
    pygame.draw.line(pantalla, rgb_rojo, [0,0],[pantalla_x//4,pantalla_y//4], 10)
    # Dibujo: rectángulo: (x,y, ancho y alto)
    pygame.draw.rect(pantalla, rgb_verde, (rectángulo1_x,rectángulo1_y,ancho_rectángulo1,50))
    # Dibujo: círculo: (x,y),radio
    pygame.draw.circle(pantalla, rgb_azul, (circulo1_x, circulo1_y), radio_circulo1)
    #Validacion para el efecto rebote del circulo: validacion en el extremo derecho o izquierdo
    if circulo1_x > pantalla_x-radio_circulo1 or circulo1_x < 0+radio_circulo1:
        mov_circulo1 *= -1
    # Validacion para el efecto rebote del rectángulo: validacion en el extremo derecho o izquierdo
    if rectángulo1_x < 0 or rectángulo1_x > pantalla_x - ancho_rectángulo1:
        mov_rectángulo1 *= -1
    #Movimiento del circulo
    circulo1_x+= mov_circulo1
    #Movimiento del rectángulo
    rectángulo1_x += mov_rectángulo1
    pygame.display.flip()
    #Cantidad de FPS
    reloj.tick(50)
