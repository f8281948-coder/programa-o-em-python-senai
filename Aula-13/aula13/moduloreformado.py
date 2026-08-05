import random

def at1 ():
    1 == random.random
    return 1

def at2():
    n1 = random.randint(1 , 5)
    n2 = random.randint(1 , 5)
    n3 = random.randint(1 , 5)
    return n1 , n2 , n3 

def at3():
    for a3 in range (9 , 31):
        a3 = random.randint(10 , 30)   
        return a3
    
def at4():
    for a4 in range (10 , 0 , -1):
        print(a4)
            


           
def at5():
    ip = int(input('insira um número inteiro positivo: '))
    soma = 0

    for i in range(2, ip + 1):

       if i % 2 == 0:
        soma += i

        print("A soma dos números pares é: ", soma)



def at6():
   n = int(input('insira um número inteiro para ver a sua tabuada de 1 a 10: '))

   for t6 in range (1 , 11):
       print(n, 'x', t6 ,'==', n * t6) 


def at7():
    for a7 in range(99 , 0, - 2):
       print(a7)