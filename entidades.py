# Clases: Personaje, Enemigo, Cofre


import random

class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vida = 100
        self.movimientos = 0

    def mover(self, dx, dy, base_matriz):
        nuevo_x = self.x + dx
        nuevo_y = self.y + dy
        filas = len(base_matriz)
        columnas = len(base_matriz[0])
        if not (0 <= nuevo_x < filas and 0 <= nuevo_y < columnas):
            return False
        if base_matriz[nuevo_x][nuevo_y] in ('.', 'S'):
            self.x = nuevo_x
            self.y = nuevo_y
            self.movimientos += 1
            return True
        return False

class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vida = 50
        self.vision = 5
        self.ultimo_movimiento = 0

    def mover_hacia_jugador(self, jugador, base_matriz, movimiento_actual):
        if movimiento_actual - self.ultimo_movimiento < 2:
            return False
        dist_x = jugador.x - self.x
        dist_y = jugador.y - self.y
        if abs(dist_x) <= self.vision and abs(dist_y) <= self.vision:
            dx, dy = 0, 0
            if abs(dist_x) > abs(dist_y):
                dx = 1 if dist_x > 0 else -1
            else:
                dy = 1 if dist_y > 0 else -1
            nuevo_x = self.x + dx
            nuevo_y = self.y + dy
            filas = len(base_matriz)
            columnas = len(base_matriz[0])
            if 0 <= nuevo_x < filas and 0 <= nuevo_y < columnas:
                if base_matriz[nuevo_x][nuevo_y] in ('.', 'S'):
                    self.x = nuevo_x
                    self.y = nuevo_y
                    self.ultimo_movimiento = movimiento_actual
                    return True
        return False

class Cofre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contenido = random.choice(['vida', 'arma', 'oro'])
        self.abierto = False
