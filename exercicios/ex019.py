import random #Módulo random

p1 = str(input('Primeiro Aluno: '))
p2 = str(input('Segundo Aluno: '))
p3 = str(input('Terceiro Aluno: '))
p4 = str(input('Quarto Aluno: '))

alunos = [p1, p2, p3, p4] #lista = [item1, item2, item3, ..., itemN]
escolhido = random.choice(alunos) # random.choice() escolhe aleatoriamente um dos elementos da lista

print('O aluno escolhido foi {}'.format(escolhido))