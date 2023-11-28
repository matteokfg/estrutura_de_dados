from connector import Connector


class Agencia(Connector):
    def __init__(self, codigo, nome, endereco, codigo_banco):
        Connector.__init__(self, "bd.json")
        self.__codigo = codigo
        self.__nome = nome
        self.__endereco = endereco
        self.__codigo_banco = codigo_banco

    def __str__(self):
        return f"Agência: {self._nome}, Endereço: {self._endereco}"
    
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