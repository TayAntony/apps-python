numeros_casas = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
casas = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
ACABOU = False

MARCACOES = ["X", "O"]
jogadores = []
CONTADOR = 0


def print_casas(mensagem, array):
    print(mensagem)
    for i in range(3):
        for j in range(3):
            print(f"| {array[i][j]} ", end="")
        print("|")


def exibir_tabuleiro() -> None:
    print("+==+==" * 10)
    print_casas("Números das casas:", numeros_casas)
    print_casas("\nTabuleiro:", casas)


def checar_vencedor():
    # Checando horizontalmente
    for linha in casas:
        if linha[0] == linha[1] and linha[1] == linha[2] and linha[0] != " ":
            return linha[0]

    # Checando verticalmente
    for coluna in range(3):
        if (
            casas[0][coluna] == casas[1][coluna]
            and casas[1][coluna] == casas[2][coluna]
            and casas[0][coluna] != " "
        ):
            return casas[0][coluna]

    # Checando
    # X
    #   X
    #     X
    if casas[0][0] == casas[1][1] and casas[1][1] == casas[2][2] and casas[0][0] != " ":
        return casas[0][0]

    # Checando
    #     X
    #   X
    # X
    if casas[0][2] == casas[1][1] and casas[1][1] == casas[2][0] and casas[0][0] != " ":
        return casas[0][2]

    velha = True
    for linha in casas:
        for casa in linha:
            if casa == " ":
                velha = False

    if velha:
        return "VELHA"

    return False


def exibir_ganhador(letra_resultado):
    if letra_resultado == "VELHA":
        print(
            """
            +===+===+===+
            | Deu velha!|
            +===+===+===+
        """
        )
        return

    print(
        f"""
        +=====+=====+=====+=====+
        O jogador {jogadores[MARCACOES.index(letra_resultado)]} ganhou!
        +=====+=====+=====+=====+
    """
    )


def pedir_jogada():
    global CONTADOR
    casa = int(input(f"Jogador {jogadores[CONTADOR % 2]}, Escolha sua casa: ")) - 1

    lista_casas = [*casas[0], *casas[1], *casas[2]]

    if lista_casas[casa] != " ":
        print("POR FAVOR, ESCOLHA UMA CASA VAZIA.")
        return pedir_jogada()

    lista_casas[casa] = MARCACOES[CONTADOR % 2]

    casas[0][0] = lista_casas[0]
    casas[0][1] = lista_casas[1]
    casas[0][2] = lista_casas[2]
    casas[1][0] = lista_casas[3]
    casas[1][1] = lista_casas[4]
    casas[1][2] = lista_casas[5]
    casas[2][0] = lista_casas[6]
    casas[2][1] = lista_casas[7]
    casas[2][2] = lista_casas[8]


def rodada():
    global CONTADOR
    exibir_tabuleiro()
    resultado = checar_vencedor()
    if resultado != False:
        exibir_ganhador(resultado)
        return True
    pedir_jogada()
    CONTADOR += 1
    return False


jogadores.append(input("Digite o nome do jogador 1: "))
jogadores.append(input("Digite o nome do jogador 2: "))

while not ACABOU:
    ACABOU = rodada()
