from agencia import Agencia
from banco import Banco
from cliente import Cliente
from conta import Conta
from connector import Connector


c = Connector('bd.json')
opcao_principal = None
while opcao_principal != "0":
    print("Banco")
    print("1 - Clientes")
    print("2 - Agências")
    print("3 - Contas")
    print("4 - Movimentos")
    print("5 - Bancos")
    print("0 - Sair")

    opcao_principal = input("Escolha uma opção: ")

    match opcao_principal:
        case "1":
            opcao_cliente = None
            while opcao_cliente != "0":
                print("Menu Clientes")
                print("1 - Cadastrar Cliente")
                print("2 - Alterar Cliente")
                print("3 - Consultar Cliente")
                print("4 - Remover Cliente")
                print("0 - Voltar")

                opcao_cliente = input("Escolha uma opção: ")
                match opcao_cliente:
                    case "1":
                        nome_cliente = input("Nome do novo cliente: ")
                        sobrenome_cliente = input("Sobrenome do novo cliente: ")
                        email_cliente = input("Email do novo cliente: ")
                        while("@" not in email_cliente):
                            email_cliente = input("Email incorreto. Email do novo cliente: ")

                        try:
                            cliente = Cliente(0, nome_cliente, sobrenome_cliente, email_cliente)
                            resultado, codigo = cliente.criar("Cliente", nome=nome_cliente, sobrenome=sobrenome_cliente, email=email_cliente)
                            print(f"Cliente criado! Com codigo: {codigo}")
                        except:
                            print("Erro!")

                    case "2":
                        print("Atualizar pelo codigo? ")
                        print("1 - Codigo")
                        print("Outro botao - Sair")
                        opcao = int(input())
                        if opcao == 1:
                            codigo_cliente = int(input("Qual o codigo do cliente? "))
                            cliente = c.procurar("Cliente", codigo_cliente)
                            if agencia is not None:
                                ins_cliente = Cliente(cliente["codigo"], cliente["nome"], cliente["sobrenome"], cliente["email"])

                                print("Valores a serem atualizados:")
                                novo_nome = input("Novo nome: ")
                                novo_sobrenome = input("Novo sobrenome: ")
                                novo_email = input("Novo email: ")

                                novos = {}
                                if novo_nome != "":
                                    novos["nome"] = novo_nome
                                if novo_sobrenome != "":
                                    novos["sobrenome"] = novo_sobrenome
                                if novo_email != "":
                                    novos["email"] = novo_email
                                
                                if novos != {}:
                                    atualizado = ins_cliente.atualizar("Cliente", cliente["codigo"], **novos)
                                    if atualizado:
                                        print("Cliente atualizado!")
                                    else:
                                        print("Erro ao atualizar")
                                else:
                                    print("Valores vazios! Impossivel atualizar")
                            else:
                                print("Cliente nao encontrado!")
                        else:
                            pass

                    case "3":
                        modo_procura = input("Como voce quer procurar o cliente?\n 1 - Nome\n 2 - Email\n ")

                        if modo_procura == "1":
                            nome_cliente = input("Nome do cliente: ")
                            cliente = c.procurar("Cliente", nome_cliente, "nome")
                            if cliente is not None:
                                print("\n  Info Cliente:")
                                for key, value in cliente.items():
                                    print(f"{key}: {value}")
                            else:
                                print("Cliente nao encontrado")
                        elif modo_procura == "2":
                            email_cliente = input("Email do cliente: ")
                            cliente = c.procurar("Cliente", email_cliente, "email")
                            if cliente is not None:
                                print("\n  Info Cliente:")
                                for key, value in cliente.items():
                                    print(f"{key}: {value}")
                            else:
                                print("Cliente nao encontrado")
                        else:
                            print("Opcao invalida.")

                    case "4":
                        codigo_cliente = int(input("Qual o codigo do cliente a ser removido: "))

                        cliente = c.procurar("Cliente", codigo_cliente)
                        if cliente is not None:
                            deletado = c.deletar("Cliente", codigo_cliente)
                            if deletado:
                                print(f"Cliente, codigo {codigo_cliente}, deletado!")
                            else:
                                print("Erro ao deletar!")
                        else:
                            print("Cliente nao encontrado")

                    case "0":
                        pass

                    case _:
                        print("Opção inválida! Tente novamente.")

        case "2":
            opcao_agencia = None
            while opcao_agencia != "0":
                print("\n==== Menu Agências ====")
                print("1 - Cadastrar Agência")
                print("2 - Alterar Agência")
                print("3 - Consultar Agência")
                print("4 - Remover Agência")
                print("0 - Voltar")

                opcao_agencia = input("Escolha uma opção: ")
                match opcao_agencia:
                    case "1":
                        nome_agencia = input("Nome da nova agencia: ")
                        endereco_agencia = input("Endereco da nova agencia: ")
                        banco = input("A agencia sera de qual banco (Nome)?\n ")

                        codigo_banco = c.procurar("Banco", banco, "nome")['codigo']

                        try:
                            agencia = Agencia(0, nome_agencia, endereco_agencia, codigo_banco)
                            resultado, codigo = agencia.criar("Agencia", nome=nome_agencia, endereco=endereco_agencia, codigo_banco=codigo_banco)
                            print(f"Agencia criada! Com codigo: {codigo}")
                        except:
                            print("Erro!")

                    case "2":
                        print("Atualizar pelo codigo? ")
                        print("1 - Codigo")
                        print("Outro botao - Sair")
                        opcao = int(input())
                        if opcao == 1:
                            codigo_agencia = int(input("Qual o codigo do agencia? "))
                            agencia = c.procurar("Banco", codigo_agencia)
                            if agencia is not None:
                                ins_agencia = Agencia(agencia["codigo"], agencia["nome"], agencia["endereco"], agencia["codigo_banco"])

                                print("Valores a serem atualizados:")
                                novo_nome = input("Novo nome: ")
                                novo_endereco = input("Novo endereco: ")
                                novo_codigo_banco = input("Novo banco (Nome): ")

                                novos = {}
                                if novo_nome != "":
                                    novos["nome"] = novo_nome
                                if novo_endereco != "":
                                    novos["endereco"] = novo_endereco
                                if novo_codigo_banco != "":
                                    novo_codigo_banco = int(novo_codigo_banco)
                                    novos["codigo_banco"] = novo_codigo_banco
                                
                                if novos != {}:
                                    atualizado = ins_agencia.atualizar("Agencia", agencia["codigo"], **novos)
                                    if atualizado:
                                        print("Agencia atualizada!")
                                    else:
                                        print("Erro ao atualizar")
                                else:
                                    print("Valores vazios! Impossivel atualizar")
                            else:
                                print("Agencia nao encontrada!")
                        else:
                            pass

                    case "3":
                        codigo_agencia = int(input("Codigo da agencia a ser consultada: "))
                        agencia = c.procurar("Agencia", codigo_agencia)
                        if agencia is not None:
                            print("\n  Info Agencia:")
                            for key, value in agencia.items():
                                print(f"{key}: {value}")
                        else:
                            print("Agencia nao encontrada")

                    case "4":
                        codigo_agencia = int(input("Codigo da agencia a ser deletada: "))
                        agencia = c.procurar("Agencia", codigo_agencia)
                        if agencia is not None:
                            deletado = c.deletar("Agencia", codigo_agencia)
                            if deletado:
                                print(f"Agencia, codigo {codigo_agencia}, deletada!")
                            else:
                                print("Erro ao deletar!")
                        else:
                            print("Agencia nao encontrada")

                    case "0":
                        pass

                    case _:
                        print("Opção inválida! Tente novamente.")

        case "3":
            opcao_conta = None
            while opcao_conta != "0":
                print("\n==== Menu Contas ====")
                print("1 - Cadastrar Conta")
                print("2 - Consultar Saldo")
                print("3 - Consultar Extrato")
                print("0 - Voltar")

                opcao_conta = input("Escolha uma opção: ")
                match opcao_conta:
                    case "1":
                        nome_dono_conta = input("Nome dono da conta: ")
                        codigo_agencia = int(input("Codigo da agencia: "))
                        tipo_conta = None
                        while tipo_conta not in ['corrente', 'especial']:
                            tipo_conta = input("Qual o tipo de conta? (Corrente, Especial)\n ").lower()
                        codigo_ultimo_movimento_conta = None
                        saldo = float(input("Saldo inicial: "))

                        codigo_dono = c.procurar("Cliente", nome_dono_conta, "nome")["codigo"]

                        try:
                            conta = Conta(0, codigo_dono, codigo_agencia, tipo_conta, codigo_ultimo_movimento_conta, saldo)
                            resultado, codigo = conta.criar("Conta", codigo_dono=codigo_dono, codigo_agencia=codigo_agencia, tipo_conta=tipo_conta, codigo_ultimo_movimento=codigo_ultimo_movimento_conta, saldo=saldo)
                            print(f"Conta cadastrada! Com codigo: {codigo}")
                        except:
                            print("Erro!")

                    case "2":
                        print("Procurando pelo codigo... ")
                        print("1 - Codigo")
                        print("Outro botao - Sair")
                        opcao = int(input())
                        if opcao == 1:
                            codigo_conta = int(input("Qual o codigo da conta? "))
                            conta = c.procurar("Conta", codigo_conta)
                            if conta is not None:
                                print(f"Saldo (R$): {conta['saldo']}")
                            else:
                                print("Conta nao encontrada!")
                        else:
                            pass

                    case "3":
                        codigo_conta = int(input("Qual o codigo da conta? "))
                        movimentos = c.listar_tabela("Movimento")

                        print(" Codigo do Movimento  |  codigo_conta_inicial    |   codigo_conta_final  |   saldo_anterior  |   saldo_posterior |   codigo_movimento_anterior   |   is_saida    |")
                        for movimento in movimentos:
                            if movimento['codigo_movimento_anterior'] == None:
                                print("---------------------------------------")
                            if movimento['codigo_conta_inicial'] == codigo_conta or movimento['codigo_conta_final'] == codigo_conta:
                                print(f"{movimento['codigo']}  |   {movimento['codigo_conta_inicial']}  |   {movimento['codigo_conta_final']}  |   {movimento['saldo_anterior']}  |   {movimento['saldo_posterior']}  | {movimento['codigo_movimento_anterior']}  |   {movimento['is_saida']}  |")

                    case "0":
                        pass

                    case _:
                        print("Opção inválida! Tente novamente.")

        case "4":
            opcao_movimento = None
            while opcao_movimento != "0":
                print("\n==== Menu Movimentos ====")
                print("1 - Cadastrar Movimento")
                print("0 - Voltar")

                opcao_movimento = input("Escolha uma opção: ")
                match opcao_movimento:
                    case "1":
                        print(" 1 - Pagar\n 2 - Receber\n Outro botao - Sair")
                        tipo_movimentacao = int(input())
                        if tipo_movimentacao == 1:
                            conta_origem = int(input("Codigo da sua conta: "))
                            conta_final = int(input("Qual o codigo da conta que voce quer pagar?\n "))
                            saldo_inicial = c.procurar("Conta", conta_origem)['saldo']
                            valor_movimentacao = float(input("Valor da transferencia (R$): "))
                            saldo_final = saldo_inicial - valor_movimentacao
                            is_saida = True

                            movimentos = c.listar_tabela("Movimento")
                            if movimentos != []:
                                ultimo_movimento = None
                                for movimento in movimentos:
                                    if (movimento['codigo_conta_inicial'] == conta_origem) or (movimento['codigo_conta_final'] == conta_origem):
                                        ultimo_movimento = movimento
                                codigo_movimento_anterior = ultimo_movimento['codigo']
                            else:
                                codigo_movimento_anterior = None

                            resultado, codigo = c.criar("Movimento", 
                                                        codigo_conta_inicial=conta_origem, 
                                                        codigo_conta_final=conta_final, 
                                                        saldo_anterior=saldo_inicial, 
                                                        saldo_posterior=saldo_final, 
                                                        codigo_movimento_anterior=codigo_movimento_anterior, 
                                                        is_saida=is_saida)
                            if resultado:
                                print(f"Movimento criado! Com codigo: {codigo}")
                                atualizada_conta_origem = c.atualizar("Conta", conta_origem, saldo=saldo_final)
                                if atualizada_conta_origem:
                                    atualizada_conta_final = c.atualizar("Conta", conta_final, saldo=c.procurar("Conta", conta_final)['saldo'] + valor_movimentacao)
                                    if not atualizada_conta_final:
                                        print("Erro ao atualizar a conta final")
                                else:
                                    print("Erro ao atualizar saldo da conta origem")
                            else:
                                print("Erro!")
                        elif tipo_movimentacao == 2:
                            conta_origem = int(input("Qual o codigo da conta que voce quer receber?\n "))
                            conta_final = int(input("Codigo da sua conta: "))
                            saldo_inicial = c.procurar("Conta", conta_origem)['saldo']
                            valor_movimentacao = float(input("Valor da transferencia (R$): "))
                            saldo_final = saldo_inicial + valor_movimentacao
                            is_saida = False

                            movimentos = c.listar_tabela("Movimento")
                            ultimo_movimento = None
                            for movimento in movimentos:
                                if (movimento['codigo_conta_inicial'] == conta_origem) or (movimento['codigo_conta_final'] == conta_origem):
                                    ultimo_movimento = movimento
                            codigo_movimento_anterior = movimento['codigo']

                            resultado, codigo = c.criar("Movimento", 
                                                        codigo_conta_inicial=conta_origem, 
                                                        codigo_conta_final=conta_final, 
                                                        saldo_anterior=saldo_inicial, 
                                                        saldo_posterior=saldo_final, 
                                                        codigo_movimento_anterior=codigo_movimento_anterior, 
                                                        is_saida=is_saida)
                            if resultado:
                                print(f"Movimento criado! Com codigo: {codigo}")
                                atualizada_conta_origem = c.atualizar("Conta", conta_final, saldo=c.procurar("Conta", conta_final)['saldo'] - valor_movimentacao)
                                if atualizada_conta_origem:
                                    atualizada_conta_final = c.atualizar("Conta", conta_origem, saldo=saldo_final)
                                    if not atualizada_conta_final:
                                        print("Erro ao atualizar a sua final")
                                else:
                                    print("Erro ao atualizar saldo da conta origem")
                            else:
                                print("Erro!")
                        else:
                            pass

                    case "0":
                        pass

                    case _:
                        print("Opção inválida! Tente novamente.")

        case "5":
            opcao_banco = None
            while opcao_banco != "0":
                print("\n==== Menu Bancos ====")
                print("1 - Cadastrar Banco")
                print("2 - Alterar Banco")
                print("3 - Consultar Banco")
                print("4 - Remover Banco")
                print("0 - Voltar")

                opcao_banco = input("Escolha uma opção: ")
                match opcao_banco:
                    case "1":
                        nome_banco = input("Qual o nome do novo banco?\n  ")

                        try:
                            banco = Banco(0, nome_banco)
                            resultado, codigo = banco.criar("Banco", nome=nome_banco)
                            print(f"Banco cadastrado! Com codigo: {codigo}")
                        except:
                            print("Erro!")

                    case "2":
                        print("Atualizar pelo codigo? ")
                        print("1 - Codigo")
                        print("Outro botao - Sair")
                        opcao = int(input())
                        if opcao == 1:
                            codigo_banco = int(input("Qual o codigo do banco? "))
                            banco = c.procurar("Banco", codigo_banco)
                            if banco is not None:
                                print("Valores a serem atualizados:")
                                novo_nome = input("Novo nome: ")
                                if novo_nome != "":
                                    ins_banco = Banco(banco["codigo"], banco["nome"])
                                    atualizado = ins_banco.atualizar("Banco", banco["codigo"], nome=novo_nome)
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

                    case "3":
                        print("Procurar pelo nome ou pelo codigo? ")
                        print("1 - Codigo")
                        print("2 - Nome")
                        print("Outro botao - Sair")
                        opcao = int(input())
                        if opcao == 1:
                            codigo_banco = int(input("Qual o codigo do banco? "))
                            banco = c.procurar("Banco", codigo_banco)
                            if banco is not None:
                                print("\n  Info Banco:")
                                for key, value in banco.items():
                                    print(f"{key}: {value}")
                            else:
                                print("Banco nao encontrado!")
                        elif opcao == 2:
                            nome_banco = input("Qual o nome do banco? ")
                            c = Connector('bd.json')
                            banco = c.procurar("Banco", nome_banco, "nome")
                            if banco is not None:
                                print("\n  Info Banco:")
                                for key, value in banco.items():
                                    print(f"{key}: {value}")
                            else:
                                print("Banco nao encontrado!")
                        else:
                            pass

                    case "4":
                        print("Deletar pelo codigo? ")
                        print("1 - Codigo")
                        print("Outro botao - Sair")
                        opcao = int(input())
                        if opcao == 1:
                            codigo_banco = int(input("Qual o codigo do banco? "))
                            deletado = c.deletar("Banco", codigo_banco)
                            if banco is not None:
                                print("Banco deletado!")
                            else:
                                print("Banco nao encontrado!")
                        else:
                            pass

                    case "0":
                        pass

                    case _:
                        print("Opção inválida! Tente novamente.")

        case "0":
            input("Aperte qualquer botao para sair...")
            print("Encerrando programa...")
            print("Encerrado!")

        case _:
            print("Opção inválida! Tente novamente.")