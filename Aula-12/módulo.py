import statistics

def estatistica(lista_notas):
    moda  =  statistics.mode(lista_notas)
    media = statistics.mean(lista_notas)
    desvio =  statistics.stdev(lista_notas)
    mediana =  statistics.median(lista_notas)
    variancia =  statistics.variance(lista_notas)
    menor =  min(lista_notas)
    maior =  max(lista_notas)


    return moda, media, desvio , mediana, variancia, menor, maior