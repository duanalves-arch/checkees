# Checkees

Checkees é um projeto pessoal, feito por hobby, para recriar o xadrez em Python
e explorar suas possibilidades. A ideia é construir o jogo aos poucos, partindo
das regras e dos elementos tradicionais do xadrez e experimentando novas
mecânicas conforme o projeto evolui.

O código atual é o começo dessa jornada: já permite representar tabuleiros,
manipular peças e converter coordenadas. A documentação abaixo descreve o que
está implementado hoje, não limita o que o projeto pode vir a ser.

## Requisitos

- Python 3.9 ou superior

O projeto não possui dependências externas.

## Uso

Com o repositório disponível no ambiente, importe `Board` e as constantes do
pacote `checkees`:

```python
from checkees import Board, PEAO_BRANCO

tabuleiro = Board((8, 8))
tabuleiro.colocar_peca((0, 6), PEAO_BRANCO)

print(tabuleiro.casa_ocupada((0, 6)))  # True
print(tabuleiro.converter_para_notacao_algebrica(0, 6))  # a2
```

As dimensões são informadas na ordem `(altura, largura)`. As coordenadas das
casas são tuplas `(coluna, linha)`, com índices iniciados em zero. O tabuleiro
é criado vazio; a configuração inicial das peças não é preenchida
automaticamente.

## API

- `Board((altura, largura))`: cria um tabuleiro vazio com dimensões positivas.
- `coordenadas_sao_validas(coluna, linha)`: verifica se os índices pertencem ao
  tabuleiro.
- `casa_ocupada((coluna, linha))`: informa se a casa contém uma peça.
- `colocar_peca((coluna, linha), peca)`: coloca uma peça em uma casa vazia.
- `tirar_peca((coluna, linha))`: esvazia uma casa.
- `converter_para_notacao_algebrica(coluna, linha)`: converte coordenadas em
  notação algébrica, como `a1`.
- `converter_notacao_algebrica_para_coordenadas(notacao)`: converte uma casa,
  como `a1` ou `H8`, para coordenadas.

As conversões de notação algébrica estão disponíveis apenas em tabuleiros de
8 × 8. Coordenadas inválidas, peças não reconhecidas e tentativas de colocar
uma peça em uma casa ocupada geram `ValueError`.

## Peças e casas

O pacote exporta `CASA_VAZIA` e as constantes das peças brancas e pretas:
`PEAO`, `BISPO`, `CAVALO`, `TORRE`, `RAINHA` e `REI`, com o sufixo `_BRANCO`,
`_BRANCA`, `_PRETO` ou `_PRETA`, conforme o nome da peça.

## Estrutura do projeto

```text
checkees/
    __init__.py   # API pública do pacote
    board.py      # Implementação do tabuleiro
    constants.py  # Valores das casas e peças
main.py           # Ponto de entrada do projeto
```