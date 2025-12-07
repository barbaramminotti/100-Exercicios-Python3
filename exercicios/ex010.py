real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/6.0376994 #Dolar em 2025
print('Com R${:.2f} você pode comprar \033[34mUS${:.2f}\033[m'.format(real, dolar))

#Yene-JP
yene = real*25.8799172
print('Com R${:.2f} você pode comprar \033[31m¥${:.2f}\033[m'.format(real, yene))
