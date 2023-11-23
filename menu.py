from agencia import Agencia
from banco import Banco
from cliente import Cliente
from conta import Conta
from movimento import Movimento

# cadastrar_agencia()

# alterar_agencia()

# consultar_agencia()

# remover_agencia()

# cadastrar_conta()

# consultar_saldo()

# consultar_extrato()

# cadastrar_movimento()

opcao_principal = None
while opcao_principal != 0:
    print("Banco")
    print("1 - Clientes")
    print("2 - Agências")
    print("3 - Contas")
    print("4 - Movimentos")
    print("5 - Bancos")
    print("0 - Sair")

    opcao_principal = input("Escolha uma opção: ")

    if opcao_principal == 1:
        opcao_cliente = None
        while opcao_cliente != 0:
            print("Menu Clientes")
            print("1 - Cadastrar Cliente")
            print("2 - Alterar Cliente")
            print("3 - Consultar Cliente")
            print("4 - Remover Cliente")
            print("0 - Voltar")

            opcao_cliente = input("Escolha uma opção: ")

            if opcao_cliente == 1:
                cadastrar_cliente()
            elif opcao_cliente == 2:
                alterar_cliente()
            elif opcao_cliente == 3:
                consultar_cliente()
            elif opcao_cliente == 4:
                remover_cliente()
            elif opcao_cliente == 0:
                break
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao_principal == 2:
        opcao_agencia = None
        while opcao_agencia != 0:
            print("\n==== Menu Agências ====")
            print("1 - Cadastrar Agência")
            print("2 - Alterar Agência")
            print("3 - Consultar Agência")
            print("4 - Remover Agência")
            print("0 - Voltar")

            opcao_agencia = input("Escolha uma opção: ")

            if opcao_agencia == 1:
                cadastrar_agencia()
            elif opcao_agencia == 2:
                alterar_agencia()
            elif opcao_agencia == 3:
                consultar_agencia()
            elif opcao_agencia == 4:
                remover_agencia()
            elif opcao_agencia == 0:
                break
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao_principal == 3:
        opcao_conta = None
        while opcao_conta != 0:
            print("\n==== Menu Contas ====")
            print("1 - Cadastrar Conta")
            print("2 - Consultar Saldo")
            print("3 - Consultar Extrato")
            print("0 - Voltar")

            opcao_conta = input("Escolha uma opção: ")

            if opcao_conta == 1:
                cadastrar_conta()
            elif opcao_conta == 2:
                consultar_saldo()
            elif opcao_conta == 3:
                consultar_extrato()
            elif opcao_conta == 0:
                break
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao_principal == 4:
        opcao_movimento = None
        while opcao_movimento != 0:
            print("\n==== Menu Movimentos ====")
            print("1 - Cadastrar Movimento")
            print("0 - Voltar")

            opcao_movimento = input("Escolha uma opção: ")

            if opcao_movimento == 1:
                cadastrar_movimento()
            elif opcao_movimento == 0:
                break
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao_principal == 5:
        opcao_banco = None
        while opcao_banco != 0:
            print("\n==== Menu Bancos ====")
            print("1 - Cadastrar Banco")
            print("2 - Alterar Banco")
            print("3 - Consultar Banco")
            print("4 - Remover Banco")
            print("0 - Voltar")

            opcao_banco = input("Escolha uma opção: ")

            if opcao_banco == 1:
                nome_banco = input("Qual o nome do novo banco?\n  ")
                banco = Banco(0, nome_banco)
                if banco.criar("Banco", nome=nome_banco):
                    print("Banco cadastrado!")
                else:
                    print("Erro!")
            elif opcao_banco == 2:
                alterar_agencia()
            elif opcao_banco == 3:
                consultar_agencia()
            elif opcao_banco == 4:
                remover_agencia()
            elif opcao_banco == 0:
                break
            else:
                print("Opção inválida! Tente novamente.")

    elif opcao_principal == 0:
        encerrar_programa = True

    else:
        print("Opção inválida! Tente novamente.")
