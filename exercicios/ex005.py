#Entrada
n = int(input('Digite um número: '))
#Processamento
ant = n - 1
suc = n + 1
#Saída
#print('Analisando o valor {}, seu antecessor é {} e o sucessor é {} '.format(n,(n-1),(n+1)))
print('Analisando o valor \033[31m{}\033[m, seu antecessor é \033[31m{}\033[m e o sucessor é \033[31m{}\033[m '.format(n,ant,suc))