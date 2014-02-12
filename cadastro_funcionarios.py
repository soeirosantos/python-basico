# -*- coding: utf-8 -*-
 
from decimal import Decimal
from datetime import date

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
            nome = raw_input("Informe o nome: ")
            telefone = raw_input("Informe o telefone: ")
            salario = raw_input("Informe o salário (Ex: 2000.40): ")

            salario_sem_ponto = salario.replace(".","")

            if not salario_sem_ponto.isdigit():
                print "\nSalário informado inválido!\n"
                continue

            salario = Decimal(salario)

            data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

            if not (len(data_de_admissao) == 10      and \
                    data_de_admissao[0:2].isdigit()  and \
                    data_de_admissao[3:5].isdigit()  and \
                    data_de_admissao[6:10].isdigit() and \
                    "/" in (data_de_admissao[2], data_de_admissao[3])):

                print "\nData de Admissão informada inválida!\n"
                continue

            dia, mes, ano = data_de_admissao.split("/")

            data_de_admissao = date(int(ano), int(mes), int(dia))

            hoje = date.today()

            funcionario = {"cpf": cpf, 
                           "nome": nome, 
                           "telefone": telefone, 
                           "salario": salario, 
                           "data_de_admissao": data_de_admissao}

            lista_de_funcionarios.append(funcionario)

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

        elif opcao == "3":
            '''
               Remove um funcionario específico
                a partir do CPF informado
            '''
            mensagem = "Removendo Funcionário"
            print mensagem.center(51, ":")

            cpf_a_remover = raw_input("Informe o CPF do Funcionário que deseja remover: ")

            funcionario_a_remover = [funcionario for funcionario in lista_de_funcionarios if funcionario["cpf"] == cpf_a_remover]

            for funcionario in lista_de_funcionarios:
                if funcionario["cpf"] == cpf_a_remover:
                    funcionario_a_remover = funcionario
                    break

            if funcionario_a_remover:
                lista_de_funcionarios.remove(funcionario_a_remover)
                print "Funcionário com CPF %s removido " % cpf_a_remover
            else:
                print "Funcionário com CPF %s não encontrado " % cpf_a_remover

        elif opcao == "4":
            '''
                Exibe os dados de um funcionário 
                específico a partir do CPF informado
            '''
            mensagem = "Detalhe Funcionário"
            print mensagem.center(51, ":")

            cpf_a_exibir = raw_input("Informe o CPF do Funcionário que deseja exibir: ")

            funcionario_a_exibir = [funcionario for funcionario in lista_de_funcionarios if funcionario["cpf"] == cpf_a_exibir]

            if funcionario_a_exibir:
                funcionario_a_exibir = iter(funcionario_a_exibir).next()
                print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario).2f | Data de Admissão: %(data_de_admissao)s] " % funcionario_a_exibir
            else:
                print "Funcionário com CPF %s não encontrado " % cpf_a_exibir

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