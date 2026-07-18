nota_1 = 7
nota_2 = 7
nota_3 = 0
print('nota final')

media = (nota_1 + nota_2 + nota_3)/3
print(media)


aprovado = media >= 7
recuperacao = media >=5 and media < 7
reprovado = media < 5

print('situação do alno')
print('aprovado')
print(aprovado)
print('recuperação')
print(recuperacao)
print('reprovado')
print(reprovado)

resultado = media

if media >= 7:
    print ('aprovado')

if media < 7 >= 5:
    print ('recuperação')

if media <5:
    print ('reprovado')