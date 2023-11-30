class EditorDeTexto:
    def __init__(self):
        self.historico_comandos = []
        self.texto = ""

    def executar_comando(self, comando):
        self.historico_comandos.append(self.texto)
        self.texto += comando

    def desfazer(self):
        if self.historico_comandos:
            self.texto = self.historico_comandos.pop()
        else:
            print("Nada para desfazer.")

    def refazer(self):
        print("Refazer ainda não implementado.")

# Exemplo de uso:
editor = EditorDeTexto()
editor.executar_comando("Insira o primeiro texto")
editor.executar_comando("Insira o segundo texto")
print(editor.texto)
editor.desfazer()
print(editor.texto)