## Cap 7) Orientação a Objetos II

1) Vamos criar uma especialização para cadastrar funcionários que exercem a função de gerente. Iremos criar esta especialização pois os gerentes possuem uma gratificação que irá incidir sobre o salário anual e o sistema deve exibir este valor atualizado.

```python
class Gerente(Funcionario):

    @property
    def salario_anual(self):
        return (self.salario * Decimal(1.2)) * 12

```

O código da aplicação atualizado fica:

```python
...
cpf = raw_input("Informe o CPF: ")
nome = raw_input("Informe o nome: ")
telefone = raw_input("Informe o telefone: ")
salario = raw_input("Informe o salário (Ex: 2000.40): ")
data_de_admissao = raw_input("Informe a data de admissão (Ex: 22/01/2014): ")

eh_gerente = raw_input("O funcionário é um gerente? (S/N) ")

if eh_gerente.upper() in ("S", "N"):
    eh_gerente = eh_gerente.upper() == "S"
else:
    print "\n Opção inválida. Escolha S ou N \n"
    continue

try:

    if not eh_gerente:
        funcionario = Funcionario(cpf, nome, telefone, salario, data_de_admissao)
    else:
        funcionario = Gerente(cpf, nome, telefone, salario, data_de_admissao)
    
    lista_de_funcionarios.adicionar(funcionario)

except FuncionarioException, e:
    print "\n %s \n" % e.message
    continue
...

```

(Não esqueça o import da classe Gerente)

2) Vamos permitir que o usuário informe o valor da gratificação.

```python
class Gerente(Funcionario):

    def __init__(self, cpf, nome, telefone, salario, data_de_admissao, gratificacao):
        Funcionario.__init__(self, cpf, nome, telefone, salario, data_de_admissao)
        self._gratificacao = Decimal(gratificacao)

    @property
    def salario_anual(self):
        return (self.salario * self._gratificacao) * 12
```

E na aplicação: 

```python
...
if not eh_gerente:
    funcionario = Funcionario(cpf, nome, telefone, salario, data_de_admissao)
else:
    gratificacao = raw_input("Informe a gratificação: ")
    funcionario = Gerente(cpf, nome, telefone, salario, data_de_admissao, gratificacao)
...
```

3) Atualize o método `__str__` na classe `Funcionario` para exibir o salário anual:

```python
...
def __str__(self):
    return "%s [CPF: %s | Tel: %s | Salário anual: %.2f | Data de Admissão: %s] " % \
                (self.nome, 
                 self.cpf, 
                 self.telefone, 
                 self.salario_anual, 
                 self._data_de_admissao.strftime('%d/%m/%Y'))

...

```

4) Agora implemente o método `__str__` na classe `Gerente` para exibir, também, o total em gratificação:

```python
...
def __str__(self):
    return "%s [CPF: %s | Tel: %s | Salário anual: %.2f | Gratificação total: %.2f | Data de Admissão: %s] " % \
                (self.nome, 
                 self.cpf, 
                 self.telefone, 
                 self.salario_anual, 
                 self._gratificacao * 12,
                 self._data_de_admissao.strftime('%d/%m/%Y'))

...

```
Além da entrada de dados, precisamos mexer em nosso programa em algum outro lugar? Nossa lista de funcionários precisou ser alterada para trabalhar com gerentes? Onde estão os contratos?