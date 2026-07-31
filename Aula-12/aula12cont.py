## Exercícios com funções:

# variáveis locais, globais e parâmetros

# ***1*** 

# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

# def comparação ():
#   n1 = int(input('coloque um número : '))
#   n2 = int(input('coloque um outro número: '))
#   print(n1 == n2)

# comparação()



# ***2***

# ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***
# def multi ():
#     n1 = int(input('coloque um número: '))
#     n2 = int(input('coloque um número: '))
#     n3 = int(input('coloque um número: '))

#     lista = [n1 , n2 , n3]
#     multiplicação = n1 * n2 * n3

#     print(multiplicação)

# multi()

# ***3***

# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

# def elev ():
#    n1 =  int(input('insira um número: '))
#    n2 =  int(input('insira um número para elevar o número anterior: '))
#    print(n1 ** n2)
# elev()   


# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

# def mensagem ():
#    idade = int(input('digite a sua idade: '))
#    if idade == 18:
#       print('parabéns!! Você já pode ser preso!!')
#    else:
#       print('isso não foi programado, volte e digite que tem 18 anos')
 
# mensagem()

# ***5***

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***
# def start ():
#     starter = bool(input('irei descobrir a sua idade com apenas uma pergunta! digite qualquer coisa para tentar: '))
#     if starter == True:
#       input('digite a sua idade: ')
#       print('acabei de descobrir a sua idade!')
#     else:
#       print('vá para o próximo código')

# start()

# ***6***

# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

# def copa ():
#     l = input('o brasil ganhou a copa de 1999? ')
#     if l == 'sim':
#         print('a resposta é sim, o Brasil ganhou a copa de 1999')
#     else:
#         print('infelizmente, não')

# copa()

# ***7*** 

# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  

# ***1 - Função -  cumprimentar o cliente***

# ***2 - Função - restaurante***

# ***3 - Sugestão utilize listas  e loops*** 

def restaurante ():
    
    pedidos = []
    
    print('olá! seja bem vindo!')
    
    resposta = input('deseja acessar o nosso restaurante? digite sim ou não: ')
    while resposta == 'sim':
        jun = {
        menu = ['' 'salada' , 'macarronada' , 'sanduíche' , 'sorvete']
      
      }
        print(jun)
        
        escolha = input('escolha o nome ')
        
        print('você escolheu:' , escolha)
        
      
        
                
        pedidos.append(escolha)

        print('seus pedidos: ' , pedidos )
        resposta = input('deseja continuar? ')
                                      
    else:
         print('obrigado! volte sempre!')  
         print('seus pedidos: ' , pedidos ) 
  
restaurante()
                 