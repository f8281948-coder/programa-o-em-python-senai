import sqlite3

con = sqlite3.connect('cadastro.db')
cursor = con.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,            
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        idade INTEGER,
        endereco TEXT NOT NULL,
        trabalho TEXT NOT NULL,
        graduacao TEXT NO NULL
                      
   )
''')


# crud




def criar_funcionário(nome,idade, email , trabalho, graduacao , endereco):
    cursor.execute('INSERT INTO clientes (nome, email) values(?,?)', (nome, idade , email , trabalho , graduacao , endereco))
    con.commit()
 

def listar_funcionários():
    cursor.execute('SELECT (nome, trabalho , graduacao) FROM clientes')
    return cursor.fetchall()


def atualizar_mail(id_cliente, novo_email):
    cursor.execute('UPDATE clientes SET email=? WHERE id = ?', (novo_email, id_cliente))
    con.commit()


def deletar_cliente(id_cliente):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
    con.commit()


def sistema():
    
    print('cadastre-se')
    nome =  input('Nome: ')
    email = input('e - mail: ')
    criar_funcionário(nome, email)
    print('Inserindo ... ')
    print(listar_funcionários())


sistema()
# def sistema():


#     while True: 


#         op = input('O que deseja fazer 1 - add cliente | 2 -  atualizar | 3 - deletar  : ')


#         if  op == '1':



#             nome =  input('Nome: ')
#             email = input('e - mail: ')
#             criar_funcionário(nome, email)
#             criar_funcionário('Lucas', 'Lucas@gmail.com')
#             print('Inserindo ... ')
#             print(listar_funcionários())


#         elif op == '2':
#             print(listar_funcionários()) 
#             id  =  int(input('Id: '))
#             n_email = input('e - mail: ')
#             # atualizar
#             print('Atualizando ...')
#             atualizar_mail(id, n_email)
#             print(listar_funcionários())



#         elif op == '3':   
#         # delete
            
#             print(listar_funcionários())
#             id  =  int(input('Id: '))
#             print('deletando ... ')
#             deletar_cliente(id)
#             print(listar_funcionários())


#             con.close()


# sistema()            