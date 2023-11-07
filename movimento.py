# Cadastro de Movimento, entradas, saídas e saldos, anterior e atual;

from connector import Connector

class Movimento(Connector):
    def __init__(self, codigo, codigo_conta_inicial, codigo_conta_final, saldo_anterior, saldo_posterior, codigo_movimento_anterior, is_saida = False):
        self.__codigo = codigo
        self.__codigo_conta_inicial = codigo_conta_inicial
        self.__codigo_conta_final = codigo_conta_final
        self.__saldo_anterior = saldo_anterior
        self.__saldo_posterior = saldo_posterior
        self.__codigo_movimento_anterior = codigo_movimento_anterior
        self.__is_saida = is_saida
        Connector.__init__('bd.json')

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def codigo_conta_inicial(self):
        return self.__codigo_conta_inicial

    @codigo_conta_inicial.setter
    def codigo_conta_inicial(self, novo_codigo_conta_inicial):
        self.__codigo_conta_inicial = novo_codigo_conta_inicial

    @property
    def codigo_conta_final(self):
        return self.__codigo_conta_final

    @codigo_conta_final.setter
    def codigo_conta_final(self, novo_codigo_conta_final):
        self.__codigo_conta_final = novo_codigo_conta_final

    @property
    def saldo_anterior(self):
        return self.__saldo_anterior

    @saldo_anterior.setter
    def saldo_anterior(self, novo_saldo_anterior):
        self.__saldo_anterior = novo_saldo_anterior

    @property
    def saldo_posterior(self):
        return self.__saldo_posterior

    @saldo_posterior.setter
    def saldo_posterior(self, novo_saldo_posterior):
        self.__codigo = novo_saldo_posterior

    @property
    def codigo_movimento_anterior(self):
        return self.__codigo_movimento_anterior
    
    @codigo_movimento_anterior.setter
    def codigo_movimento_anterior(self, novo_codigo_movimento_anterior):
        self.__codigo_movimento_anterior = novo_codigo_movimento_anterior

    @property
    def is_saida(self):
        return self.__is_saida

    @is_saida.setter
    def is_saida(self, novo_is_saida):
        self.__is_saida = novo_is_saida
