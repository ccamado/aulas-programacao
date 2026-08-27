# CENTRAL DE AVISOS v0.1
# Programação Aplicada II — 3º A — 27/08/2026

avisos = []


def cadastrar_aviso():
    print("\n--- CADASTRO DE AVISO ---")
    titulo = input("Título: ")
    data = input("Data: ")
    tipo = input("Tipo: ")

    aviso = {
        "titulo": titulo,
        "data": data,
        "tipo": tipo
    }

    avisos.append(aviso)
    print("\nAviso cadastrado com sucesso!")


def listar_avisos():
    print("\n--- AVISOS CADASTRADOS ---")

    for aviso in avisos:
        print("\nTítulo:", aviso["titulo"])
        print("Data:", aviso["data"])
        print("Tipo:", aviso["tipo"])
        print("------------------------")


opcao = ""

while opcao != "0":
    print("\n========================")
    print("   CENTRAL DE AVISOS")
    print("========================")
    print("1 - Cadastrar aviso")
    print("2 - Listar avisos")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_aviso()
    elif opcao == "2":
        listar_avisos()
    elif opcao == "0":
        print("\nEncerrando...")
    else:
        print("\nOpção inválida.")

print("Central encerrada.")
