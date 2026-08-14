import customtkinter as ctk
from tkinter import messagebox


# FUNÇÃO DO BOTÃO ENVIAR


def enviar():
    # Pega o conteúdo digitado em cada campo
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()
    endereco = entrada_endereco.get()
    celular = entrada_celular.get()
    cep = entrada_cep.get()
    cidade = entrada_cidade.get()
    curso = entrada_curso.get()

    # Mostra as informações no console
    print("\n========== CADASTRO DO CLIENTE ==========")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Celular: {celular}")
    print(f"CEP: {cep}")
    print(f"Cidade: {cidade}")
    print(f"Curso: {curso}")
    print("=========================================")

    # Mostra uma mensagem na tela
    messagebox.showinfo(
        "Cadastro",
        "Cliente cadastrado com sucesso!"
    )

# CONFIGURAÇÃO DA JANELA


janela = ctk.CTk()

janela.title("Sistema de Cadastro de Clientes")

janela.geometry("1700x750")

# janela.resizable(False, False)

# CONFIGURAÇÃO DO TEMA


ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")

# TÍTULO


titulo = ctk.CTkLabel(
    janela,
    text="SISTEMA DE CADASTRO DE CLIENTES",
    font=("Arial", 28, "bold")
)

titulo.pack(pady=30)

# FRAME DO FORMULÁRIO


formulario = ctk.CTkFrame(
    janela,
    width=800,
    height=500,
    corner_radius=15
)

formulario.pack(pady=10)

formulario.pack_propagate(False)

# NOME

label_nome = ctk.CTkLabel(
    formulario,
    text="Nome:",
    font=("Arial", 15)
)

label_nome.grid(
    row=0,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_nome = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="Digite seu nome"
)

entrada_nome.grid(
    row=0,
    column=1,
    padx=20,
    pady=12
)


# IDADE

label_idade = ctk.CTkLabel(
    formulario,
    text="Idade:",
    font=("Arial", 15)
)

label_idade.grid(
    row=1,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_idade = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="Digite sua idade"
)

entrada_idade.grid(
    row=1,
    column=1,
    padx=20,
    pady=12
)

# E-MAIL


label_email = ctk.CTkLabel(
    formulario,
    text="E-mail:",
    font=("Arial", 15)
)

label_email.grid(
    row=2,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_email = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="Digite seu e-mail"
)

entrada_email.grid(
    row=2,
    column=1,
    padx=20,
    pady=12
)


# ENDEREÇO


label_endereco = ctk.CTkLabel(
    formulario,
    text="Endereço:",
    font=("Arial", 15)
)

label_endereco.grid(
    row=3,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_endereco = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="Digite seu endereço"
)

entrada_endereco.grid(
    row=3,
    column=1,
    padx=20,
    pady=12
)


# CELULAR


label_celular = ctk.CTkLabel(
    formulario,
    text="Celular:",
    font=("Arial", 15)
)

label_celular.grid(
    row=4,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_celular = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="(00) 00000-0000"
)

entrada_celular.grid(
    row=4,
    column=1,
    padx=20,
    pady=12
)

# CEP


label_cep = ctk.CTkLabel(
    formulario,
    text="CEP:",
    font=("Arial", 15)
)

label_cep.grid(
    row=5,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_cep = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="00000-000"
)

entrada_cep.grid(
    row=5,
    column=1,
    padx=20,
    pady=12
)



# CIDADE


label_cidade = ctk.CTkLabel(
    formulario,
    text="Cidade:",
    font=("Arial", 15)
)

label_cidade.grid(
    row=6,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_cidade = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="Digite sua cidade"
)

entrada_cidade.grid(
    row=6,
    column=1,
    padx=20,
    pady=12
)



# CURSO


label_curso = ctk.CTkLabel(
    formulario,
    text="Curso:",
    font=("Arial", 15)
)

label_curso.grid(
    row=7,
    column=0,
    padx=20,
    pady=12,
    sticky="e"
)


entrada_curso = ctk.CTkEntry(
    formulario,
    width=500,
    height=40,
    placeholder_text="Digite o curso"
)

entrada_curso.grid(
    row=7,
    column=1,
    padx=20,
    pady=12
)


# BOTÃO ENVIAR


botao_enviar = ctk.CTkButton(
    janela,
    text="ENVIAR",
    font=("Arial", 16, "bold"),
    width=200,
    height=50,
    corner_radius=10,
    fg_color="#2E8B57",
    hover_color="#246B45",
    command=enviar
)

botao_enviar.pack(pady=25)



# INICIAR PROGRAMA


janela.mainloop()