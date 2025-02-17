import os
import subprocess

# Exercício 2: Usando subprocess.run para listar arquivos do diretório
print("\nExecutando ls usando subprocess.run:")
subprocess.run(["dir"] if os.name == "nt" else ["ls"])



# Escolhe o comando correto dependendo do sistema operacional
# command = "dir" if os.name == "nt" else "ls"

# print(f"Executando {command} usando subprocess.run:")

# Adiciona shell=True para permitir comandos internos do shell no Windows
# subprocess.run(command, shell=True)