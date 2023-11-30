class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def calcular(self, expressao):
        tokens = expressao.split()
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.pilha.append(float(token))
            else:
                operando2 = self.pilha.pop()
                operando1 = self.pilha.pop()
                if token == '+':
                    resultado = operando1 + operando2
                elif token == '-':
                    resultado = operando1 - operando2
                elif token == '*':
                    resultado = operando1 * operando2
                elif token == '/':
                    resultado = operando1 / operando2
                elif token == '^':
                    resultado = operando1 ** operando2
                else:
                    print("Operador inválido")
                    return
                self.pilha.append(resultado)
        return self.pilha[0]


calculadora = CalculadoraRPN()
resultado = calculadora.calcular("3 4 + 2 *")
print(resultado)