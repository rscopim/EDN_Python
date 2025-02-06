import csv  # Importa a biblioteca 'csv', que permite ler e escrever arquivos no formato CSV (Comma Separated Values)
import copy  # Importa a biblioteca 'copy', que contém a função 'deepcopy' para criar cópias independentes de objetos

# Definição do dicionário 'meuVeiculo', que serve como modelo para criar os veículos
meuVeiculo = {
    "vin" : "<empty>",       # VIN do veículo (identificador único)
    "make" : "<empty>",      # Marca do veículo
    "model" : "<empty>",     # Modelo do veículo
    "year" : 0,              # Ano de fabricação do veículo
    "range" : 0,             # Autonomia do veículo em quilômetros
    "topSpeed" : 0,          # Velocidade máxima do veículo em km/h
    "zeroSixty" : 0.0,       # Tempo de aceleração de 0 a 100 km/h
    "mileage" : 0            # Quilometragem do veículo
}

# Loop para imprimir as chaves e valores do dicionário 'meuVeiculo'
for key, value in meuVeiculo.items():
    print("{} : {}".format(key, value))  # O método '.format()' é usado para formatar e inserir variáveis dentro de strings

# Lista para armazenar os dados de veículos lidos do arquivo CSV
listaInventario = []

# Abertura do arquivo CSV 'car_fleet.csv' para leitura dos dados
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  # 'csv.reader' cria um objeto para ler o arquivo CSV
    lineCount = 0  # Contador de linhas lidas
    # Loop para processar cada linha do arquivo CSV
    for row in csvReader:
        if lineCount == 0:  # Se for a primeira linha (nomes das colunas)
            print(f'Column names are: {", ".join(row)}')  # 'join()' combina elementos de uma lista em uma única string, separados por vírgulas
            lineCount += 1  # Incrementa o contador de linhas
        else:  # Para todas as outras linhas
            # Exibe os dados do veículo presentes na linha
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            
            # Cria uma cópia profunda do dicionário 'meuVeiculo'
            currentVehicle = copy.deepcopy(meuVeiculo)  # A função 'deepcopy()' cria uma cópia completa de um objeto, incluindo objetos internos
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            
            # Adiciona o veículo processado à lista 'listaInventario'
            listaInventario.append(currentVehicle)  
            lineCount += 1  # Incrementa o contador de linhas
    
    print(f'Processed {lineCount} lines.')  # Exibe o número total de linhas processadas

# Criação de uma nova cópia do dicionário 'meuVeiculo' para uso posterior
currentVehicle = copy.deepcopy(meuVeiculo)

# Loop para exibir os dados de todos os veículos armazenados na lista 'listaInventario'
for myCarProperties in listaInventario:
    # Loop para imprimir todas as propriedades de cada veículo
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))  # Exibe a chave e o valor do veículo
        print("-----")  # Exibe uma linha separadora entre as propriedades

# Explicação dos elementos usados no código:

# IMPORT: O comando 'import' é utilizado para carregar bibliotecas ou módulos no código. 
# Aqui, ele carrega o módulo 'csv' para leitura de arquivos CSV e o módulo 'copy' para manipulação de objetos.

# FOR: O loop 'for' é utilizado para iterar sobre itens de uma sequência (como listas ou dicionários).
# Neste código, ele é utilizado para iterar sobre as chaves e valores do dicionário e também para percorrer as linhas do arquivo CSV.

# WITH: O comando 'with' é utilizado para trabalhar com recursos que precisam ser fechados ou liberados após o uso, como arquivos.
# Aqui, ele garante que o arquivo CSV seja fechado corretamente após o seu processamento, evitando possíveis problemas de leitura/escrita.

# .format: O método '.format()' é utilizado para inserir valores dentro de uma string, usando chaves ('{}') como marcadores.
# No código, ele é utilizado para formatar e exibir informações como 'key' e 'value' dentro das strings.

# .deepcopy: A função 'deepcopy()' da biblioteca 'copy' é utilizada para criar uma cópia independente de um objeto.
# Ela é útil para evitar que alterações no objeto copiado afetem o objeto original.

# .join: O método '.join()' é utilizado para unir os elementos de uma sequência (como uma lista) em uma única string, 
# separando-os por um delimitador especificado, como uma vírgula.

# .reader: A função 'csv.reader' cria um objeto que pode ser utilizado para ler arquivos CSV.
# Ela lê cada linha do arquivo e a divide em uma lista de valores, separados por vírgulas (ou outro delimitador definido).