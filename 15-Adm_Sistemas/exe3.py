import os
import subprocess

# Exercício 3: Usando subprocess.run com argumento adicional (-l para listagem longa)cd ..
# print("\nExecutando ls -l usando subprocess.run:")
# subprocess.run(["dir"] if os.name == "nt" else ["ls", "-l"])

# Verifica o sistema operacional e define o comando correto
if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"

print(f"Executando {command} usando subprocess.run:")

# Usa shell=True para comandos internos do Windows
subprocess.run(command, shell=True)