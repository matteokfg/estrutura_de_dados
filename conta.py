# Cadstro de Contas, com opção de consulta de saldo e extrato;
from connector import Connector

class Conta(Connector):
    def __init__(self, codigo, codigo_dono, codigo_agencia, tipo, codigo_ultimo_movimento, saldo = 0):
        Connector.__init__(self, 'bd.json')
        self.__codigo = codigo
        self.__codigo_dono = codigo_dono
        self.__codigo_agencia = codigo_agencia
        self.__tipo = tipo
        self.__codigo_ultimo_movimento = codigo_ultimo_movimento
        self.__saldo = saldo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def codigo_dono(self):
        return self.__codigo_dono

    @codigo_dono.setter
    def codigo_dono(self, novo_codigo_dono):
        self.__codigo_dono = novo_codigo_dono

    @property
    def codigo_agencia(self):
        return self.__codigo_agencia

    @codigo_agencia.setter
    def codigo_agencia(self, novo_codigo_agencia):
        self.__codigo_agencia = novo_codigo_agencia

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    @property
    def codigo_ultimo_movimento(self):
        return self.__codigo_ultimo_movimento

    @codigo_ultimo_movimento.setter
    def codigo_ultimo_movimento(self, novo_codigo_ultimo_movimento):
        self.__codigo_ultimo_movimento = novo_codigo_ultimo_movimento
