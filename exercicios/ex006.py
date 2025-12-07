#Entrada
n = int(input('Digite um número: '))
#Processamento
d = n * 2
t = n * 3
r = n ** (1/2)
#Saída
print('O \033[4mdobro\033[m de {} vale \033[4m{}\033[m. \nO \033[4mtriplo\033[m de {} vale \033[4m{}\033[m. \nA \033[4mraiz quadrada\033[m de {} é igual a \033[4m{:.2f}\033[m. '.format(n,d,n,t,n,r), end=' ')
