# -*- coding: utf-8 -*-
 
from decimal import Decimal
from datetime import date

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
        if self.eh_salario_valido(salario):
            self._salario = Decimal(salario)
        else:
            self._salario = Decimal(0)

    @data_de_admissao.setter
    def data_de_admissao(self, data_de_admissao):
        if self.eh_data_valida(data_de_admissao):
            self._data_de_admissao = str_to_date(data_de_admissao)
        else:
            self._data_de_admissao = date.today()
            
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

def aplicacao():
    '''
        Programa que controla o cadastro de 
        funcionários com as funcionalidades de 
        -- Inclusão
        -- Alteração
        -- Exclusão
        -- Listagem de todos os Funcionários
        -- Exibição dos dados de um Funcionário
    '''
    
    print "\n:: SISTEMA DE CONTROLE DE FUNCIONÁRIOS ::\n"

    cadastrando_funcionarios = True    
 
    lista_de_funcionarios = ListaDeFuncionarios()

    while cadastrando_funcionarios:
        print "O que você deseja fazer?"
        print "1 - Incluir um funcionário"
        print "2 - Alterar um funcionário"
        print "3 - Remover um funcionário"
        print "4 - Exbir dados de um funcionário"
        print "5 - Listar todos os funcionários"
        print "6 - Sair"
        
        opcao = raw_input("Escolha uma opção:")
 
        if opcao == "1":
            '''
                Inclui um funcionário com os seguintes dados:
                cpf, nome, telefone, salario, data_de_admissao
            '''
            mensagem = "Cadastrando Funcionário"
            print mensagem.center(51, ":")

            cpf = raw_input("Informe o CPF: ")

            if lista_de_funcionarios.obter(cpf):
                print "\nCPF %s, já cadastrado\n" % cpf
                continue

            nome = raw_input("Informe o nome: ")
            telefone = raw_input("Informe o telefone: ")
            salario = raw_input("Informe o salário (Ex: 2000.40): ")
            data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

            funcionario = Funcionario(cpf, nome, telefone, salario, data_de_admissao)

            lista_de_funcionarios.adicionar(funcionario)

            hoje = date.today()
            print "\nFuncionário %s, CPF %s, cadastrado com sucesso em %s" % (funcionario.nome.upper(), funcionario.cpf, hoje.strftime('%d/%m/%Y'))
            
            print "Salário anual: R$ %.2f\n" % funcionario.salario_anual

        elif opcao == "2":
            '''
               Altera as informações de um funcionário
               específico a partir do CPF informado
            '''
            mensagem = "Atualizando Funcionário"
            print mensagem.center(51, ":")

            cpf_a_atualizar = raw_input("Informe o CPF do Funcionário que deseja atualizar: ")

            funcionario_a_atualizar = lista_de_funcionarios.obter(cpf_a_atualizar)

            if not funcionario_a_atualizar:
                print "Funcionário com CPF %s não encontrado " % cpf_a_atualizar
                continue

            atualizando_funcionario = True

            while atualizando_funcionario:
                print "O que você deseja atualizar?"
                print "1 - Nome"
                print "2 - Telefone"
                print "3 - Salário"
                print "4 - Data de admissão"

                opcao_atualizar = raw_input("Escolha uma opção a atualizar:")

                if opcao_atualizar == "1":
                    
                    novo_nome = raw_input("Informe o nome: ")
                    funcionario_a_atualizar.nome = novo_nome

                elif opcao_atualizar == "2":

                    novo_telefone = raw_input("Informe o telefone: ")
                    funcionario_a_atualizar.telefone = novo_telefone
                
                elif opcao_atualizar == "3":

                    novo_salario = raw_input("Informe o salário: ")
                    funcionario_a_atualizar.salario = novo_salario

                elif opcao_atualizar == "4":

                    data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")
                    funcionario_a_atualizar.data_de_admissao = data_de_admissao

                atualizando_funcionario = False

                print "\nFuncionário com CPF %s atualizado\n" % cpf_a_atualizar

        elif opcao == "3":
            '''
               Remove um funcionario específico
                a partir do CPF informado
            '''
            mensagem = "Removendo Funcionário"
            print mensagem.center(51, ":")

            cpf_a_remover = raw_input("Informe o CPF do Funcionário que deseja remover: ")

            removido = lista_de_funcionarios.remover(cpf_a_remover)

            if removido:
                print "\nFuncionário com CPF %s removido\n " % cpf_a_remover
            else:
                print "\nFuncionário com CPF %s não encontrado\n " % cpf_a_remover

        elif opcao == "4":
            '''
                Exibe os dados de um funcionário 
                específico a partir do CPF informado
            '''
            mensagem = "Detalhe Funcionário"
            print mensagem.center(51, ":")

            cpf_a_exibir = raw_input("Informe o CPF do Funcionário que deseja exibir: ")

            funcionario_a_exibir = lista_de_funcionarios.obter(cpf_a_exibir)

            if funcionario_a_exibir:
                print funcionario_a_exibir
            else:
                print "\nFuncionário com CPF %s não encontrado\n " % cpf_a_exibir

        elif opcao == "5":    
            '''
                Exibe os dados de todos os funcionários
            '''
            mensagem = "Todos os Funcionários"
            print mensagem.center(51, ":")

            for funcionario in lista_de_funcionarios.todos():
                print funcionario

        elif opcao == "6":
            '''
                Finaliza o programa 
            '''
            cadastrando_funcionarios = False
        
        else:
            print "\nOpção não encontrada, por favor selecione um valor de 1 a 6.\n"
        
        print ":" * 50
    print "\n:: CONTROLE DE FUNCIONARIOS FINALIZADO ::\n"

if __name__ == "__main__":
    aplicacao()