# -*- coding: utf-8 -*-

from decimal import Decimal, InvalidOperation
from datetime import date

def valido(eh_valido, msg_de_erro):
    def onDecorator(funcao_verificada):
        def onCall(self, valor_a_validar):
            sucesso = True
            if eh_valido(self, valor_a_validar):
                try:
                    return funcao_verificada(self, valor_a_validar)
                except:
                    sucesso = False
            else:
                sucesso = False

            if not sucesso:
                raise FuncionarioException(msg_de_erro)
        return onCall
    return onDecorator

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
    def salario(self):
        return self._salario

    @salario.setter
    @valido(eh_salario_valido, "Salário informado inválido!")
    def salario(self, salario):
        self._salario = Decimal(salario)

    @property
    def data_de_admissao(self):
        return self._data_de_admissao

    @data_de_admissao.setter
    @valido(eh_data_valida, "Data de Admissão informada inválida!")
    def data_de_admissao(self, data_de_admissao):
        self._data_de_admissao = str_to_date(data_de_admissao)

    @property
    def salario_anual(self):
        return self.salario * 12

    def __str__(self):
        return "%s [CPF: %s | Tel: %s | Salário anual: %.2f | Data de Admissão: %s] " % \
                    (self.nome, 
                     self.cpf, 
                     self.telefone, 
                     self.salario_anual, 
                     self._data_de_admissao.strftime('%d/%m/%Y'))


class Gerente(Funcionario):

    def __init__(self, cpf, nome, telefone, salario, data_de_admissao, gratificacao):
        Funcionario.__init__(self, cpf, nome, telefone, salario, data_de_admissao)
        self._gratificacao = Decimal(gratificacao)

    @property
    def salario_anual(self):
        return (self.salario * self._gratificacao) * 12

    def __str__(self):
        return "%s [CPF: %s | Tel: %s | Salário anual: %.2f | Gratificação total: %.2f | Data de Admissão: %s] " % \
                    (self.nome, 
                     self.cpf, 
                     self.telefone, 
                     self.salario_anual, 
                     self._gratificacao * 12,
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