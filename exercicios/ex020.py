import random #Módulo random

p1 = str(input('Primeiro Aluno: '))
p2 = str(input('Segundo Aluno: '))
p3 = str(input('Terceiro Aluno: '))
p4 = str(input('Quarto Aluno: '))

alunos = [p1, p2, p3, p4] #lista = [item1, item2, item3, ..., itemN]
random.shuffle(alunos) #random.shuffle() embaralha os elementos na lista
print('A ordem de apresentação será \n{}'.format(alunos))