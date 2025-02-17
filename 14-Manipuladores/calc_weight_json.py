# Exercício 3: Criando o programa principal
# Criamos um programa principal para processar os dados JSON e calcular o peso molecular da insulina.

import jsonFileHandler  # Importamos o módulo jsonFileHandler

data = jsonFileHandler.readJsonFile('files/insulin.json')  # Lemos os dados do arquivo JSON

if data != "":  # Verificamos se os dados foram carregados corretamente
    bInsulin = data['molecules']['bInsulin']  # Recuperamos a sequência da cadeia B da insulina
    aInsulin = data['molecules']['aInsulin']  # Recuperamos a sequência da cadeia A da insulina
    insulin = bInsulin + aInsulin  # Concatenamos as cadeias A e B para formar a insulina completa
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']  # Recuperamos o peso molecular real da insulina
    
    print('bInsulin: ' + bInsulin)  # Exibimos a cadeia B da insulina
    print('aInsulin: ' + aInsulin)  # Exibimos a cadeia A da insulina
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))  # Exibimos o peso molecular real
else:
    print("Error. Exiting program")  # Caso os dados não sejam carregados, exibimos um erro

# Calculando o peso molecular aproximado da insulina
if data != "":
    aaWeights = data['weights']  # Obtemos o dicionário contendo os pesos dos aminoácidos
    
    # Contamos quantas vezes cada aminoácido aparece na sequência de insulina
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aaWeights.keys()})  
    
    # Calculamos o peso molecular somando o número de cada aminoácido multiplicado pelo seu peso
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in aaWeights.keys()}.values())  
    
    # Exibimos o peso molecular aproximado da insulina
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    
    # Calculamos e exibimos o erro percentual entre o peso real e o peso aproximado
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
