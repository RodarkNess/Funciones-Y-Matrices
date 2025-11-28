# Clase Mapa y lógica de generación


import random
from entidades import Personaje, Enemigo, Cofre
from config import VISIBLE_RADIUS

class Mapa:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.base_matriz = [[' ' for _ in range(columnas)] for _ in range(filas)]
        self.revelado = [[False for _ in range(columnas)] for _ in range(filas)]
        self.jugador = None
        self.enemigos = []
        self.cofres = []
        self.portal = None

    def generar_mapa(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if random.random() < 0.7:
                    self.base_matriz[i][j] = '.'
        px, py = self._posicion_aleatoria_valida()
        self.base_matriz[px][py] = 'S'
        self.portal = (px, py)
        cx = self.filas // 2
        cy = self.columnas // 2
        if self.base_matriz[cx][cy] != '.':
            self.base_matriz[cx][cy] = '.'
        self.jugador = Personaje(cx, cy)
        self.revelar_area(cx, cy, VISIBLE_RADIUS)
        for _ in range(5):
            ex, ey = self._posicion_aleatoria_valida(lejos_de=(cx, cy), min_dist=2)
            self.enemigos.append(Enemigo(ex, ey))
        for _ in range(8):
            tx, ty = self._posicion_aleatoria_valida(lejos_de=(cx, cy), min_dist=1)
            self.cofres.append(Cofre(tx, ty))

    def _posicion_aleatoria_valida(self, lejos_de=None, min_dist=0):
        while True:
            x = random.randint(0, self.filas - 1)
            y = random.randint(0, self.columnas - 1)
            if self.base_matriz[x][y] == '.':
                if lejos_de is None:
                    return x, y
                dx = lejos_de[0] - x
                dy = lejos_de[1] - y
                if dx * dx + dy * dy >= min_dist * min_dist:
                    return x, y

    def revelar_area(self, x, y, radio):
        r2 = radio * radio
        for i in range(max(0, x - radio), min(self.filas, x + radio + 1)):
            for j in range(max(0, y - radio), min(self.columnas, y + radio + 1)):
                dx = x - i
                dy = y - j
                if dx * dx + dy * dy <= r2:
                    self.revelado[i][j] = True
