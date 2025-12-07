#Entrada: medida em metros
#Processamento: dividir 10 se for uma medida maior e multiplicar 10 se for uma medida menor
#Saida: mostrar todas as medidas km hm dam dm cm mm

m = float(input('Uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de \033[36m{}m\033[m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m,km,hm,dam,dm,cm,mm))
