#Entrada
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
#Processamento
s = n1 + n2
#Saída
print('\033[34m{}\033[m + \033[33m{}\033[m = \033[31m{}\033[m'.format(n1,n2,s))