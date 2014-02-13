## Cap 4) Funções e Módulos built-in

Vamos começar a extrair nosso código em funções. Observe que nós temos muitos comportamentos que estão emaranhados ao esqueleto da aplicação: validação de dados de entrada, manipulação da lista de funcionários, exibição de dados, além das nossas operações principais em si.

Declare suas funções após os imports.

1) Crie uma função para validar o salário informado. Esta função deve se chamar `eh_salario_valido`, receber o salário informado pelo usuário e retornar um booleano.

```python 

def eh_salario_valido(salario):
    '''
        recebe um salário no formato 9999.99 e retorna
        um False caso o formato seja inválido
    '''
    salario_sem_ponto = salario.replace(".","")
    return salario_sem_ponto.isdigit()

```

Agora substitua o código que realiza a validação pela chamada a função:

```python 
...
salario = raw_input("Informe o salário (Ex: 2000.40): ")

if not salario_valido(salario):
    print "\nSalário informado inválido!\n"
    continue

salario = Decimal(salario)
...

```

2) Crie agora uma função para validar a data. Essa função deve se chamar `eh_data_valida`, receber a data informada pelo usuário e retornar um booleano:

```python 

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

```

Substitua o código correspondente pela chamada a função.

3) Aproveite e crie uma função que recebe a data informada pelo usuário, em formato String, e converte para o tipo date:

```python 

def str_to_date(data):
    '''
        Converte uma String no formado dd/MM/yyyy
        em um date
    '''
    dia, mes, ano = data.split("/")
    return date(int(ano), int(mes), int(dia))



```

Substitua o código correspondente pela chamada a função.

4) Vamos criar funções para os comportamentos que manipulam nossa lista de funcionários:

a. Inicie pela inclusão, que não faz nada além de adicionar o dicionário que representa os dados do nosso funcionário à lista de funcionários:


```python 

def adicionar_funcionario(lista, funcionario):
    '''
        Adiciona um funcionário a lista
    '''
    lista.append(funcionario)


```

b. Para exibir, vamos implementar uma função que obtenha os dados do funcionário a partir do CPF informado:

```python 

def obter_funcionario(lista, cpf):
    '''
        Obtém um funcionário da lista
    '''
    f = [funcionario for funcionario in lista if funcionario["cpf"] == cpf]
    if f:
        return iter(f).next()

```

Substitua o código correspondente pela chamada a função. Observe que desta vez a alteração não é tão direta quanto a anterior:

```python 
...

cpf_a_exibir = raw_input("Informe o CPF do Funcionário que deseja exibir: ")

funcionario_a_exibir = obter_funcionario(lista_de_funcionarios, cpf_a_exibir)

if funcionario_a_exibir:
    print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario).2f | Data de Admissão: %(data_de_admissao)s] " % funcionario_a_exibir
else:
    print "\nFuncionário com CPF %s não encontrado\n " % cpf_a_exibir

...

```

c. Implemente a remoção de funcionários. Faça a função de exclusão chamar a função de obter e retorne um booleano para informar se a exclusão ocorreu:


```python 

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


```

Atualizando o código fica:

```python 
...

cpf_a_remover = raw_input("Informe o CPF do Funcionário que deseja remover: ")

removido = remover_funcionario(cpf_a_remover)

if removido:
    print "\nFuncionário com CPF %s removido\n " % cpf_a_remover
else:
    print "\nFuncionário com CPF %s não encontrado\n " % cpf_a_remover

...

```

(Altere, também, a verificação que checa se o CPF já está cadastrado utilizando a função `obter_funcionario`)

5) Melhoramos bastante nosso código removendo várias duplicações. Vamos agora implementar a funcionalidade de alteração utilizando as funções que acabamos de criar. Ao acessar a funcionalidade de alteração o usuário deverá ser perguntado sobre qual dado deseja alterar e em seguida a aplicação deve processar a alteração:

a. Implemente o menu de opções:

```python

...

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

...

```

b. Agora implemente a atualização:


```python

...

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

...

```
