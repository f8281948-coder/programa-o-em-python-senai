

# atividade a partir desse código

# #ATIVIDADE 2
# Crie um formulário em Tkinter
# Problema: Sistema de Cadastro de Clientes
# Você é um desenvolvedor de software e foi contratado por uma empresa de serviços para criar um sistema de cadastro de clientes. O sistema deve permitir que os clientes forneçam suas informações pessoais, como nome, idade, e-mail, endereço, celular...
# Atividade:
# Crie um formulário em Tkinter que contenha os seguintes campos:
# Nome
# Idade
# E-mail
# Endereço
# Celular
# Cep
# Cidade
# Cursos
# O formulário deve ter um botão de "Enviar" que, quando clicado, imprima as informações do cliente na console.
# Tamanho da tela = '1700x750’ 

import tkinter as tk





janela  =  tk.Tk()
janela.geometry('1700x750')
janela.title('FORMULÁRIO')



# TITULO DO FORM


titulo  =  tk.Label(janela, text='FORMULARIO DE CADASTRO')
titulo.pack()


# TÍTULO  DO NOME |  INPUT DO NOME


nome_texto = tk.Label(janela, text  =  'Nome')
nome_texto.pack()


nome_input =  tk.Entry(janela)
nome_input.pack()


# -------------------

idade_texto = tk.Label(janela, text  =  'idade')
idade_texto.pack()
idade_input =  tk.Entry(janela)
idade_input.pack()

#------------------

email_texto = tk.Label(janela, text  =  'email')
email_texto.pack()
email_input =  tk.Entry(janela)
email_input.pack()

#----------------------

endereço_texto = tk.Label(janela, text  =  'endereço')
endereço_texto.pack()
endereço_input =  tk.Entry(janela)
endereço_input.pack()

#---------------------

cel_texto = tk.Label(janela, text  =  'celular')
cel_texto.pack()
cel_input =  tk.Entry(janela)
cel_input.pack()


#----------------------

cep_texto = tk.Label(janela, text  =  'cep')
cep_texto.pack()
cep_input =  tk.Entry(janela)
cep_input.pack()

#-------------------------

cidade_texto = tk.Label(janela, text  =  'cidade')
cidade_texto.pack()
cidade_input =  tk.Entry(janela)
cidade_input.pack()

#---------------------------

cursos_texto = tk.Label(janela, text  =  'cursos')
cursos_texto.pack()
cursos_input =  tk.Entry(janela)
cursos_input.pack()

#-----------------------------

def enviar():
    nome = nome_input.get()
    idade = idade_input.get()
    email = email_input.get()
    endereco = endereço_input.get()
    celular = cel_input.get()
    cep = cep_input.get()
    cidade = cidade_input.get()
    cursos = cursos_input.get()

    # Cria uma nova janela
    resultado = tk.Toplevel(janela)
    resultado.geometry('500x500')
    resultado.title('Dados do Cliente')

    tk.Label(resultado, text='DADOS DO CLIENTE',
             font=('Arial', 18, 'bold')).pack(pady=20)

    tk.Label(resultado, text=f'Nome: {nome}').pack(pady=5)
    tk.Label(resultado, text=f'Idade: {idade}').pack(pady=5)
    tk.Label(resultado, text=f'E-mail: {email}').pack(pady=5)
    tk.Label(resultado, text=f'Endereço: {endereco}').pack(pady=5)
    tk.Label(resultado, text=f'Celular: {celular}').pack(pady=5)
    tk.Label(resultado, text=f'CEP: {cep}').pack(pady=5)
    tk.Label(resultado, text=f'Cidade: {cidade}').pack(pady=5)
    tk.Label(resultado, text=f'Cursos: {cursos}').pack(pady=5)

btn = tk.Button(janela, text='Enviar', command=enviar)
btn.pack()



janela.mainloop()



# subir para o github 