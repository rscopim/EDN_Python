# Definição da versão do Python e codificação do arquivo
# python3.6
# coding: utf-8

# Armazena a sequência de proteína da preproinsulina humana em uma variável
preproInsulina = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Armazena as diferentes cadeias da insulina humana
lsInsulina = "malwmrllpllallalwgpdpaaa"
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulina = "giveqcctsicslyqlenycn"
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Combina as cadeias relevantes para formar a insulina funcional
insulina = bInsulina + aInsulina

# Impressão das sequências no console
print("A sequência da preproinsulina humana:")
print(preproInsulina)

print("A sequência da insulina humana, cadeia a: " + aInsulina)

# Cálculo do peso molecular aproximado da insulina humana
# Dicionário com os pesos moleculares dos aminoácidos
pesosAminoacidos = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
             'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
             'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
             'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Conta o número de cada aminoácido na sequência da insulina
contagemAminoacidosInsulina = {x: float(insulina.upper().count(x)) for x in pesosAminoacidos.keys()}

# Multiplica a contagem pelo peso molecular de cada aminoácido
pesoMolecularInsulina = sum({x: (contagemAminoacidosInsulina[x] * pesosAminoacidos[x]) for x in pesosAminoacidos.keys()}.values())

# Exibe o peso molecular aproximado da insulina
print("O peso molecular aproximado da insulina: " + str(pesoMolecularInsulina))

# Cálculo do percentual de erro em relação ao peso real da insulina
pesoMolecularRealInsulina = 5807.63
erroPorcentagem = ((pesoMolecularInsulina - pesoMolecularRealInsulina) / pesoMolecularRealInsulina) * 100

# Exibe a porcentagem de erro
print("Porcentagem de erro: " + str(erroPorcentagem))

# ---- Explicação das variáveis e comandos ----
# - 'preproInsulina', 'lsInsulina', 'bInsulina', 'aInsulina', 'cInsulina': Variáveis que armazenam diferentes partes da sequência de insulina.
# - 'insulina': Combinação das cadeias B e A da insulina funcional.
# - 'pesosAminoacidos': Dicionário que contém o peso molecular de cada aminoácido.
# - 'contagemAminoacidosInsulina': Dicionário que conta quantas vezes cada aminoácido aparece na sequência de insulina.
# - 'pesoMolecularInsulina': Variável que armazena o peso molecular total da insulina calculado.
#
# Comandos usados:
# - float(): Converte valores para ponto flutuante, garantindo precisão em cálculos.
# - .upper(): Converte todas as letras da string para maiúsculas.
# - .count(): Conta o número de ocorrências de um caractere específico na string.
# - .keys(): Retorna todas as chaves de um dicionário.
# - .values(): Retorna todos os valores do dicionário.

