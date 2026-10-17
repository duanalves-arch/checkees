from constants import CASA_VAZIA, PEAO_BRANCO, BISPO_BRANCO, CAVALO_BRANCO, TORRE_BRANCA, RAINHA_BRANCA, REI_BRANCO, PEAO_PRETO, BISPO_PRETO, CAVALO_PRETO, TORRE_PRETA, RAINHA_PRETA, REI_PRETO


class Board:
    def __init__(self, dimensao: tuple[int, int]):
        self.altura, self.largura = dimensao
        self.tabuleiro = [[CASA_VAZIA for _ in range(self.largura)] for _ in range(self.altura)]

    def coordenadas_sao_validas(self, coluna: int, linha: int) -> bool:
        return 0 <= coluna < self.largura and 0 <= linha < self.altura

    def converter_para_notacao_algebrica(self, coluna: int, linha: int) -> str:
        if not self.coordenadas_sao_validas(coluna, linha):
            raise ValueError("Coordenadas inválidas")

        letra_coluna = chr(ord('a') + coluna)
        numero_linha = str(self.altura - linha)
        return f"{letra_coluna}{numero_linha}"

    def converter_notacao_algebrica_para_coordenadas(self, notacao: str) -> tuple[int, int]:
        if len(notacao) != 2:
            raise ValueError("Notação inválida")

        coluna = ord(notacao[0]) - ord('a')
        linha = self.altura - int(notacao[1])

        if not self.coordenadas_sao_validas(coluna, linha):
            raise ValueError("Notação inválida")

        return coluna, linha

    def botar_peca(self, coordenadas: tuple[int, int], peca: int):
        coluna, linha = coordenadas
        if not self.coordenadas_sao_validas(coluna, linha):
            raise ValueError("Coordenadas inválidas")
        if self.casa_ocupada(coordenadas):
            raise ValueError("Casa já ocupada")
        self.tabuleiro[linha][coluna] = peca

    def casa_ocupada(self, coordenadas: tuple[int, int]) -> bool:
        coluna, linha = coordenadas
        if not self.coordenadas_sao_validas(coluna, linha):
            raise ValueError("Coordenadas inválidas")
        return self.tabuleiro[linha][coluna] != CASA_VAZIA

    def tirar_peca(self, coordenadas: tuple[int, int]):
        coluna, linha = coordenadas
        if not self.coordenadas_sao_validas(coluna, linha):
            raise ValueError("Coordenadas inválidas")
        self.tabuleiro[linha][coluna] = CASA_VAZIA
