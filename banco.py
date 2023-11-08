from connector import Connector


class Banco(Connector):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        Connector.__init__('bd.json')

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