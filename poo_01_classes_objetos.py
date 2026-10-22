# CEPEF - 3º A - POO: classes, objetos e atributos (08/10)
# Primeiro exemplo: criar instancias a partir de uma classe.
class Aviso:
    pass

aviso1 = Aviso()
aviso1.titulo = "Prova de Programacao"
aviso1.data = "20/10/2026"
aviso1.tipo = "prova"

aviso2 = Aviso()
aviso2.titulo = "Reuniao"
aviso2.data = "22/10/2026"
aviso2.tipo = "reuniao"

print("Aviso 1:", aviso1.titulo, aviso1.data, aviso1.tipo)
print("Aviso 2:", aviso2.titulo, aviso2.data, aviso2.tipo)
