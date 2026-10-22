# CEPEF - 3º A - POO: construtor, self e __init__ (08/10)
# Os atributos passam a ser definidos no construtor.
class Aviso:
    def __init__(self, titulo, data, tipo):
        self.titulo = titulo
        self.data = data
        self.tipo = tipo

aviso1 = Aviso("Prova", "20/10/2026", "prova")
aviso2 = Aviso("Reuniao", "22/10/2026", "reuniao")

print("Aviso 1:", aviso1.titulo, aviso1.data, aviso1.tipo)
print("Aviso 2:", aviso2.titulo, aviso2.data, aviso2.tipo)
