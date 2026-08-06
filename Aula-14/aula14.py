import os
# **Exercício 1: Criar e ler um Arquivo**

with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá!")

with open("arquivo.txt", "r") as arquivo:
    texto = arquivo.read()
    print(texto)

# **Exemplo 2: Cria um Diretório**



os.mkdir("aula14")

# **Exercício 3: Renomear um Diretório**



os.rename("aula14", "python")

# **Exercício 4:  Listar Arquivos em um Diretório** 



arquivos = os.listdir("python")

print(arquivos)

# **Exercício 5:  Copiar Arquivos em um Diretório**

import shutil

shutil.copy("arquivo.txt", "copia.txt")

# **Exercício 6:  Remover**



os.remove("arquivo.txt")