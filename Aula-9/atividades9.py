#3: Verificando se uma string é vazia ou não


minha_string = input('digite algo, se quiser: ')

if not minha_string:
    print('string vazia')

else:
    print('string com algo dentro')

if input('quer ver oque tem dentro da string? ') == 'sim':
    print(minha_string)

else:
    print('então vaza')