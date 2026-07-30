try:
   int(input('insira um número inteiro: '))

except ValueError as erro:
 print(erro)

except TypeError as problem:
 print(problem) 