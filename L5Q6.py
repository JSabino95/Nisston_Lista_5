class NavegadorWeb:
    def __init__(self):
        self.historico = []
        self.pagina_atual = None

    def visitar_pagina(self, pagina):
        self.historico.append(self.pagina_atual)
        self.pagina_atual = pagina

    def voltar(self):
        if self.historico:
            self.pagina_atual = self.historico.pop()
        else:
            print("Não há mais páginas para voltar.")

    def avancar(self):
        if self.pagina_atual is not None:
            self.historico.append(self.pagina_atual)
            self.pagina_atual = None
        else:
            print("Não há mais páginas para avançar.")

# Exemplo de uso:
navegador = NavegadorWeb()
navegador.visitar_pagina("google.com")
navegador.visitar_pagina("facebook.com")
navegador.voltar()
navegador.avancar()