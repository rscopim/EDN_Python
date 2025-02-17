# Exercício 2: Criando o módulo manipulador de arquivo JSON
# Criamos um módulo chamado jsonFileHandler.py para ler os dados JSON.

import json  # Importamos o módulo JSON para manipular arquivos JSON

def readJsonFile(fileName):
    # Definimos a função que lê um arquivo JSON e retorna seu conteúdo como um dicionário Python
    data = ""  # Inicializamos a variável data como uma string vazia
    try:
        with open(fileName) as json_file:  # Abrimos o arquivo JSON
            data = json.load(json_file)  # Carregamos os dados JSON no dicionário
    except IOError:
        print("Could not read file")  # Exibimos uma mensagem caso o arquivo não possa ser lido
    return data  # Retornamos os dados JSON carregados
