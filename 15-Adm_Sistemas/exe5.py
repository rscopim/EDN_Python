import os
import subprocess

# Exercício 5: Recuperando informações do sistema com uname -a
command = "systeminfo" if os.name == "nt" else "uname"
commandArgument = "" if os.name == "nt" else "-a"
print(f'\nGathering system information with command: {command} {commandArgument}')
subprocess.run([command] if os.name == "nt" else [command, commandArgument])