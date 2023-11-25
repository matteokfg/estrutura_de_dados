# melhorar cliente, usar Connector
from connector import Connector


class Cliente(Connector):
    def __init__(self, codigo, nome, sobrenome, email):
        Connector.__init__(self, "bd.json")
        self.__codigo = codigo
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email


    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def sobrenome(self):
        return self.__sobrenome
    
    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self.__sobrenome = novo_sobrenome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        self.__email = novo_email


# sistema = SistemaCadastroClientes()


# sistema.inserir_cliente("Matteo", "Kurpjuweit", "matteo@email.com")
# sistema.inserir_cliente("Ana", "Maiello", "ana@email.com")


# sistema.listar_clientes()

# # consulta
# sistema.consultar_cliente("matteo@email.com")
# sistema.alterar_cliente("matteo@email.com", "Matteo", "Fischer", "matteo.fischer@email.com")

# # remover 
# sistema.remover_cliente("ana@email.com")

# # lista
# sistema.listar_clientes()


