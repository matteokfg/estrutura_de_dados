# melhorar agencia, tirar o cadastro para usar Connector
from connector import Connector


class Agencia(Connector):
    def __init__(self, nome, endereco, codigo_banco):
        Connector.__init__(self, "bd.json")
        self.__nome = nome
        self.__endereco = endereco
        self.__codigo_banco = codigo_banco

    def __str__(self):
        return f"Agência: {self._nome}, Endereço: {self._endereco}"

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco
    
    @property
    def codigo_banco(self):
        return self.__codigo_banco
    
    @codigo_banco.setter
    def codigo_banco(self, novo_codigo_banco):
        self.__codigo_banco = novo_codigo_banco

    def descricao(self):
        return "Agência Genérica"

class AgenciaPrincipal(Agencia):
    def descricao(self):
        return f"{self.get_nome()} - Agência Principal"

class AgenciaSecundaria(Agencia):
    def descricao(self):
        return f"{self.get_nome()} - Agência Secundária"



    # def listar_agencias(self):
    #     if self.agencias:
    #         print("Lista de agências:")
    #         for agencia in self.agencias:
    #             print(agencia)
    #     else:
    #         print("Nenhuma agência cadastrada.")


# cadastro_agencias = CadastroAgencias()

# # agencias diferentes
# agencia_principal = AgenciaPrincipal("Agência Central", "Rua Antonio Andrade, 123")
# agencia_secundaria = AgenciaSecundaria("Agência Filial", "Rua Bernardo Ferraz de Almeida, 232")

# # colocando agencias no cadastro
# cadastro_agencias.inserir_agencia(agencia_principal)
# cadastro_agencias.inserir_agencia(agencia_secundaria)

# # list agencias
# cadastro_agencias.listar_agencias()


