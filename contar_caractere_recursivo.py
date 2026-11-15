def contar_caractere(s, c):
    if len(s) <= 0:
        return 0
    contagem = 1 if s[0] == c else 0
    return contagem + contar_caractere(s[1:], c)

texto = input("Texto: ")
caractere = input("Caractere: ")
resultado = contar_caractere(texto.lower(), caractere.lower())
print("Contagem:", resultado)