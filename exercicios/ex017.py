# Hipotenusa: c² = a² + b²
import math

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))

#c = (a ** 2 + b ** 2) ** (1/2)
#c = math.hypot(a, b)
#print('A hipotenusa vai medir {:.2f}'.format(c))

c = math.pow(a,2) + math.pow(b, 2)
print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(c)))