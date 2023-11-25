from connector import Connector


class Banco(Connector):
    def __init__(self, codigo, nome):
        Connector.__init__(self, 'bd.json')
        self.__codigo = codigo
        self.__nome = nome

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

    def __str__(self) -> str:
        return f"Codigo: {self.__codigo}\n  Nome: {self.__nome}\n"