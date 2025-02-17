import os
import subprocess

# Exercício 1: Usando os.system para listar arquivos do diretório
print("Executando ls usando os.system:")
os.system("dir" if os.name == "nt" else "ls")