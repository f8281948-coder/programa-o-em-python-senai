import módulo
def sistema ():
    lista_notas = []

    n = input('deseja adicionar uma nota? ')
    while n == 'sim':
        notas = int(input('coloque a sua nota: '))
        

        lista_notas.append(notas)
        print(lista_notas)
        n = input('deseja adicionar outra nota? ')
        

    moda, media, desvio , mediana, variancia, menor, maior=módulo.estatistica(lista_notas)
    print('moda -',moda,'media', media, desvio , mediana, variancia, menor, maior)
sistema()        