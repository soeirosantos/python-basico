## Cap 2) Números, Datas e Conversão de Tipos

1) Vamos iniciar convertendo o salário informado pelo usuário em um número de ponto flutuante para que possamos efetuar operações em cima dele. Após a validação, faça:

```python

...

salario = raw_input("Informe o salário (Ex: 2000.40): ")

salario_sem_ponto = salario.replace(".","")

if not salario_sem_ponto.isdigit():
    print "\nSalário informado inválido!\n"
    continue

salario = float(salario)
...

```

2) Exiba a saída do salário anual do funcionário cadastrado logo após a mensagem que já estamos exibindo:

```python
...
print "\nFuncionário %s, CPF %s, cadastrado com sucesso." % (nome.upper(), cpf)

salario_anual = salario * 12

print "Salário anual: R$ %.2f\n" % salario_anual

...

```

3) Vimos que utilizar `float` para trabalhar com valores monetários, ou que necessitam de precisão de uma maneira geral, não é uma boa escolha, então vamos melhorar nosso código utilizando o tipo Decimal:

a. Comece fazendo o import no topo do arquivo: `from decimal import Decimal`

b. Agora vamos reescrever a linha que converte o salário do tipo String em um tipo numérico, substituindo o float por Decimal:

```python
...
if not salario_sem_ponto.isdigit():
    print "\nSalário informado inválido!\n"
    continue

salario = Decimal(salario)

...
```

Observe que nada mais muda em nosso código.

4) Agora vamos criar um objeto que nos permita trabalhar com datas a partir da data informada:

a. Inicie com o import no topo do arquivo `from datetime import date`

b. Agora crie um objeto do tipo date:

```python

if not (len(data_de_admissao) == 10      and \
        data_de_admissao[0:2].isdigit()  and \
        data_de_admissao[3:5].isdigit()  and \
        data_de_admissao[6:10].isdigit() and \
        "/" in (data_de_admissao[2], data_de_admissao[3])):

    print "\nData de Admissão informada inválida!\n"
    continue

dia = int(data_de_admissao[0:2])
mes = int(data_de_admissao[3:5])
ano = int(data_de_admissao[6:10])

data_de_admissao = date(ano, mes, dia)

```

5) Agora vamos formatar a exibição de uma data a partir da data de criação do funcionário. Para isso obtenha a data corrente e inclua na mensagem de cadastro efetuado.


```python
...

dia, mes, ano = data_de_admissao.split("/")

data_de_admissao = date(int(ano), int(mes), int(dia))

hoje = date.today()

print "\nFuncionário %s, CPF %s, cadastrado com sucesso em %s" % (nome.upper(), cpf, hoje.strftime('%d/%m/%Y'))

...

```
