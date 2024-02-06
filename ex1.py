#Exemplos de comandos básicos em Python
print('Funciona!!!')
nota1 = 7
print(nota1)
print(type(nota1))
print(f'nota1 tem valor {nota1} e é do tipo {type(nota1)}')
nota2 = 7.3
print(f'nota2 tem valor {nota2} e é do tipo {type(nota2)}')
aluno = 'Maria'
print(f'aluno tem valor {aluno} e é do tipo {type(aluno)}')
media = (nota1 + nota2) / 2
print(f'{aluno}\t{nota1}\t{nota2}\t{media}') #\t tabula e \n nova linha
#Operadores aritméticos básicos
soma = nota1 + nota2
divisao = nota1 / nota2
multiplicacao = nota1 * nota2
subtracao = nota1 - nota2
resto_divisao = nota1 % nota2

#Exemplo de interação do usuário
nome = input('Digite seu nome: ')
print(f'Olá {nome}. Seja bem vindo(a)!')

#Leia dois valores numéricos e apresente o resto da divisão
#input sempre retorna um texto (string), se precisar que seja
#numérico, faz-se necessário a conversão
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
resto = v1 % v2
print(f'{v1} % {v2} = {resto}')

#Leia o valor de um produto e o desconto em reais e 
#apresente o valor final a pagar
preco = float(input('Preço R$: '))
desconto = float(input('Desconto R$: '))
valor_final = preco - desconto
print(f'Valor a pagar: R$ {valor_final}')

#Leia o valor de um produto em Reais e o desconto em
#percentual e apresente o valor final a pagar
preco = float(input('Preço R$: '))
desconto = float(input('Desconto %: '))
valor_final = preco - (preco * desconto/100)
print(f'Valor a pagar: R$ {valor_final}')
