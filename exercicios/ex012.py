#Entrada
preco = float(input('Qual é o preço do produto? R$'))
#Processamento
final = preco - (preco*0.05)
#Saída
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, final))