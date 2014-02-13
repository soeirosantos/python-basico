## Cap 5) Orientação a Objetos I

Nesse momento temos comportamentos e dados espalhados pela nossa aplicação. Estamos trabalhando com pelo menos dois conceitos bem definidos que podem ser bem representados por objetos: Os funcionários e a lista de funcionários. O objetivo aqui é melhorar a organização do código, facilitando leitura e etendimento, evolução, entre outros.

1) Vamos começar trocando a estrutura de dados que armazena as informações de um funcionário do tipo dicionário para um tipo `Funcionario`. 

a. Crie uma classe que, no momento da instanciação, deve popular atributos com os mesmos dados de um funcionário usados até agora:

```python

class Funcionario(object):

    def __init__(self, cpf, nome, telefone, salario, data_de_admissao):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.salario = salario
        self.data_de_admissao = data_de_admissao

```

b. Agora troque o momento da criação do dicionário pela instanciação de nossa classe `Funcionario`:

```python
...
funcionario = Funcionario(cpf, nome, telefone, salario, data_de_admissao)

adicionar_funcionario(lista_de_funcionarios, funcionario)

...
```

c. Precisamos acertar todos os lugares onde o dicionário é acessado através de uma chave para o acesso usando o atributo da classe Funcionario, como no exemplo abaixo:

    trocar funcionario["nome"] por funcionario.nome

d. Observe que na hora de exibir um funcionário estamos passando um dict para a String de impressão. É possível, facilmente, manter este código funcionando utilizando o atributo `__dict__`:

```python
if funcionario_a_exibir:
    print "%(nome)s [CPF: %(cpf)s | Tel: %(telefone)s | Salário: %(salario).2f | Data de Admissão: %(data_de_admissao)s] " % funcionario_a_exibir.__dict__
else:
    print "\nFuncionário com CPF %s não encontrado\n " % cpf_a_exibir
```

(Isso é apenas para manter nosso código funcionando, vamos melhorar isso em instantes)

Aplique, também, na exibição de funcionário no momento da listagem.

2) Agora que já trouxemos nossos dados para a classe `Funcionario` vamos trazer, também, nossos comportamentos. Veja que temos alguns comportamentos de validação em cima dos dados fornecidos pelo usuário.

a. Transfome as funções `eh_salario_valido` e `eh_data_valida` em métodos da nossa classe `Funcionario`:

```python

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


```

b. Agora, no método __init__, nós iremos tratar de toda a lógica relacionada a criação de um objeto do tipo funcionário válido. Faremos isso extraindo todo código validação e conversão que está espalhado na funcionalidade de inclusão (`opção 1`) para dentro do método `__init__`:

```python
...
def __init__(self, cpf, nome, telefone, salario, data_de_admissao):
    self.cpf = cpf
    self.nome = nome
    self.telefone = telefone

    if self.eh_salario_valido(salario):
        self.salario = Decimal(salario)

    if self.eh_data_valida(data_de_admissao):
        self.data_de_admissao = str_to_date(data_de_admissao)

...
```

c. Depois de escrever esse código não esqueça de remover o código equivalente que está espalhado pela funcionalidade. Que ficará assim:

```python

if opcao == "1":
    '''
        Inclui um funcionário com os seguintes dados:
        cpf, nome, telefone, salario, data_de_admissao
    '''
    mensagem = "Cadastrando Funcionário"
    print mensagem.center(51, ":")

    cpf = raw_input("Informe o CPF: ")

    if obter_funcionario(lista_de_funcionarios, cpf):
        print "\nCPF %s, já cadastrado\n" % cpf
        continue

    nome = raw_input("Informe o nome: ")
    telefone = raw_input("Informe o telefone: ")
    salario = raw_input("Informe o salário (Ex: 2000.40): ")
    data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")
    
    funcionario = Funcionario(cpf, nome, telefone, salario, data_de_admissao)

    adicionar_funcionario(lista_de_funcionarios, funcionario)

    hoje = date.today()

    print "\nFuncionário %s, CPF %s, cadastrado com sucesso em %s" % (funcionario.nome.upper(), funcionario.cpf, hoje.strftime('%d/%m/%Y'))
    
    salario_anual = salario * 12

    print "Salário anual: R$ %.2f\n" % salario_anual

```

(Observe que perdemos as nossas mensagens de aviso ao usuário. No próximo capítulo vamos resolver isso :)

d. Repare que o cálculo do salário anual também é um comportamento do nosso funcionário, então vamos expô-lo através de uma propriedade de leitura:

```python
class Funcionario(object):

    ...

    @property
    def salario_anual(self):
        return self.salario * 12
```

Atualizando fica:

```python
...
print "Salário anual: R$ %.2f\n" % funcionario.salario_anual
...
```

3) Como você deve ter percebido, nossa funcionalidade de alteração (`opção 2`) não está mais funcionando, isso porque nós movemos as funções que fazem a validação para dentro da classe `Funcionario`. Se acertarmos este código e colocarmos para funcionar nós vamos perceber um problema: a validação do salário e da data de admissão ocorrem no método `__init__` o que significa que atribuindo valores diretamente, como estamos fazendo na alteração, irá deixar nosso objeto em um estado inválido. Para resolver isso vamos impedir a escrita direta aos atributos salario e data_de_admissao.

a. O primeiro passo é renomar os nossos atributos adicionando um `_` na frente (significa que estes atributos são para uso interno, vide PEP8)

```python

class Funcionario(object):

    def __init__(self, cpf, nome, telefone, salario, data_de_admissao):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone

        if self.eh_salario_valido(salario):
            self._salario = Decimal(salario)

        if self.eh_data_valida(data_de_admissao):
            self._data_de_admissao = str_to_date(data_de_admissao)


    ...
```

b. Isso irá quebrar nosso código que acessa esses atributos, mas já sabemos como resolver isso, basta criar propriedades de leitura que mantenham o nome utilizado externamente:

```python

class Funcionario(object):

    def __init__(self, cpf, nome, telefone, salario, data_de_admissao):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone

        if self.eh_salario_valido(salario):
            self._salario = Decimal(salario)

        if self.eh_data_valida(data_de_admissao):
            self._data_de_admissao = str_to_date(data_de_admissao)

    @property
    def salario(self):
        return self._salario

    @property
    def data_de_admissao(self):
        return self._data_de_admissao


    ...

```

c. Ok, agora precisamos intervir no momento da atribuição de valores e implementar nosso tratamento. Então vamos criar propriedades de escrita para os atributos:

```python

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
    def salario(self, value):
        if self.eh_salario_valido(value):
            self._salario = Decimal(value)

    @data_de_admissao.setter
    def data_de_admissao(self, value):
        if self.eh_data_valida(value):
            self._data_de_admissao = str_to_date(value)

```

d. Por fim, removemos todo o código desnecessário da funcionalidade de alteração, ficando:

```python
...

 elif opcao_atualizar == "3":

    novo_salario = raw_input("Informe o salário: ")
    funcionario_a_atualizar.salario = novo_salario

elif opcao_atualizar == "4":

    data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")
    funcionario_a_atualizar.data_de_admissao = data_de_admissao

...

```

4) Agora o ajuste final. Vamos criar um método chamado `__str__` que será utilizado por exibir uma saída amigável toda vez que usarmos `print`. Isso irá centralizar e padronizar a impressão dos dados de nossos funcionários. Crie esse método na nossa classe `Funcionario` e extraia para ele a String de exibição (conforme `opção 4`) fazendo os devidos ajustes:

```python

class Funcionario(object):

    ...

    def __str__(self):
        return "%s [CPF: %s | Tel: %s | Salário: %.2f | Data de Admissão: %s] " % \
                    (self.nome, 
                     self.cpf, 
                     self.telefone, 
                     self._salario, 
                     self._data_de_admissao.strftime('%d/%m/%Y'))

```

Atualize o código de exibição fazendo simplesmente:

```python

if funcionario_a_exibir:
    print funcionario_a_exibir
else:
    print "\nFuncionário com CPF %s não encontrado\n " % cpf_a_exibir


```

(Atualize, também, na listagem)

5) Faça o mesmo para a `lista_de_funcionarios`, agrupe dados e comportamentos em uma classe chamada `ListaDeFuncionarios` e acerte o código para chamar os métodos dessa classe, ao invés das funções. Ao final a classe ficará assim:

```python

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


```