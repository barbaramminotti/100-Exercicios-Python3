name = str(input('Digite seu nome completo: ')).strip()
#nome = name.strip()

unidades = name.split() #name.split() separa cada palavra em conjuntos para uma lista
inteiro = ''.join(unidades) #''.join(unidades) junta palavras

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúsculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(inteiro))) #Espaços entre as palavras não contam
#print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(unidades[0], len(unidades[0])))
#print('Seu primeiro nome tem {} letras'.format(name.find(' ')))