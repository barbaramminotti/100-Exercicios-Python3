#import random
from random import randint
from time import sleep
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*18)
computador = randint(0, 5) #valor randômico em uma margem de inteiros definidos
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
