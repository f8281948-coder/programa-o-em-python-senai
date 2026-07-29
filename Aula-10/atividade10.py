# ## ***ATIVIDADE 1***

# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
# n = 1
# while n <= 1000:
#      print("Número:", n)
#      n += 1



# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.


lista = []
n = 1
while n <= 10:
     nome = input('coloque um nome: ')
     lista.append(nome)
print(lista)