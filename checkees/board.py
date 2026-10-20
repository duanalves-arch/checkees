from .constants import (
    CASA_VAZIA,
    PEAO_BRANCO,
    BISPO_BRANCO,
    CAVALO_BRANCO,
    TORRE_BRANCA,
    RAINHA_BRANCA,
    REI_BRANCO,
    PEAO_PRETO,
    BISPO_PRETO,
    CAVALO_PRETO,
    TORRE_PRETA,
    RAINHA_PRETA,
    REI_PRETO,
)


_PECAS_VALIDAS = frozenset(
    {
        PEAO_BRANCO,
        BISPO_BRANCO,
        CAVALO_BRANCO,
        TORRE_BRANCA,
        RAINHA_BRANCA,
        REI_BRANCO,
        PEAO_PRETO,
        BISPO_PRETO,
        CAVALO_PRETO,
        TORRE_PRETA,
        RAINHA_PRETA,
        REI_PRETO,
    }
)


class Board:
    def __init__(self, dimensao: tuple[int, int]):
        """Inicializa um tabuleiro vazio com dimensões (altura, largura).

        As dimensões devem ser dois inteiros positivos, sem incluir valores
        booleanos. Tabuleiros de tamanhos diferentes de 8 × 8 são permitidos.

        Raises:
            ValueError: Se as dimensões estiverem malformadas ou forem inválidas.
        """
        if not isinstance(dimensao, (tuple, list)) or len(dimensao) != 2:
            raise ValueError("Dimensões inválidas")

        altura, largura = dimensao
        if any(
            not isinstance(valor, int)
            or isinstance(valor, bool)
            or valor <= 0
            for valor in (altura, largura)
        ):
            raise ValueError("Dimensões inválidas")

        self.altura = altura
        self.largura = largura
        self.tabuleiro = [
            [CASA_VAZIA for _ in range(self.largura)]
            for _ in range(self.altura)
        ]

    def coordenadas_sao_validas(self, coluna: int, linha: int) -> bool:
        """Indica se coluna e linha são índices inteiros dentro do tabuleiro.

        Booleanos não são aceitos como índices, embora sejam subclasses de int.
        """
        return (
            isinstance(coluna, int)
            and not isinstance(coluna, bool)
            and isinstance(linha, int)
            and not isinstance(linha, bool)
            and 0 <= coluna < self.largura
            and 0 <= linha < self.altura
        )

    def _validar_coordenadas(
        self, coordenadas: tuple[int, int]
    ) -> tuple[int, int]:
        """Valida coordenadas no formato (coluna, linha) e as devolve.

        Raises:
            ValueError: Se as coordenadas não tiverem dois índices válidos.
        """
        if not isinstance(coordenadas, (tuple, list)) or len(coordenadas) != 2:
            raise ValueError("Coordenadas inválidas")

        coluna, linha = coordenadas
        if not self.coordenadas_sao_validas(coluna, linha):
            raise ValueError("Coordenadas inválidas")
        return coluna, linha

    def _validar_tabuleiro_convencional(self) -> None:
        """Garante que o tabuleiro tenha dimensões 8 × 8 para usar notação algébrica.

        Raises:
            ValueError: Se o tabuleiro não tiver dimensões 8 × 8.
        """
        if self.altura != 8 or self.largura != 8:
            raise ValueError(
                "Notação algébrica disponível apenas para tabuleiros 8 × 8"
            )

    def converter_para_notacao_algebrica(self, coluna: int, linha: int) -> str:
        """Converte índices (coluna, linha) para notação algébrica, como ``a1``.

        A conversão só é suportada em tabuleiros 8 × 8.

        Raises:
            ValueError: Se as coordenadas forem inválidas ou o tabuleiro não for
                8 × 8.
        """
        if not self.coordenadas_sao_validas(coluna, linha):
            raise ValueError("Coordenadas inválidas")
        self._validar_tabuleiro_convencional()

        letra_coluna = chr(ord("a") + coluna)
        numero_linha = str(self.altura - linha)
        return f"{letra_coluna}{numero_linha}"

    def converter_notacao_algebrica_para_coordenadas(
        self, notacao: str
    ) -> tuple[int, int]:
        """Converte uma casa algébrica, como ``a1`` ou ``H8``, em (coluna, linha).

        Letras maiúsculas e minúsculas são aceitas. A conversão só é suportada
        em tabuleiros 8 × 8.

        Raises:
            ValueError: Se a notação for inválida ou o tabuleiro não for 8 × 8.
        """
        self._validar_tabuleiro_convencional()
        if not isinstance(notacao, str) or len(notacao) != 2:
            raise ValueError("Notação inválida")

        letra_coluna = notacao[0].lower()
        numero_linha = notacao[1]
        if letra_coluna not in "abcdefgh" or numero_linha not in "12345678":
            raise ValueError("Notação inválida")

        coluna = ord(letra_coluna) - ord("a")
        linha = 8 - int(numero_linha)
        return coluna, linha

    def casa_ocupada(self, coordenadas: tuple[int, int]) -> bool:
        """Indica se a casa em (coluna, linha) contém uma peça.

        Raises:
            ValueError: Se as coordenadas forem inválidas.
        """
        coluna, linha = self._validar_coordenadas(coordenadas)
        return self.tabuleiro[linha][coluna] != CASA_VAZIA

    def tirar_peca(self, coordenadas: tuple[int, int]) -> None:
        """Remove a peça da casa; não faz nada se ela já estiver vazia.

        Raises:
            ValueError: Se as coordenadas forem inválidas.
        """
        coluna, linha = self._validar_coordenadas(coordenadas)
        self.tabuleiro[linha][coluna] = CASA_VAZIA

    def colocar_peca(self, coordenadas: tuple[int, int], peca: int) -> None:
        """Coloca uma peça válida na casa indicada por (coluna, linha).

        Raises:
            ValueError: Se as coordenadas forem inválidas ou a peça não for
                reconhecida.
        """
        coluna, linha = self._validar_coordenadas(coordenadas)
        if not isinstance(peca, int) or isinstance(peca, bool):
            raise ValueError("Peça inválida")
        if peca not in _PECAS_VALIDAS:
            raise ValueError("Peça inválida")
        if self.tabuleiro[linha][coluna] != CASA_VAZIA:
            raise ValueError("Casa já ocupada")
        self.tabuleiro[linha][coluna] = peca
