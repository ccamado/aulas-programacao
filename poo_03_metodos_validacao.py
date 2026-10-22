# CEPEF - 3º A - POO: metodos e validacao (22/10)
# Exemplo progressivo anterior ao CRUD visual.
class Aviso:
    def __init__(self, titulo, categoria):
        self.titulo = titulo.strip()
        self.categoria = categoria.strip()
        self.ativo = True

    def validar(self):
        categorias = ["Evento", "Atividade", "Comunicado"]
        return bool(self.titulo) and self.categoria in categorias

    def resumo(self):
        if not self.validar():
            return "Aviso invalido: revise titulo ou categoria."
        return f"[{self.categoria}] {self.titulo}"

avisos = [
    Aviso("Feira de Ciencias", "Evento"),
    Aviso("Entregar relatorio", "Atividade"),
    Aviso("  ", "Evento")
]
for aviso in avisos:
    print(aviso.resumo())
