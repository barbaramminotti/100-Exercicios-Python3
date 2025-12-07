import math

a = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sen))
cos = math.cos(math.radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos))
tan = math.tan(math.radians(a))
print('O ângulo de {}  tem a TANGENTE de {:.2f}'.format(a, tan))