class ListaDeTarefas:
    def __init__(self):
        self.fila = []

    def adicionar_tarefa(self, tarefa):
        self.fila.append(tarefa)

    def concluir_tarefa(self):
        if self.fila:
            return self.fila.pop(0)
        else:
            return "Lista de tarefas vazia"

# Exemplo de uso:
lista_tarefas = ListaDeTarefas()
lista_tarefas.adicionar_tarefa("Tarefa1")
lista_tarefas.adicionar_tarefa("Tarefa2")
print(lista_tarefas.concluir_tarefa())