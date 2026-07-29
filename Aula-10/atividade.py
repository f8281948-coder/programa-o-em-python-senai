# ## ***ATIVIDADE 2***

# Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***

#  **Sistema de notas de alunos**

# - ***Visão do professor***

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

# ***IMPORTANTE:***

# - Ao finalizar o código, insira na borda do script, no última linha:

# input(’Digite enter para sair’)


notas = []
chanches = 3
for n in range(chanches):
    senha = input('senha:')
    if senha == '1234':
        print('seja bem vindo')
        p = input('deseja add notas?')
        while p == 'sim':
            n1 = float(input('nota'))
            notas.append(n1)
            p = input('deseja continuar?')
        else:
            s= sum(notas)/len(notas)
            print('média', s)

            f = input('Digite enter para sair: ')

        if f == 'enter':
          print('volte sempre!')

    else:
       print('senha incorreta')
else:

    block = print('conta bloqueada') 

   

  
