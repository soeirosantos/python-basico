# -*- coding: utf-8 -*-
 
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
            pass

        elif opcao == "2":
            '''
               Altera as informações de um funcionário
               específico a partir do CPF informado
            '''
            pass

        elif opcao == "3":
            '''
               Remove um funcionario específico
                a partir do CPF informado
            '''
            pass

        elif opcao == "4":
            '''
                Exibe os dados de um funcionário 
                específico a partir do CPF informado
            '''
            pass

        elif opcao == "5":    
            '''
                Exibe os dados de todos os funcionários
            '''
            pass

        elif opcao == "6":
            '''
                Finaliza o programa 
            '''
            cadastrando_funcionarios = False
        
        else:
            print "\nOpção não encontrada, por favor selecione um valor de 1 a 6.\n"
 
    print "\n:: CONTROLE DE FUNCIONARIOS FINALIZADO ::\n"

if __name__ == "__main__":
    aplicacao()