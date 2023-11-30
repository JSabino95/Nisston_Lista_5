class FilaDeAtendimento:
    def __init__(self):
        self.fila = []

    def entrar_na_fila(self, cliente):
        self.fila.append(cliente)

    def atender_cliente(self):
        if self.fila:
            return self.fila.pop(0)
        else:
            return "Fila vazia"

# Exemplo de uso:
fila_banco = FilaDeAtendimento()
fila_banco.entrar_na_fila("Cliente1")
fila_banco.entrar_na_fila("Cliente2")
print(fila_banco.atender_cliente())