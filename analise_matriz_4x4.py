matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
soma_acima = 0
soma_abaixo = 0
soma_total = 0
# Percorre todas as linhas
for i in range(0, 4):
    print(f"{i + 1}ª Linha")
    print("===========")

    # Percorre todas as colunas, solicitando a entrada do usuario
    for j in range(0, 4):
        matriz[i][j] = int(input(f"{j + 1}° Valor: "))

        soma_total += matriz[i][j]

        # Verifica se a soma fica acima ou abaixo da diagonal principal
        if i < j:
            soma_acima += matriz[i][j]
        elif i > j:
            soma_abaixo += matriz[i][j]

    print("===========")

media = soma_total / 16

# Imprime a Matriz 4x4 na tela
for i in range(0, 4):
    for j in range(0, 4):
        print(f"{matriz[i][j]:^5}", end = "")
    print("")
# Imprime na tela os resultados
print("===========")
print("Soma acima da diagonal principal:", soma_acima)
print("Soma abaixo da diagonal principal:", soma_abaixo)
print("Soma total da matriz:", soma_total)
print(f"Media da matriz: {media:.2f}")
print("===========")
