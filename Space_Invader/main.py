import pygame
import random
import math
from pygame import mixer

"""Inicializar la libreria pygame"""
pygame.init()


"""Creamos la pantalla"""
pantalla = pygame.display.set_mode((800, 600))


"""Titulo e Icono"""
pygame.display.set_caption('Space Invader')
icono = pygame.image.load('incono.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Agregar Música
mixer.music.load('musicaback.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)


"""Imagen y posicion de la nave"""
img_jugador = pygame.image.load('personaje.png')
pos_x = 368
pos_y = 510
pos_x_mov = 0

"""Imagen y posicion del enemigo"""
img_enemigo = []
ene_x = []
ene_y = []
ene_x_mov = []
ene_y_mov = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    ene_x.append(random.randint(0, 736))
    ene_y.append(random.randint(20, 200))
    ene_x_mov.append(0.3)
    ene_y_mov.append(50)

"""Imagen y posicion del misil"""
img_misil = pygame.image.load('misil.png')
misil_x = 0
misil_y = 500
misil_x_mov = 0
misil_y_mov = 0.7
misil_shot = False

# Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final
fuente_final = pygame.font.Font('freesansbold.ttf', 32)


def texto_final():
    mi_fuente_f = fuente_final.render('FIN DEL JUEGO', True, (255, 255, 255))
    pantalla.blit(mi_fuente_f, (280, 300))

# Funcion mostrar puntaje


def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Funcion personaje


def nave(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion enemigo


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Funcion lanzar misil


def lanzar_misil(x, y):
    global misil_shot
    misil_shot = True
    pantalla.blit(img_misil, (x + 16, y + 10))

# Detectar colision


def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


"""Loop para iniciar el juego"""
se_ejecuta = True
while se_ejecuta:

    # Crear fondo
    pantalla.blit(fondo, (0, 0))

    """Iteracion de eventos"""
    for evento in pygame.event.get():

        # Funcion para cerrar la pantalla
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Funcino para generar el movimiento
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                pos_x_mov = -0.5
            if evento.key == pygame.K_RIGHT:
                pos_x_mov = 0.5
            if evento.key == pygame.K_SPACE:
                sonido_misil = mixer.Sound('missle-launch.mp3')
                sonido_misil.set_volume(0.2)
                sonido_misil.play()
                if not misil_shot:
                    misil_x = pos_x
                    lanzar_misil(misil_x, misil_y)

        # Detectar parar movimiento
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                pos_x_mov = 0

    # Modificar movimiento de la nave judador
    pos_x += pos_x_mov

    # Definir los limites del jugador
    if pos_x <= 0:
        pos_x = 0
    elif pos_x >= 736:
        pos_x = 736

    # Modificar movimiento del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if ene_y[e] > 500:
            for k in range(cantidad_enemigos):
                ene_y[k] = 1000
            texto_final()
            break

        ene_x[e] += ene_x_mov[e]

    # Definir los limites del enemigo
        if ene_x[e] <= 0:
            ene_x_mov[e] = 0.3
            ene_y[e] += ene_y_mov[e]
        elif ene_x[e] >= 736:
            ene_x_mov[e] = -0.3
            ene_y[e] += ene_y_mov[e]

        # Colision
        colision = hay_colision(ene_x[e], ene_y[e], misil_x, misil_y)
        if colision:
            sonido_explosion = mixer.Sound('impacto.mp3')
            sonido_explosion.set_volume(0.5)
            sonido_explosion.play()
            misil_y = 500
            misil_shot = False
            puntaje += 1
            ene_x[e] = random.randint(0, 736)
            ene_y[e] = random.randint(20, 200)

        enemigo(ene_x[e], ene_y[e], e)

    # Movimiento misil
    if misil_y <= -64:
        misil_y = 500
        misil_shot = False

    if misil_shot:
        lanzar_misil(misil_x, misil_y)
        misil_y -= misil_y_mov

    nave(pos_x, pos_y)

    mostrar_puntaje(texto_x, texto_y)

    # Actualizar los eventos
    pygame.display.update()
