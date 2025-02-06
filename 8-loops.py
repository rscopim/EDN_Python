import random  # Importa a biblioteca 'random', que permite gerar números aleatórios

print("Bem-vindo ao Adivinhe o Número!")  # Exibe uma mensagem de boas-vindas
print("As regras são simples. Vou pensar em um número e você tentará adivinhá-lo.")  # Explica as regras do jogo

# Gera um número aleatório entre 1 e 10 (inclusive)
numero = random.randint(1, 10)  # A função randint gera um número aleatório dentro do intervalo especificado
advinheCerto = False  # Inicializa a variável de controle, que indica se o jogador acertou o número

# Inicia o loop, que continuará até que o número correto seja adivinhado
while advinheCerto != True:  # O loop continua enquanto 'advinheCerto' for False
    advi = input("Adivinhe um número entre 1 e 10: ")  # Solicita ao jogador que insira um palpite
    if int(advi) == numero:  # Verifica se o palpite (convertido para inteiro) é igual ao número gerado
        print("Você adivinhou {}. Isso está correto! Você venceu!".format(advi))  # Exibe uma mensagem de sucesso
        advinheCerto = True  # Se o jogador acertou, 'advinheCerto' se torna True, interrompendo o loop
    else:  # Caso o palpite esteja errado
        print("Você não adivinhou {}. Desculpe, não é isso. Tente novamente.".format(advi))  # Exibe uma mensagem de erro

# Explicações simplificadas dos termos:

# IMPORT: O comando 'import' é utilizado para carregar uma biblioteca externa no código.
# Aqui, 'import random' carrega a biblioteca 'random' para que possamos gerar números aleatórios.
# 
# random.randint: A função 'random.randint(a, b)' retorna um número inteiro aleatório entre os valores 'a' e 'b' (inclusive).
# Neste código, ela gera o número aleatório que o jogador precisa adivinhar, entre 1 e 10.
# 
# while / if / else:
# - while: O loop 'while' executa um bloco de código enquanto uma condição for verdadeira.
# No código, o loop continua pedindo palpites até o jogador acertar.
# 
# - if: O comando 'if' é utilizado para verificar se uma condição é verdadeira.
# Aqui, ele checa se o palpite do jogador é igual ao número aleatório gerado.
# 
# - else: O comando 'else' é executado caso a condição do 'if' não seja verdadeira.
# Neste caso, se o jogador não adivinhar o número, o código dentro do 'else' será executado, pedindo um novo palpite.
# 
# .format: O método '.format()' é utilizado para inserir variáveis dentro de uma string.
# As chaves '{}' são substituídas pelos valores que você fornece dentro do método 'format()'.
# No código, ele é usado para inserir o palpite do jogador na mensagem de resposta.


print("Count to 10!")  # Exibe uma mensagem na tela, pedindo para contar até 10

# Inicia um loop 'for', que vai iterar sobre uma sequência de números
# A função range(0, 11) gera uma sequência de números de 0 até 10 (11 é exclusivo)
for x in range(0, 11):  
    print(x)  # Exibe o valor de 'x' a cada iteração do loop, que vai de 0 a 10
