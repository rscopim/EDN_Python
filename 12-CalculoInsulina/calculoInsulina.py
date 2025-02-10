# Python3.6  
# Coding: utf-8  

# Armazena a sequência da preproinsulina humana
preproInsulina = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Armazena as diferentes cadeias da insulina humana
lsInsulina = "malwmrllpllallalwgpdpaaa"  
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulina = "giveqcctsicslyqlenycn"  
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"  

# Combina as cadeias relevantes para formar a insulina funcional
insulina = bInsulina + aInsulina  

# Dicionário contendo os valores de pKa dos aminoácidos que contribuem para a carga líquida
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Conta o número de cada aminoácido relevante na sequência da insulina
seqCount = {x: float(insulina.count(x)) for x in ['y','c','k','h','r','d','e']}

# Inicializa a variável de pH
pH = 0  

# Loop para calcular a carga líquida da insulina de pH 0 a 14
while pH <= 14:
    netCharge = (
        +(sum({x: ((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x]))) for x in ['k', 'h', 'r']}.values()))
        -(sum({x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x]))) for x in ['y', 'c', 'd', 'e']}.values()))
    )
    
    # Exibe o pH e a carga líquida formatada com duas casas decimais
    print('{0:.2f}'.format(pH), netCharge)
    
    # Incrementa o pH
    pH += 1

# Explicação das variáveis e comandos utilizados:
# - preproInsulina, lsInsulina, bInsulina, aInsulina, cInsulina: Armazenam sequências da insulina humana.
# - insulina: Combina as cadeias B e A para formar a insulina funcional.
# - pKR: Dicionário com valores de pKa para os aminoácidos relevantes.
# - count(): Conta a ocorrência de um aminoácido na sequência.
# - float(): Converte o valor da contagem para um número decimal.
# - seqCount: Dicionário que armazena a contagem de cada aminoácido relevante.
# - while: Loop que repete o cálculo da carga líquida para valores de pH de 0 a 14.
# - .values(): Obtém os valores de um dicionário para serem usados nos cálculos.
# - sum(): Soma os valores obtidos para os grupos carregados positivamente e negativamente.
# - print('{0:.2f}'.format(pH), netCharge): Exibe o pH com duas casas decimais e a carga líquida correspondente.
