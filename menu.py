from agencia import Agencia
from banco import Banco
from cliente import Cliente
from conta import Conta
from movimento import Movimento
from connector import Connector

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
                pass
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
                pass
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
                nome_dono_conta = input()
                nome_agencia = input()
                tipo_conta = input()
                codigo_ultimo_movimento_conta = None
                saldo = 0

                c = Connector('bd.json')

                codigo_dono = c.procurar("Cliente", nome_dono_conta, "nome")["codigo"]
                codigo_agencia = c.procurar("Agencia", nome_agencia, "nome")["codigo"]

                conta = Conta(0, codigo_dono, codigo_agencia, tipo_conta, codigo_ultimo_movimento_conta)
                resultado, codigo = conta.criar("Conta", 
                                                codigo_dono=codigo_dono, 
                                                codigo_agencia=codigo_agencia, 
                                                tipo=tipo_conta, 
                                                codigo_ultimo_movimento=codigo_ultimo_movimento_conta, 
                                                saldo=saldo)
                if resultado:
                    print(f"Conta cadastrada! Com codigo: {codigo}")
                else:
                    print("Erro!")

            elif opcao_conta == 2:
                print("Procurando pelo codigo... ")
                print("1 - Codigo")
                print("Outro botao - Sair")
                opcao = int(input())
                if opcao == 1:
                    codigo_conta = input("Qual o codigo da conta? ")
                    c = Connector('bd.json')
                    conta = c.procurar("Conta", codigo_conta)
                    if conta is not None:
                        print(f"Saldo (R$): {conta['saldo']}")
                    else:
                        print("Conta nao encontrada!")
                else:
                    pass

            elif opcao_conta == 3:
                consultar_extrato()
            elif opcao_conta == 0:
                pass
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
                pass
            else:
                print("Opção inválida! Tente novamente.")

    #feito
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
                resultado, codigo = banco.criar("Banco", nome=nome_banco)
                if resultado:
                    print(f"Banco cadastrado! Com codigo: {codigo}")
                else:
                    print("Erro!")

            elif opcao_banco == 2:
                print("Atualizar pelo codigo? ")
                print("1 - Codigo")
                print("Outro botao - Sair")
                opcao = int(input())
                if opcao == 1:
                    codigo_banco = input("Qual o codigo do banco? ")
                    c = Connector('bd.json')
                    banco = c.procurar("Banco", codigo_banco)
                    if banco is not None:
                        print("Valores a serem atualizados:")
                        novo_nome = input("Novo nome: ")
                        if novo_nome != "":
                            ins_banco = Banco(banco["codigo"], banco["nome"])
                            atualizado = Banco.atualizar("Banco", banco["codigo"], nome=novo_nome)
                            if atualizado:
                                print("Banco atualizado!")
                            else:
                                print("Erro ao cadastrar")
                        else:
                            print("Nome nao pode ser vazio!")
                    else:
                        print("Banco nao encontrado!")
                else:
                    pass

            elif opcao_banco == 3:
                print("Procurar pelo nome ou pelo codigo? ")
                print("1 - Codigo")
                print("2 - Nome")
                print("Outro botao - Sair")
                opcao = int(input())
                if opcao == 1:
                    codigo_banco = input("Qual o codigo do banco? ")
                    c = Connector('bd.json')
                    banco = c.procurar("Banco", codigo_banco)
                    if banco is not None:
                        print(f"Info Banco:\n  Codigo: {banco['codigo']}\n  Nome: {banco['nome']}")
                        pass
                    else:
                        print("Banco nao encontrado!")
                elif opcao == 2:
                    nome_banco = input("Qual o nome do banco? ")
                    c = Connector('bd.json')
                    banco = c.procurar("Banco", nome_banco, "nome")
                    if banco is not None:
                        print(f"Info Banco:\n  Codigo: {banco['codigo']}\n  Nome: {banco['nome']}")
                        pass
                    else:
                        print("Banco nao encontrado!")
                else:
                    pass

            elif opcao_banco == 4:
                print("Deletar pelo codigo? ")
                print("1 - Codigo")
                print("Outro botao - Sair")
                opcao = int(input())
                if opcao == 1:
                    codigo_banco = input("Qual o codigo do banco? ")
                    c = Connector('bd.json')
                    deletado = c.deletar("Banco", codigo_banco)
                    if banco is not None:
                        print("Banco deletado!")
                    else:
                        print("Banco nao encontrado!")
                else:
                    pass

            elif opcao_banco == 0:
                pass

            else:
                print("Opção inválida! Tente novamente.")
    #feito
    elif opcao_principal == 0:
        input("Aperte qualquer botao para sair...")
        print("Encerrando programa...")
        print("Encerrado!")
    #feito
    else:
        print("Opção inválida! Tente novamente.")
