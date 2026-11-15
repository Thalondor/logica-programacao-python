def encontrar_minimo(lista):
    if len(lista) == 1:
        return lista[0]
    menor_resto = encontrar_minimo(lista[1:])

    if lista[0] < menor_resto:
        return lista[0]
    else:
        return menor_resto

entrada = input("Digite um numero: ")
numeros = [float(x) for x in entrada.split()]
menor = encontrar_minimo(numeros)
print("Menor número:", menor)