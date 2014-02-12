## Cap 3) Estruturas de Controle e Coleções

1) Vamos começar a guardar nossos funcionários para que possamos acessar suas informações futuramente. Primeiro, precisamos de uma estrutura de dados que nos permita armazenar cada um dos atributos de um funcionário. Vamos criar um `dicionário` para receber os dados informados pelo usuário:

```python

...

funcionario = {"cpf": cpf, 
                  "nome": nome, 
                  "telefone": telefone, 
                  "salario": salario, 
                  "data_de_ admissao": data_de_admissao}

print "\nFuncionário %s, CPF %s, cadastrado com sucesso em %s" % (nome.upper(), cpf, hoje.strftime('%d/%m/%Y'))

...

```

2) Utilize, agora, este dicionário para passar os dados para a mensagem de funcionário cadastrado:

```python
...

print "\nFuncionário %s, CPF %s, cadastrado com sucesso em %s" % (funcionario['nome'].upper(), funcionario['cpf'], hoje.strftime('%d/%m/%Y'))

...
```

3) Vamos armazenar cada funcionário criado em uma lista para acesso posterior. Para isso, exatamente antes de inciar o loop `while` principal da aplicação crie um objeto do tipo `list`:

```python

print "\n:: SISTEMA DE CONTROLE DE FUNCIONÁRIOS ::\n"

cadastrando_funcionarios = True    

lista_de_funcionarios = list()

while cadastrando_funcionarios:

```

Agora adicione o dicionário com os dados do funcionário cadastrado a essa lista:

```python
...
funcionario = {"cpf": cpf, 
               "nome": nome, 
               "telefone": telefone, 
               "salario": salario, 
               "data_de_admissao": data_de_admissao}

banco_de_funcionarios.append(funcionario)

...
```

4) Vamos implementar a funcionalidade da `opção 5`, que lista todos os funcionários cadastrados:

```python

elif opcao == "5":    
    '''
        Exibe os dados de todos os funcionários
    '''
    mensagem = "Todos os Funcionários"
    print mensagem.center(51, ":")

    for funcionario in lista_de_funcionarios:
        print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario)s | Data de Admissão: %(data_de_admissao)s] " % funcionario
...

```
(Observe que não estamos formatando a data ainda, iremos melhorar isso mais a frente)

5) Vamos exibir os dados de um funcionário específico, `opção 4`. Para isso, solicite ao usuário o cpf do funcionário a ser exibido e percorra a lista de funcionários:

```python

elif opcao == "4":
    '''
        Exibe os dados de um funcionário 
        específico a partir do CPF informado
    '''
    mensagem = "Detalhe Funcionário"
    print mensagem.center(51, ":")

    cpf_a_exibir = raw_input("Informe o CPF do Funcionário que deseja exibir: ")
    funcionario_a_exibir = None

    for funcionario in lista_de_funcionarios:
        if funcionario["cpf"] == cpf_a_exibir:
            funcionario_a_exibir = funcionario
            break

    if funcionario_a_exibir:
        print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario).2f | Data de Admissão: %(data_de_admissao)s] " % funcionario_a_exibir
    else:
        print "Funcionário com CPF %s não encontrado " % cpf_a_exibir

...

```

7) Podemos usar a mesma lógica implementada para exibir um funcionário, agora, para remover, na `opção 3`:

```python

elif opcao == "3":
    '''
       Remove um funcionario específico
        a partir do CPF informado
    '''
    mensagem = "Removendo Funcionário"
    print mensagem.center(51, ":")

    cpf_a_remover = raw_input("Informe o CPF do Funcionário que deseja remover: ")
    funcionario_a_remover = None

    for funcionario in lista_de_funcionarios:
        if funcionario["cpf"] == cpf_a_remover:
            funcionario_a_remover = funcionario
            break

    if funcionario_a_remover:
        lista_de_funcionarios.remove(funcionario_a_remover)
        print "Funcionário com CPF %s removido " % cpf_a_remover 
    else:
        print "Funcionário com CPF %s não encontrado " % cpf_a_remover

```

8) Observe que nos dois casos estamos percorrendo a lista de funcionários para selecionar o funcionário a ser exibido/removido e depois efetuando a operação, caso o funcionário tenha sido encontrado. Vamos utilizar uma list comprehension para escrever aquele loop em um jeito mais _pythonista_:

```python

cpf_a_exibir = raw_input("Informe o CPF do Funcionário que deseja exibir: ")

funcionario_a_exibir = [funcionario for funcionario in lista_de_funcionarios if funcionario["cpf"] == cpf_a_exibir]

if funcionario_a_exibir:
    funcionario_a_exibir = iter(funcionario_a_exibir).next()
    print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario).2f | Data de Admissão: %(data_de_admissao)s] " % funcionario_a_exibir
else:
    print "Funcionário com CPF %s não encontrado " % cpf_a_exibir

```

(Repare que o list comprehension retorna uma nova lista com os funcionário que atenderam ao critério no _if_, no nosso caso um elemento só, então utilizamos iter(...).next() para obter este elemento)