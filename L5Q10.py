def eh_palindromo(frase):
    pilha = []
    for caractere in frase:
        if caractere.isalnum():
            pilha.append(caractere.lower())

    while len(pilha) > 1:
        if pilha.pop(0) != pilha.pop():
            return False

    return True


frase_teste = "Ame a ema"
print(eh_palindromo(frase_teste))