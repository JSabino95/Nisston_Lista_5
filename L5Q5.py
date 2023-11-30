class FilaPedidosOnline:
    def __init__(self):
        self.fila = []

    def adicionar_pedido(self, pedido):
        self.fila.append(pedido)

    def processar_pedido(self):
        if self.fila:
            return self.fila.pop(0)
        else:
            return "Fila de pedidos online vazia"

# Exemplo de uso:
fila_pedidos_online = FilaPedidosOnline()
fila_pedidos_online.adicionar_pedido("PedidoOnline1")
fila_pedidos_online.adicionar_pedido("PedidoOnline2")
print(fila_pedidos_online.processar_pedido())