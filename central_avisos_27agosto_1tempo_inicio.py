# CENTRAL DE AVISOS — 27/08/2026 — 1º TEMPO
# Código inicial da aula
# Objetivo: transformar a opção 1 em um cadastro real de avisos.

avisos = []

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
        print("\nCadastro ainda será implementado.")

    elif opcao == "2":
        print("\nListagem será implementada no 2º tempo.")

    elif opcao == "0":
        print("\nEncerrando...")

    else:
        print("\nOpção inválida.")

print("Central encerrada.")
