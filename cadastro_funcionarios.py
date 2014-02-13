# -*- coding: utf-8 -*-
 
from decimal import Decimal
from datetime import date

def eh_salario_valido(salario):
    '''
        recebe um salário no formato 9999.99 e retorna
        um False caso o formato seja inválido
    '''
    salario_sem_ponto = salario.replace(".","")
    return salario_sem_ponto.isdigit()

def eh_data_valida(data):
    '''
        recebe uma data dd/MM/yyyy e retorna
        um False caso o formato seja inválido
    '''
    return (len(data) == 10      and \
            data[0:2].isdigit()  and \
            data[3:5].isdigit()  and \
            data[6:10].isdigit() and \
            "/" in (data[2], data[3]))


def str_to_date(data):
    '''
        Converte uma String no formado dd/MM/yyyy
        em um date
    '''
    dia, mes, ano = data.split("/")
    return date(int(ano), int(mes), int(dia))

def adicionar_funcionario(lista, funcionario):
    '''
        Adiciona um funcionário a lista
    '''
    lista.append(funcionario)

def obter_funcionario(lista, cpf):
    '''
        Obtém um funcionário da lista
    '''
    f = [funcionario for funcionario in lista if funcionario["cpf"] == cpf]
    if f:
        return iter(f).next()

def remover_funcionario(lista, cpf):
    '''
        Remove um funcionário da lista
    '''
    a_remover = obter_funcionario(lista, cpf)
    if a_remover:
        lista.remove(a_remover)
        return True
    else:
        return False

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
 
    lista_de_funcionarios = list()

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

            if cpf in [funcionario["cpf"] for funcionario in lista_de_funcionarios]:
                print "\nCPF %s, já cadastrado\n" % cpf
                continue

            nome = raw_input("Informe o nome: ")
            telefone = raw_input("Informe o telefone: ")
            salario = raw_input("Informe o salário (Ex: 2000.40): ")

            if not eh_salario_valido(salario):
                print "\nSalário informado inválido!\n"
                continue

            salario = Decimal(salario)

            data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

            if not eh_data_valida(data_de_admissao):
                print "\nData de Admissão informada inválida!\n"
                continue

            data_de_admissao = str_to_date(data_de_admissao)

            hoje = date.today()

            funcionario = {"cpf": cpf, 
                           "nome": nome, 
                           "telefone": telefone, 
                           "salario": salario, 
                           "data_de_admissao": data_de_admissao}

            adicionar_funcionario(lista_de_funcionarios, funcionario)

            print "\nFuncionário %s, CPF %s, cadastrado com sucesso em %s" % (funcionario['nome'].upper(), funcionario['cpf'], hoje.strftime('%d/%m/%Y'))
            
            salario_anual = salario * 12

            print "Salário anual: R$ %.2f\n" % salario_anual

        elif opcao == "2":
            '''
               Altera as informações de um funcionário
               específico a partir do CPF informado
            '''
            mensagem = "Atualizando Funcionário"
            print mensagem.center(51, ":")

            cpf_a_atualizar = raw_input("Informe o CPF do Funcionário que deseja atualizar: ")

            funcionario_a_atualizar = obter_funcionario(lista_de_funcionarios, cpf_a_atualizar)

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
                    funcionario_a_atualizar["nome"] = novo_nome

                elif opcao_atualizar == "2":

                    novo_telefone = raw_input("Informe o telefone: ")
                    funcionario_a_atualizar["telefone"] = novo_telefone
                
                elif opcao_atualizar == "3":

                    novo_salario = raw_input("Informe o salário: ")
                    
                    if not eh_salario_valido(novo_salario):
                        print "\nSalário informado inválido!\n"
                        continue

                    funcionario_a_atualizar["salario"] = Decimal(novo_salario)

                elif opcao_atualizar == "4":

                    data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

                    if not eh_data_valida(data_de_admissao):
                        print "\nData de Admissão informada inválida!\n"
                        continue

                    funcionario_a_atualizar["data_de_admissao"] = str_to_date(data_de_admissao)

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

            removido = remover_funcionario(lista_de_funcionarios, cpf_a_remover)

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

            funcionario_a_exibir = obter_funcionario(lista_de_funcionarios, cpf_a_exibir)

            if funcionario_a_exibir:
                print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario).2f | Data de Admissão: %(data_de_admissao)s] " % funcionario_a_exibir
            else:
                print "\nFuncionário com CPF %s não encontrado\n " % cpf_a_exibir

        elif opcao == "5":    
            '''
                Exibe os dados de todos os funcionários
            '''
            mensagem = "Todos os Funcionários"
            print mensagem.center(51, ":")

            for funcionario in lista_de_funcionarios:
                print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario).2f | Data de Admissão: %(data_de_admissao)s] " % funcionario

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