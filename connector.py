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
            case "Agencia":
                pass
            case 'Cliente':
                pass

            case 'Conta':
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)   #transformo json em dicionario
                    coluna_conta = data["BD"][tipo] #escolho a coluna
                    codigo_ultimo = coluna_conta[-1]["Codigo"]  #pego o codigo da ultima conta
                    coluna_conta.append({"Codigo": codigo_ultimo + 1, "Codigo_dono": args[1], "Codigo_agencia": args[2], "Tipo": args[3], "Extrato": args[4], "Saldo": args[5]})    #salvo a conta no ultimo lugar da coluna
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)    #salvo as alteracoes no bd.json

            case 'Movimento':
                with open(self.path_bd) as bd_json:
                    data = json.load(bd_json)   #transformo json em dicionario
                    coluna_movimento = data["BD"][tipo] #escolho a coluna
                    codigo_ultimo = coluna_movimento[-1]["Codigo"]  #pego o codigo da ultima conta
                    coluna_movimento.append({"Codigo": codigo_ultimo + 1, "Codigo_conta_inicial": args[1], "Codigo_conta_final": args[2], "Saldo_anterior": args[3], "Saldo_posterior": args[4], "codigo_movimento_anterior": args[5], "is_Saida": args[6]})    #salvo a conta no ultimo lugar da coluna
                with open(self.path_bd, 'w') as bd_json:
                    json.dump(data, bd_json)    #salvo as alteracoes no bd.json
            case _:
                return None