class FilaDePedidos:
    def __init__(self):
        self.fila = []

    def fazer_pedido(self, pedido):
        self.fila.append(pedido)

    def processar_pedido(self):
        if self.fila:
            return self.fila.pop(0)
        else:
            return "Fila vazia"

# Exemplo de uso:
fila_restaurante = FilaDePedidos()
fila_restaurante.fazer_pedido("Pedido1")
fila_restaurante.fazer_pedido("Pedido2")
print(fila_restaurante.processar_pedido())