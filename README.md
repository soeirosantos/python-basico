## Cap 6) Tratamento de Exceções

1) Vamos começar melhorando a organização do nosso código. O arquivo `cadastro_funcionarios.py` já está muito grande, dificultando a leitura do código e evolução. Vamos criar um módulo para conter toda a implementação relacionada a funcionários.

a. No mesmo diretório do arquivo cadastro_funcionarios.py crie um arquivo chamado `__init__.py` vazio;

b. Agora crie um arquivo chamado `funcionarios.py` e mova para ele o código das classes `Funcionario`, `ListaDeFuncionarios` e da função `str_to_date` (não esqueça de mover os imports utilizados por estas classes);

c. Adicione no arquivo cadastro_funcionarios.py o import das classes:

```python

from funcionarios import Funcionario, ListaDeFuncionarios

```

2) Estamos fazendo um tratamento bem básico nos dados de entrada `data_de_admissao` e `salario`. Na hora que vamos criar os objetos `date` e `Decimal` vários problemas podem ocorrer além das situações que estamos verificando. Não queremos que a execução do nosso programa pare por situações inesperadas, então vamos melhorar o nosso tratamento de erro.

(Ex: 222.222.22 irá lançar decimal.InvalidOperation e 20/13/2011 irá lançar ValueError)

a. Na propriedade de escrita `salario` faça:

```python
@salario.setter
def salario(self, salario):
    if self.eh_salario_valido(salario):
        
        try:
            self._salario = Decimal(salario)
        except InvalidOperation:
            self._salario = Decimal(0)

    else:
        self._salario = Decimal(0)
```

b. Na propriedade de escrita `data_de_admissao` faça:

```python
@data_de_admissao.setter
def data_de_admissao(self, data_de_admissao):
    if self.eh_data_valida(data_de_admissao):

        try:
            self._data_de_admissao = str_to_date(data_de_admissao)
        except ValueError:
            self._data_de_admissao = date.today()

    else:
        self._data_de_admissao = date.today()
```

Nossa funcionalidade agora está blindada contra erros, mas esse é o tratamento que queremos? Não queremos criar um funcionário com esses valores inconsistentes, queremos enviar uma mensagem para o usuário e informá-lo que não foi possível gravar os dados do funcionário.

3) Vamos criar e lançar nossa própria exceção:

a. Crie uma classe chamada `FuncionarioException`

```python

class FuncionarioException(Exception)
    
    def __init__(self, message, Errors):
        Exception.__init__(self, message)
        self.Errors = Errors

```

b. Em cada um das propriedades `salario` e `data_de_admissao` lance a exceção que acabamos de criar:

```python

@salario.setter
def salario(self, salario):

    sucesso = True

    if self.eh_salario_valido(salario):
        try:
            self._salario = Decimal(salario)
        except InvalidOperation:
            sucesso = False
    else:
        sucesso = False

    if not sucesso:
        raise FuncionarioException("Salário informado inválido!")

@data_de_admissao.setter
def data_de_admissao(self, data_de_admissao):

    sucesso = True

    if self.eh_data_valida(data_de_admissao):
        try:
            self._data_de_admissao = str_to_date(data_de_admissao)
        except ValueError:
            sucesso = False
    else:
        sucesso = False

    if not sucesso:
        raise FuncionarioException("Data de Admissão informada inválida!")

```

c. No momento de instanciar a classe `Funcionario` faça o tratamento:

```python
...

nome = raw_input("Informe o nome: ")
telefone = raw_input("Informe o telefone: ")
salario = raw_input("Informe o salário (Ex: 2000.40): ")
data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

try:

    funcionario = Funcionario(cpf, nome, telefone, salario, data_de_admissao)

except FuncionarioException, e:
    print "\n %s \n" % e.message
    continue

lista_de_funcionarios.adicionar(funcionario)

...
```

4) Agora vamos fazer o mesmo na funcionalidade de alteração:

```python
...

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

...

```

5) Outro ponto onde podemos utilizar nossa exceção é para verificar se já existe um CPF cadastrado e com isso extrair a lógica de verificação para o método `adicionar` da classe `ListaDeFuncionarios`, ficaria assim:

```python

...

def adicionar(self, funcionario):
    '''
        Adiciona um funcionário a lista
    '''
    if self.obter(funcionario.cpf):
        raise FuncionarioException("CPF %s, já cadastrado" % funcionario.cpf)

    self._values.append(funcionario)

...

```

E o código alterado da aplicação:

```python

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

```