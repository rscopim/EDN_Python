import os
import subprocess

# Exercício 4: Usando subprocess.run com argumento de diretório específico (README.md)
# print("\nExecutando ls -l README.md usando subprocess.run:")
# subprocess.run(["dir", "README.md"] if os.name == "nt" else ["ls", "-l", "README.md"])

# Verifica o sistema operacional e define o comando correto
if os.name == "nt":
    command = f'cmd /c dir | findstr README.md'  # Filtra a saída para exibir README.md
else:
    command = "ls -l README.md"

print(f"Executando {command} usando subprocess.run:")

# Usa shell=True para comandos internos do Windows
subprocess.run(command, shell=True)