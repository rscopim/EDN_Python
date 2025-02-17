import os
import subprocess

# Exercício 6: Recuperando informações sobre processos ativos com ps -x
command = "tasklist" if os.name == "nt" else "ps"
commandArgument = "" if os.name == "nt" else "-x"
print(f'\nGathering active process information with command: {command} {commandArgument}')
subprocess.run([command] if os.name == "nt" else [command, commandArgument])