'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q01():
    print('João Paulo')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q02():
    print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q03():
    print((5+8+12)/3)

#4. Faça um programa que leia e imprima um número inteiro.
def q04():
    numero = int(input('Digite um número inteiro: '))
    print(numero)

#5. Faça um programa que leia dois números reais e os imprima.
def q05():
    numero1 = float(input('Digite um número real: '))
    numero2 = float(input('Digite um outro número real: '))
    print(numero1)
    print(numero2)

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q06():
    numero = int(input('Digite um número inteiro: '))
    print(f'Sucessor: {numero+1}')
    print(f'Antecessor: {numero-1}')

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q07():
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    print(f'\n{nome}\n{telefone}\n{endereco}')

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q08():
    num1 = int(input('Núm1: '))
    num2 = int(input('Núm2: '))
    subtracao = num1 - num2
    print(f'{subtracao}')

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q09():
    numero = float(input('Número real: '))
    print(f'{numero/4}')

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('Núm1: '))
    num2 = float(input('Núm2: '))
    num3 = float(input('Núm3: '))
    print(f'{(num1+num2+num3)/3}')

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = float(input('Núm1: '))
    num2 = float(input('Núm2: '))
    print(f'{num1} + {num2} = {num1+num2}')
    print(f'{num1} - {num2} = {num1-num2}')
    print(f'{num1} * {num2} = {num1*num2}')
    print(f'{num1} / {num2} = {round((num1/num2),1)}')

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    numero = float(input('Número: '))
    print(f'{numero**2}')

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('Saldo da conta: R$ '))
    print(f'{saldo*1.02}')

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura / 2).
def q14():
    base = float(input('Base do triângulo: '))
    altura = float(input('Altura do triângulo: '))
    print(f'Perímetro: {base + altura}')
    print(f'Área: {base * altura / 2}')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    preco = float(input('Preço do produto: R$ '))
    desconto = float(input('Desconto (%): '))
    valor_desconto = preco * desconto / 100
    preco_final = preco - valor_desconto
    print(f'Valor do desconto: R$ {round(valor_desconto,2)}')
    print(f'Preço final do produto: R$ {round(preco_final,2)}')

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    salario = float(input('Salário: R$ '))
    reajuste = float(input('Reajuste (%): '))
    novo_salario = salario * (1 + (reajuste / 100))
    print(f'Novo salário: R$ {novo_salario:.2f}') #trunca até a segunda casa

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
    c = float(input('Graus Centígrados: '))
    f = (9 * c + 160) / 5
    print(f'Equivalente em Fahrenheit: {f}')

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    tempo = int(input('Tempo da viagem(minutos): '))
    velocidade = int(input('Velocidade média (km/h): '))
    distancia = tempo/60 * velocidade
    litros = distancia/12
    print(f'Distância percorrida: {distancia} km')
    print(f'Litros gastos: {litros}')

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    valor_prestacao = float(input('Valor da prestação: R$ '))
    taxa_juros = float(input('Taxa de juros diária (%): '))
    dias_atraso = int(input('Qtde de dias atrasado: '))
    multa = valor_prestacao * taxa_juros/100 * dias_atraso
    valor_final = valor_prestacao + multa
    print(f'Valor da multa: R$ {round(multa,2)}')
    print(f'Valor a pagar: R$ {round(valor_final,2)}')

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
    dolares = float(input('Qtde de dólares: US$ '))
    cotacao = float(input('Cotação do dólar: R$ '))
    print(f'Valor em reais: R$ {dolares * cotacao}')

# Escolha a questão a ser executada
q01()
