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



import sqlite3
import customtkinter as tk
from tkinter import messagebox

def banco ():
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



def dados ():
    nome = entrada_nome.get.strip()
    email = entrada_email.get.strip()
    telefone = entrada_telefone.get.strip()
    endereco = entrada_endereco.get.strip()

