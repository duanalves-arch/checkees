from constants import CASA_VAZIA

class Board:
    def __init__(self, dimensao: tuple[int, int]):
        self.altura, self.largura = dimensao
        self.board = [[CASA_VAZIA for _ in range(self.largura)] for _ in range(self.altura)]

    def coordenadas_validas(self, x, y):
        return 0 <= x < self.largura and 0 <= y < self.altura

    def converter_coordenadas_para_notacao_algebrica(self, x, y):
        if not self.coordenadas_validas(x, y):
            raise ValueError("Coordenadas inválidas")
        coluna = chr(ord('a') + x)
        linha = str(self.altura - y)
        return f"{coluna}{linha}"

    def converter_notacao_algebrica_para_coordenadas(self, notacao):
        if len(notacao) != 2:
            raise ValueError("Notação inválida")
        coluna = ord(notacao[0]) - ord('a')
        linha = self.altura - int(notacao[1])
        if not self.coordenadas_validas(coluna, linha):
            raise ValueError("Notação inválida")
        return coluna, linha
