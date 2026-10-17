from constants import CASA_VAZIA

class Board:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.board = [[CASA_VAZIA for _ in range(largura)] for _ in range(altura)]

    def coordenadas_validas(self, x, y):
        return 0 <= x < self.largura and 0 <= y < self.altura
    