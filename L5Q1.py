class FilaDeImpressao:
    def __init__(self):
        self.fila = []

    def adicionar_documento(self, documento):
        self.fila.append(documento)

    def imprimir(self):
        if self.fila:
            return self.fila.pop(0)
        else:
            return "Fila vazia"

# Exemplo de uso:
fila_impressao = FilaDeImpressao()
fila_impressao.adicionar_documento("Documento1")
fila_impressao.adicionar_documento("Documento2")
print(fila_impressao.imprimir())