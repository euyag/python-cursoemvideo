print('===== DESAFIO 022 =====')
nome = str(input('Digite o seu nome: '))
print('o seu nome com todas as letras maiusculas:', nome.upper())
print('o seu nome com todas as letras minusculas:', nome.lower())
print('quantidade de letras:', len(nome) - nome.count(' '))
divisao = nome.split()
print('quantidade de letras do primeiro nome:', len(divisao[0]))