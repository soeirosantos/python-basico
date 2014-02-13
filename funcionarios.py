# -*- coding: utf-8 -*-

from decimal import Decimal, InvalidOperation
from datetime import date

class FuncionarioException(Exception):
    
    def __init__(self, message):
        Exception.__init__(self, message)

class Funcionario(object):

    def __init__(self, cpf, nome, telefone, salario, data_de_admissao):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.salario = salario
        self.data_de_admissao = data_de_admissao
        
    @property
    def salario(self):
        return self._salario

    @property
    def data_de_admissao(self):
        return self._data_de_admissao

    @salario.setter
    def salario(self, salario):

        sucesso = True

        if self.eh_salario_valido(salario):
            try:
                self._salario = Decimal(salario)
            except InvalidOperation:
                sucesso = False
        else:
            sucesso = False

        if not sucesso:
            raise FuncionarioException("Salário informado inválido!")

    @data_de_admissao.setter
    def data_de_admissao(self, data_de_admissao):

        sucesso = True

        if self.eh_data_valida(data_de_admissao):
            try:
                self._data_de_admissao = str_to_date(data_de_admissao)
            except ValueError:
                sucesso = False
        else:
            sucesso = False

        if not sucesso:
            raise FuncionarioException("Data de Admissão informada inválida!")

    def eh_salario_valido(self, salario):
        '''
            recebe um salário no formato 9999.99 e retorna
            um False caso o formato seja inválido
        '''
        salario_sem_ponto = salario.replace(".","")
        return salario_sem_ponto.isdigit()

    def eh_data_valida(self, data):
        '''
            recebe uma data dd/MM/yyyy e retorna
            um False caso o formato seja inválido
        '''
        return (len(data) == 10      and \
                data[0:2].isdigit()  and \
                data[3:5].isdigit()  and \
                data[6:10].isdigit() and \
                "/" in (data[2], data[3]))

    @property
    def salario_anual(self):
        return self.salario * 12

    def __str__(self):
        return "%s [CPF: %s | Tel: %s | Salário: %.2f | Data de Admissão: %s] " % \
                    (self.nome, 
                     self.cpf, 
                     self.telefone, 
                     self._salario, 
                     self._data_de_admissao.strftime('%d/%m/%Y'))


def str_to_date(data):
    '''
        Converte uma String no formado dd/MM/yyyy
        em um date
    '''
    dia, mes, ano = data.split("/")
    return date(int(ano), int(mes), int(dia))

class ListaDeFuncionarios(object):

    def __init__(self):
        self._values = list()

    def adicionar(self, funcionario):
        '''
            Adiciona um funcionário a lista
        '''
        if self.obter(funcionario.cpf):
            raise FuncionarioException("CPF %s, já cadastrado" % funcionario.cpf)

        self._values.append(funcionario)

    def obter(self, cpf):
        '''
            Obtém um funcionário da lista
        '''
        f = [funcionario for funcionario in self._values if funcionario.cpf == cpf]
        if f:
            return iter(f).next()

    def remover(self, cpf):
        '''
            Remove um funcionário da lista
        '''
        a_remover = self.obter(cpf)
        if a_remover:
            self._values.remove(a_remover)
            return True
        else:
            return False

    def todos(self):
        return self._values