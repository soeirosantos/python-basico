# -*- coding: utf-8 -*-

from funcionarios import Funcionario, ListaDeFuncionarios, FuncionarioException
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
            nome = raw_input("Informe o nome: ")
            telefone = raw_input("Informe o telefone: ")
            salario = raw_input("Informe o salário (Ex: 2000.40): ")
            data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

            try:

                funcionario = Funcionario(cpf, nome, telefone, salario, data_de_admissao)
                lista_de_funcionarios.adicionar(funcionario)
            
            except FuncionarioException, e:
                print "\n %s \n" % e.message
                continue


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

                try:

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

                except FuncionarioException, e:
                    print "\n %s \n" % e.message
                    continue


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