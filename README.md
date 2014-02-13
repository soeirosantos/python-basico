## Cap 1) Iniciando a aplicação; Trabalhando com Strings

Vamos trabalhar em cima de uma aplicação de cadastro de funcionários, construindo as principais funcionalidades relativas a Inclusão (Create), Leitura (Read), Atualização (Update) e Exclusão (Delete) de funcionários (CRUD). Iremos evoluir de maneira gradativa aplicando os recursos e conceitos que estamos aprendendo em Python até alcançar um nível bem maduro.

1) Copie o arquivo %%LOCAL%%/cadastro_funcionarios.py que contém o esqueleto da aplicação que iremos evoluir. Abra o arquivo e veja que a variável `opcao` recebe através da função `raw_input()` qual funcionalidade deve ser executada. A variável `cadastrando_funcionarios` permite que nossa aplicação continue executando dentro do bloco `while` enquanto o usuário não informar o contrário (opção 6).

2) Vamos começar identificando nossas funcionalidades, fazendo a implementação mais básica possível em cada uma delas. Imprima uma mensagem que identifique cada funcionalidade:

```python

...

if opcao == "1":
    '''
        Inclui um funcionário com os seguintes dados:
        cpf, nome, telefone, salario, data_de_admissao
    '''
    mensagem = "Cadastrando Funcionário"
    print mensagem.center(51, ":")

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

elif opcao == "4":
    '''
        Exibe os dados de um funcionário 
        específico a partir do CPF informado
    '''
    mensagem = "Detalhe Funcionário"
    print mensagem.center(51, ":")

elif opcao == "5":    
    '''
        Exibe os dados de todos os funcionários
    '''
    mensagem = "Todos os Funcionários"
    print mensagem.center(51, ":")
...

```

Para melhorar a visualização, ao final do programa imprima 100 vezes o caracter ":":

```python
...
    else:
        print "\nOpção não encontrada, por favor selecione um valor de 1 a 6.\n"
    
    print ":" * 50
print "\n:: CONTROLE DE FUNCIONARIOS FINALIZADO ::\n"
...
```

3) Inicie a funcionalidade de `Inclusão` lendo a partir do teclado os dados de um funcionário (`cpf`, `nome`, `telefone`, `salario` e `data_de_admissao`):

```python
...

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
...
```

4) Gere uma mensagem para o usuário com os dados do funcionário que acabaram de ser informados.

```python
...

if opcao == "1":
	...
    salario = raw_input("Informe o salario (Ex: 2000,40): ")
    data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

    print "Funcionário %s, CPF %s cadastrado com sucesso." % (nome, cpf)
...

```

5) Formate o nome para exibir em caixa alta na mensagem de cadastro realizado:

```python
print "Funcionário %s, CPF %s cadastrado com sucesso." % (nome.upper(), cpf)
```

6) Observe que não estamos fazendo nenhuma verificação nos valores informados em `salario` e data_de_admissao`. Vamos usar mais alguns métodos de String para checar os dados informados pelo usuário.

a. Verifique se o salário informado pelo usuário é um número:
(observe que esta validação é bem simples e não pega todos os problemas com a entrada do salário, mas, por hora, atende aos nossos objetivos didáticos)

```python
...
salario = raw_input("Informe o salário (Ex: 2000.40): ")

salario_sem_ponto = salario.replace(".","")

if not salario_sem_ponto.isdigit():
    print "\nSalário informado inválido!\n"
    continue
...
```

b. Verifique se a data informada está no formato adequado

```python
...

data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

if not (len(data_de_admissao) == 10      and \
        data_de_admissao[0:2].isdigit()  and \
        data_de_admissao[3:5].isdigit()  and \
        data_de_admissao[6:10].isdigit() and \
        "/" in (data_de_admissao[2], data_de_admissao[3])):
    print "\nData de Admissão informada inválida!\n"
    continue

print "\nFuncionário %s, CPF %s cadastrado com sucesso.\n" % (nome, cpf)
...
```