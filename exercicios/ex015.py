#Entrada
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
#Processamento
total = (60 * dias) + (km * 0.15)
#Saída
print('O total a pagar é de R${:.2f}'.format(total))