#Entrada
salario = float(input('Qual é o salário do funcionário? R$'))
#Processamento
novo = salario + (salario*0.15)
#Saída
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario,novo))