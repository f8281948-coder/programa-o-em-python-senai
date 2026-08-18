# 1. SITUAÇÃO PROBLEMA: CADASTRO DE CLIENTES EM UM COMÉRCIO DE

# VAREJO

# A EMPRESA "XYZ COMÉRCIO" TEM DIFICULDADES EM CONTROLAR O

# CADASTRO DE SEUS CLIENTES. ATUALMENTE, O ARQUIVO COM OS DADOS

# DOS CLIENTES ESTÁ DESORGANIZADO, E A EQUIPE DE VENDAS TEM

# ENCONTRADO DIFICULDADES EM ENCONTRAR INFORMAÇÕES RÁPIDO. A

# EMPRESA PRECISA DE UM SISTEMA QUE PERMITA O CADASTRO DE NOVOS

# CLIENTES, A CONSULTA DE CLIENTES JÁ CADASTRADOS E A EDIÇÃO OU

# EXCLUSÃO DE DADOS.

# Solução proposta: Criar um sistema que permita o cadastro de novos clientes

# com informações como nome, e-mail, telefone e endereço. Além disso, o

# sistema permitirá a consulta, edição e exclusão dos dados dos clientes

# através de uma interface gráfica simples.


import customtkinter as ctk
from tkinter import messagebox
import sqlite3


# ============================================================
# BANCO DE DADOS
# ============================================================

def criar_banco():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            endereco TEXT NOT NULL,
            celular TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# ============================================================
# CADASTRAR CLIENTE
# ============================================================

def enviar():

    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    endereco = entrada_endereco.get().strip()
    celular = entrada_celular.get().strip()

    # Verifica se algum campo está vazio
    if nome == "" or email == "" or endereco == "" or celular == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )
        return

    # Conecta ao banco
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    # Insere o cliente
    cursor.execute("""
        INSERT INTO clientes (nome, email, endereco, celular)
        VALUES (?, ?, ?, ?)
    """, (nome, email, endereco, celular))

    conexao.commit()
    conexao.close()

    # Mensagem de sucesso
    messagebox.showinfo(
        "Cadastro",
        "Cliente cadastrado com sucesso!"
    )

    # Limpa os campos
    entrada_nome.delete(0, "end")
    entrada_email.delete(0, "end")
    entrada_endereco.delete(0, "end")
    entrada_celular.delete(0, "end")


# ============================================================
# EXCLUIR CLIENTE
# ============================================================

def excluir_cliente(id_cliente):

    resposta = messagebox.askyesno(
        "Excluir cliente",
        "Tem certeza que deseja excluir este cliente?"
    )

    if resposta:

        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM clientes WHERE id = ?",
            (id_cliente,)
        )

        conexao.commit()
        conexao.close()

        messagebox.showinfo(
            "Exclusão",
            "Cliente excluído com sucesso!"
        )

        # Atualiza a janela
        visualizar_clientes()


# ============================================================
# EDITAR CLIENTE
# ============================================================

def editar_cliente(cliente):

    id_cliente = cliente[0]
    nome_atual = cliente[1]
    email_atual = cliente[2]
    endereco_atual = cliente[3]
    celular_atual = cliente[4]

    janela_editar = ctk.CTkToplevel(janela)

    janela_editar.title("Editar Cliente")
    janela_editar.geometry("600x600")

    janela_editar.grab_set()

    titulo_editar = ctk.CTkLabel(
        janela_editar,
        text="EDITAR CLIENTE",
        font=("Arial", 25, "bold")
    )

    titulo_editar.pack(pady=25)

    # ---------------- NOME ----------------

    label_nome = ctk.CTkLabel(
        janela_editar,
        text="Nome:",
        font=("Arial", 15)
    )

    label_nome.pack(pady=(10, 5))

    entrada_nome_editar = ctk.CTkEntry(
        janela_editar,
        width=450,
        height=40
    )

    entrada_nome_editar.pack()

    entrada_nome_editar.insert(0, nome_atual)

    # ---------------- EMAIL ----------------

    label_email = ctk.CTkLabel(
        janela_editar,
        text="E-mail:",
        font=("Arial", 15)
    )

    label_email.pack(pady=(15, 5))

    entrada_email_editar = ctk.CTkEntry(
        janela_editar,
        width=450,
        height=40
    )

    entrada_email_editar.pack()

    entrada_email_editar.insert(0, email_atual)

    # ---------------- ENDEREÇO ----------------

    label_endereco = ctk.CTkLabel(
        janela_editar,
        text="Endereço:",
        font=("Arial", 15)
    )

    label_endereco.pack(pady=(15, 5))

    entrada_endereco_editar = ctk.CTkEntry(
        janela_editar,
        width=450,
        height=40
    )

    entrada_endereco_editar.pack()

    entrada_endereco_editar.insert(0, endereco_atual)

    # ---------------- CELULAR ----------------

    label_celular = ctk.CTkLabel(
        janela_editar,
        text="Celular:",
        font=("Arial", 15)
    )

    label_celular.pack(pady=(15, 5))

    entrada_celular_editar = ctk.CTkEntry(
        janela_editar,
        width=450,
        height=40
    )

    entrada_celular_editar.pack()

    entrada_celular_editar.insert(0, celular_atual)

    # ========================================================
    # SALVAR ALTERAÇÕES
    # ========================================================

    def salvar_edicao():

        novo_nome = entrada_nome_editar.get().strip()
        novo_email = entrada_email_editar.get().strip()
        novo_endereco = entrada_endereco_editar.get().strip()
        novo_celular = entrada_celular_editar.get().strip()

        if (
            novo_nome == ""
            or novo_email == ""
            or novo_endereco == ""
            or novo_celular == ""
        ):
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos!"
            )
            return

        conexao = sqlite3.connect("clientes.db")
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE clientes
            SET nome = ?,
                email = ?,
                endereco = ?,
                celular = ?
            WHERE id = ?
        """, (
            novo_nome,
            novo_email,
            novo_endereco,
            novo_celular,
            id_cliente
        ))

        conexao.commit()
        conexao.close()

        messagebox.showinfo(
            "Alteração",
            "Cliente atualizado com sucesso!"
        )

        janela_editar.destroy()

        visualizar_clientes()

    # ---------------- BOTÃO SALVAR ----------------

    botao_salvar = ctk.CTkButton(
        janela_editar,
        text="SALVAR ALTERAÇÕES",
        font=("Arial", 15, "bold"),
        width=250,
        height=45,
        command=salvar_edicao
    )

    botao_salvar.pack(pady=30)


# ============================================================
# VISUALIZAR CLIENTES
# ============================================================

def visualizar_clientes():

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM clientes
        ORDER BY id
    """)

    clientes = cursor.fetchall()

    conexao.close()

    # Cria janela
    janela_clientes = ctk.CTkToplevel(janela)

    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("1200x700")

    # ========================================================
    # TÍTULO
    # ========================================================

    titulo_clientes = ctk.CTkLabel(
        janela_clientes,
        text="CLIENTES CADASTRADOS",
        font=("Arial", 26, "bold")
    )

    titulo_clientes.pack(pady=25)

    # ========================================================
    # CABEÇALHO DA TABELA
    # ========================================================

    cabecalho = ctk.CTkFrame(
        janela_clientes,
        corner_radius=10
    )

    cabecalho.pack(
        padx=20,
        pady=10,
        fill="x"
    )

    colunas = [
        ("ID", 50),
        ("Nome", 200),
        ("E-mail", 250),
        ("Endereço", 250),
        ("Celular", 150),
        ("Ações", 200)
    ]

    for coluna, largura in colunas:

        label = ctk.CTkLabel(
            cabecalho,
            text=coluna,
            font=("Arial", 14, "bold"),
            width=largura
        )

        label.pack(
            side="left",
            padx=2,
            pady=10
        )

    # ========================================================
    # CLIENTES
    # ========================================================

    if len(clientes) == 0:

        mensagem = ctk.CTkLabel(
            janela_clientes,
            text="Nenhum cliente cadastrado.",
            font=("Arial", 18)
        )

        mensagem.pack(pady=40)

        return

    for cliente in clientes:

        linha = ctk.CTkFrame(
            janela_clientes,
            corner_radius=8
        )

        linha.pack(
            padx=20,
            pady=5,
            fill="x"
        )

        # ID
        label_id = ctk.CTkLabel(
            linha,
            text=str(cliente[0]),
            width=50
        )

        label_id.pack(
            side="left",
            padx=2,
            pady=10
        )

        # NOME
        label_nome = ctk.CTkLabel(
            linha,
            text=cliente[1],
            width=200
        )

        label_nome.pack(
            side="left",
            padx=2
        )

        # EMAIL
        label_email = ctk.CTkLabel(
            linha,
            text=cliente[2],
            width=250
        )

        label_email.pack(
            side="left",
            padx=2
        )

        # ENDEREÇO
        label_endereco = ctk.CTkLabel(
            linha,
            text=cliente[3],
            width=250
        )

        label_endereco.pack(
            side="left",
            padx=2
        )

        # CELULAR
        label_celular = ctk.CTkLabel(
            linha,
            text=cliente[4],
            width=150
        )

        label_celular.pack(
            side="left",
            padx=2
        )

        # ====================================================
        # BOTÃO EDITAR
        # ====================================================

        botao_editar = ctk.CTkButton(
            linha,
            text="EDITAR",
            width=80,
            height=30,
            command=lambda c=cliente: editar_cliente(c)
        )

        botao_editar.pack(
            side="left",
            padx=5
        )

        # ====================================================
        # BOTÃO EXCLUIR
        # ====================================================

        botao_excluir = ctk.CTkButton(
            linha,
            text="EXCLUIR",
            width=80,
            height=30,
            fg_color="#C0392B",
            hover_color="#922B21",
            command=lambda id=cliente[0]: excluir_cliente(id)
        )

        botao_excluir.pack(
            side="left",
            padx=5
        )


# ============================================================
# CRIAR BANCO
# ============================================================

criar_banco()


# ============================================================
# CONFIGURAÇÃO DA JANELA
# ============================================================

janela = ctk.CTk()

janela.title("Sistema de Cadastro de Clientes")

janela.geometry("1700x750")


# ============================================================
# CONFIGURAÇÃO DO TEMA
# ============================================================

ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")


# ============================================================
# TÍTULO
# ============================================================

titulo = ctk.CTkLabel(
    janela,
    text="SISTEMA DE CADASTRO DE CLIENTES",
    font=("Arial", 28, "bold")
)

titulo.pack(pady=30)


# ============================================================
# FRAME DO FORMULÁRIO
# ============================================================

formulario = ctk.CTkFrame(
    janela,
    width=800,
    height=500,
    corner_radius=15
)

formulario.pack(pady=10)

formulario.pack_propagate(False)


# ============================================================
# NOME
# ============================================================

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


# ============================================================
# E-MAIL
# ============================================================

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


# ============================================================
# ENDEREÇO
# ============================================================

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


# ============================================================
# CELULAR
# ============================================================

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


# ============================================================
# BOTÃO ENVIAR
# ============================================================

botao_enviar = ctk.CTkButton(
    janela,
    text="CADASTRAR CLIENTE",
    font=("Arial", 16, "bold"),
    width=250,
    height=50,
    corner_radius=10,
    fg_color="#2E8B57",
    hover_color="#246B45",
    command=enviar
)

botao_enviar.pack(pady=15)


# ============================================================
# BOTÃO VISUALIZAR
# ============================================================

botao_visualizar = ctk.CTkButton(
    janela,
    text="VISUALIZAR CLIENTES",
    font=("Arial", 16, "bold"),
    width=250,
    height=50,
    corner_radius=10,
    command=visualizar_clientes
)

botao_visualizar.pack(pady=5)


# ============================================================
# INICIAR PROGRAMA
# ============================================================

janela.mainloop()