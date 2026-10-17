from constants import CASA_VAZIA


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


tabuleiro_padrao = Board((8, 8))

for linha in range(8):
    for coluna in range(8):
        coordenada = tabuleiro_padrao.converter_para_notacao_algebrica(coluna, linha)
        print(coordenada, end=' ')
        print(tabuleiro_padrao.converter_notacao_algebrica_para_coordenadas(coordenada), end=' ')
    print()
