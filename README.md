## Cap 8) Tópicos Avançados

1) Observe que nossas propriedades de escrita para `salario` e `data_de_admissao` estão praticamente idênticas. Exceto por alguns detalhes, a estrutura do código é a mesma: executa uma validação, trata erros na hora de converter, e lança uma exceção caso alguma coisa dê errado. Podemos melhorar isso extraindo esse código repetido para um lugar específico e, para isso, vamos utilizar um _decorator_. Por construção da funcionalidade, nosso decorator precisa receber o método que será usado para validação e a mensagem que será lançada em caso de erro (observe que poderíamos nos preocupar, também, em passar o tipo de exceção que será tratada e, assim, aumentar a granularidade do nosso tratamento de erros, mas pra simplificar, iremos capturar qualquer erro que ocorra no momento da conversão).

1) Extraia o código do método `salario(self, salario)` para um função decoradora chamada `valido`, que deve ser criada antes da classe `Funcionario`:

```python

def valido(eh_valido, msg_de_erro):
    def onDecorator(funcao_verificada):
        def onCall(self, valor_a_validar):
            sucesso = True
            if eh_valido(self, valor_a_validar):
                try:
                    return funcao_verificada(self, valor_a_validar)
                except:
                    sucesso = False
            else:
                sucesso = False

            if not sucesso:
                raise FuncionarioException(msg_de_erro)
        return onCall
    return onDecorator

```

Repare que essa função recebe dois paramêtros: o primeiro é a função que efetua a validação e o segundo é a mensagem de erro que queremos exibir ao usuário. Os parâmetros `funcao_verificada` e `valor_a_validar` referem-se, respectivamente, a função que está sendo decorada e ao parâmetro passado para a função que está sendo decorada.

2) Agora tudo o que precisamos fazer é utilizar o nosso decorator:

```python
...

@salario.setter
@valido(eh_salario_valido, "Salário informado inválido!")
def salario(self, salario):
    self._salario = Decimal(salario)

...

@data_de_admissao.setter
@valido(eh_data_valida, "Data de Admissão informada inválida!")
def data_de_admissao(self, data_de_admissao):
    self._data_de_admissao = str_to_date(data_de_admissao)

...
```
__Antes de testar atente ao seguinte:__ Para usarmos o nosso decorator, precisamos que os métodos `eh_salario_valido` e `eh_data_valida`, validadores que serão passados como argumentos ao decorator, estejam declarados antes do seu uso, por isso vamos mover esses métodos para antes das chamadas ao decorator, ok?

No final nossa classe `Funcionario` ficará assim: 

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
        
    @property
    def salario(self):
        return self._salario

    @salario.setter
    @valido(eh_salario_valido, "Salário informado inválido!")
    def salario(self, salario):
        self._salario = Decimal(salario)

    @property
    def data_de_admissao(self):
        return self._data_de_admissao

    @data_de_admissao.setter
    @valido(eh_data_valida, "Data de Admissão informada inválida!")
    def data_de_admissao(self, data_de_admissao):
        self._data_de_admissao = str_to_date(data_de_admissao)

    @property
    def salario_anual(self):
        return self.salario * 12

    def __str__(self):
        return "%s [CPF: %s | Tel: %s | Salário anual: %.2f | Data de Admissão: %s] " % \
                    (self.nome, 
                     self.cpf, 
                     self.telefone, 
                     self.salario_anual, 
                     self._data_de_admissao.strftime('%d/%m/%Y'))


```

TODO: É possível encaixar na aplicação outros tópicos como função lambda, generators, yield, etc. Mas é preciso saber o quão grande seria interessante manter esse cápitulo.