# Classe a ser herdada por todos as classes a serem salvas pelo BD.
import json

class Connector:
    def __init__(self, path_bd) -> None:
        self.__path_bd = path_bd

    @property
    def path_bd(self):
        return self.__path_bd
    
    @path_bd.setter
    def path_bd(self, nova_path):
        self.__path_bd = nova_path

    def criar(self, tipo, *args):
        match tipo:
            case 'Agencia':
                pass
            case 'Cliente':
                pass

            case 'Conta':
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)   #transformo json em dicionario
                    coluna_conta = data["BD"][tipo] #escolho a coluna
                    try:
                        codigo_ultimo = coluna_conta[-1]["Codigo"]  #pego o codigo da ultima conta
                    except IndexError:
                        codigo_ultimo = 0
                    coluna_conta.append({"Codigo": codigo_ultimo + 1, "Codigo_dono": args[0], "Codigo_agencia": args[1], "Tipo": args[2], "Extrato": args[3], "Saldo": args[4]})    #salvo a conta no ultimo lugar da coluna
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)    #salvo as alteracoes no bd.json
                return True

            case 'Movimento':
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)   #transformo json em dicionario
                    coluna_movimento = data["BD"][tipo] #escolho a coluna
                    try:
                        codigo_ultimo = coluna_movimento[-1]["Codigo"]  #pego o codigo da ultima conta
                    except IndexError:
                        codigo_ultimo = 0
                    coluna_movimento.append({"Codigo": codigo_ultimo + 1, "Codigo_conta_inicial": args[0], "Codigo_conta_final": args[1], "Saldo_anterior": args[2], "Saldo_posterior": args[3], "codigo_movimento_anterior": args[4], "is_Saida": args[5]})    #salvo a conta no ultimo lugar da coluna
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)    #salvo as alteracoes no bd.json
                return True
            case _:
                return None
            
    def atualizar(self, tipo, codigo, **kwargs):
        match tipo:
            case 'Agencia':
                pass
            case 'Cliente':
                pass
            case 'Conta':
                certo = False
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)
                    coluna_conta = data["BD"][tipo] #escolho a coluna
                    lugar = -1
                    for index, conta in enumerate(coluna_conta):
                        if conta["Codigo"] == codigo:
                            lugar = index
                    if lugar != -1:
                        for key, value in enumerate(kwargs.items()):
                            conta[lugar][key] = value
                        certo = True
                    else:
                        print("Objeto nao encontrado!")
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)
                return certo

            case 'Movimento':
                certo = False
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)
                    coluna_movimento = data["BD"][tipo] #escolho a coluna
                    lugar = -1
                    for index, movimento in enumerate(coluna_movimento):
                        if movimento["Codigo"] == codigo:
                            lugar = index
                    if lugar != -1:
                        for key, value in enumerate(kwargs.items()):
                            movimento[lugar][key] = value
                        certo = True
                    else:
                        print("Objeto nao encontrado!")
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)
                return certo
            case _:
                return None
            
    def deletar(self, tipo, codigo):
        match tipo:
            case 'Agencia':
                pass
            case 'Cliente':
                pass
            case 'Conta':
                certo = False
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)
                    coluna_conta = data["BD"][tipo] #escolho a coluna
                    lugar = -1
                    for index, conta in enumerate(coluna_conta):
                        if conta["Codigo"] == codigo:
                            lugar = index
                    if lugar != -1:
                        coluna_conta.pop(lugar)
                        certo = True
                    else:
                        print("Objeto nao encontrado!")
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)
                return certo

            case 'Movimento':
                certo = False
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)
                    coluna_movimento = data["BD"][tipo] #escolho a coluna
                    lugar = -1
                    for index, movimento in enumerate(coluna_movimento):
                        if movimento["Codigo"] == codigo:
                            lugar = index
                    if lugar != -1:
                        coluna_movimento.pop(lugar)
                        certo = True
                    else:
                        print("Objeto nao encontrado!")
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)
                return certo
            case _:
                return None