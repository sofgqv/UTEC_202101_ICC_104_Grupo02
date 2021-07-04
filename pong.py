import sys

import pygame

pygame.init()
#Nombre del juego
pygame.display.set_caption("Pong")
#Colores
negro = (0,0,0)
blanco = (255,255,255)
tamanho_pantalla = (800,600)
ancho_jugador = 15
alto_jugador = 90

#Generar la pantalla
pantalla = pygame.display.set_mode(tamanho_pantalla)
#Reloj: FPS
reloj = pygame.time.Clock()
#Coordenadas del jugador 1
jugador1_x = 50
jugador1_y = 300 - (alto_jugador//2)
#Coordenadas del jugador 2
jugador2_x = 750-ancho_jugador
jugador2_y = 300 - (alto_jugador//2)
#Movimientos de los jugadores
mov_jugador1 = 0
mov_jugador2 = 0
#Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
mov_pelota_x=3
mov_pelota_y=3
#Flag: bandera de fin del juego
game_over = False
#Marcador
marcadorJugador1 = 0
marcadorJugador2 = 0

while not game_over:
    # Gestión de Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        # Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            #Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = -3
            if evento.key == pygame.K_s:
                mov_jugador1 = 3
            #Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = -3
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 3
        #Si se deja de presionar la tecla
        if evento.type == pygame.KEYUP:
            #Jugador 1
            if evento.key == pygame.K_w:
                mov_jugador1 = 0
            if evento.key == pygame.K_s:
                mov_jugador1 = 0
            #Jugador 2
            if evento.key == pygame.K_UP:
                mov_jugador2 = 0
            if evento.key == pygame.K_DOWN:
                mov_jugador2 = 0

    #Validación de la pelota: efecto rebote
    if pelota_y > 590 or pelota_y < 10:
        mov_pelota_y *=-1
    #Si la pelota sale por el lado izquierdo o derecho es porque alguien perdió
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        #score
        marcadorJugador2 += 1
        #Si sale de la pantalla, invertimos dirección
        mov_pelota_x*=-1
        mov_pelota_y*=-1
        if (marcadorJugador1 + marcadorJugador2) % 2 == 0 and (marcadorJugador1 != 0 or marcadorJugador2 != 0):
            mov_pelota_x -= 1.25
    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        #score
        marcadorJugador1 += 1
        # Si sale de la pantalla, invertimos dirección
        mov_pelota_x *= -1
        mov_pelota_y *= -1
        if (marcadorJugador1 + marcadorJugador2) % 2 == 0 and (marcadorJugador1 != 0 or marcadorJugador2 != 0):
            mov_pelota_x += 1.25

    #Mover a los jugadores
    jugador1_y += mov_jugador1
    jugador2_y += mov_jugador2
    #Mover a la pelota
    pelota_x += mov_pelota_x
    pelota_y += mov_pelota_y
    #------------------------------------------------
    #Dibujo
    # ------------------------------------------------
    #Dibujamos el fondo
    pantalla.fill(negro)
    #Dibujamos el score
    fuente = pygame.font.SysFont("console", 100)
    score1 = fuente.render(str(marcadorJugador1), 1, (200, 200, 200))
    score2 = fuente.render(str(marcadorJugador2), 1, (200, 200, 200))
    pantalla.blit(score1, (525, 10))
    pantalla.blit(score2, (225, 10))


    #Game Over
    if marcadorJugador1 > 9 or marcadorJugador2 > 9:
        game_over = True
        if game_over == True:
            screen_text = fuente.render("GAME OVER", 1, (200, 200, 200))
            pantalla.blit(screen_text, (100, 200))

    #Dibujamos jugador1
    jugador1 = pygame.draw.rect(pantalla, blanco, (jugador1_x,jugador1_y, ancho_jugador, alto_jugador))
    #Dibujamos jugador 2
    jugador2 = pygame.draw.rect(pantalla, blanco, (jugador2_x,jugador2_y, ancho_jugador, alto_jugador))
    #Dibujo centrow
    centro = pygame.draw.line(pantalla, blanco, (400, 0), (400, 600), 5)
    #Dibujamos law pelota
    pelota = pygame.draw.circle(pantalla, blanco, (pelota_x, pelota_y),10)
    #Colisionesw
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        mov_pelota_x *= -1


    pygame.display.flip()
    reloj.tick(60)

pygame.quit()