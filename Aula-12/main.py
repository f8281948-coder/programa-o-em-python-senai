

# 4  tipos de dados primitivos


# str int float bool


# estruturas de dados 
# guardando dados na memoria ram(mutavel do pc )


# v =  12
# lis = [1,2,3]
# tupla = (12,3)
# conj =  {1,2,3}
# dicio = {'a':10, 'a':5}




# estruturas de fluxo de controle 
# repetições e toma decisões 




# if else elif 
# for 
# while 
# match
# try
# del 


# ------------------------------


# funções


# 3
# funções imbutidas na linguagem  -  print () input() len() ...
# bibliotecas externas pandas numpy tensorflow 
# da sua criação


# definition -  incapsulamento e  organização
# def nome(): 
#     print('teste')
    

# nome()



def cadastro(quantidade, nomes, idades):
    for x in range(quantidade):
        nome = input('nome: ')
        idade  = input('idade: ')
        nomes.append(nome)
        idades.append(idade)
    return nomes, idades,
    


def reservas():
    lista_quartos = ['', "Simples", "Duplo" , "Luxo"]
    valores  =  [0,100.0,150.0,250.0]
    print(lista_quartos)
    print(valores)
    escolha  =  int(input('Escolha quarto >>>'))
    quantidade_dias = int(input('Quantidade de dias:  '))
    print(escolha)
    c =  quantidade_dias * valores[escolha]
    print('R$', c)
    l =  ['','pix','cc','cd']
    print(l)
    formapag =  int(input('digite a forma de pagamento: '))
   
    print(l[formapag]) 
    print('Obrigada volte sempre!')
    


def hotel_main():    

    nomes = []
    idades = []
    q =  int(input('Digite a quantidade de pessoas: '))
    dados_nomes, dados_idade = cadastro(q,nomes, idades)
    quantidade_pessoas = len(dados_nomes)
    print('quantidade de pessoas:', quantidade_pessoas)
    for n in range(quantidade_pessoas):
        print(f'Reserva do cliente {dados_nomes[n]}')
        reservas()


hotel_main()    

    



#banco


def saque(saldo, sq):
    return saldo -  sq

def deposito(saldo , dp):
    return saldo +  dp

def extrato(saldo):
    return saldo

def banco():

    while True:
        print('acesse seu banco ...')
        ac = input('Deseja acessar o banco? ')
        while ac  == 'sim':
              senha =  input('SENHA >>>')
              saldo =  [5000]
              for i in range(3):
                  if senha == '123':
                      print('conta XXX')
                      
                      print('saldo', saldo)
                      op = input('Escolha  a operação: ')
                      if op == 'saque':
                          valor_saque =  float(input('Valor saque>>>'))
                          s  =  sum(saldo)
                          if valor_saque > s:
                              print('Sem saldo ...')
                          else:
                              
                              s =  sum(saldo)
                              print('Saque: R$', valor_saque)
                              print('Em conta', saque(s, valor_saque))
                              saldo.append(-valor_saque)
                              ac = input('Deseja acessar o banco? ')
                      elif op == 'deposito':
                          valor_deposito =  float(input('Valor deposito>>>'))
                          if valor_deposito:
                              s =  sum(saldo)
                              print('deposito: R$', valor_deposito)
                              print('Em conta', deposito(s, valor_deposito))
                              saldo.append(valor_deposito)
                              ac = input('Deseja continuar? ')
                      elif op == 'extrato':
                           print('extrato', saldo)                                            

banco()                                                        
