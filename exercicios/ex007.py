#Entrada
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
#Processamento
media = (n1 + n2) / 2
#Saída
print('A média entre {:.1f} e {:.1f} é igual a \033[4m{:.1f}\033[m'.format(n1,n2,media))
