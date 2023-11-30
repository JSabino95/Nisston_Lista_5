class AnalisadorExpressao:
    def __init__(self):
        self.pilha = []

    def encontrar_operadores(self, expressao):
        for caractere in expressao:
            if caractere in "+-*/^":
                self.pilha.append(caractere)

    # Exemplo de uso:
analisador = AnalisadorExpressao()
analisador.encontrar_operadores("(2+3)*(8-9)/(7^3)")
print(analisador.pilha)
