# Python3.6  
# Coding: utf-8  

def obterAlfabetoDuplicado(alfabeto):
    # Duplica o alfabeto para permitir a cifra de César funcionar corretamente.
    # Exemplo: 'ABC' -> 'ABCABC'
    alfabetoDuplicado = alfabeto + alfabeto
    return alfabetoDuplicado


def obterMensagem():
    # Solicita ao usuário uma mensagem para criptografar.
    # Retorna a mensagem digitada.
    mensagemParaCriptografar = input("Digite uma mensagem para criptografar: ")
    return mensagemParaCriptografar


def obterChaveCifra():
    # Solicita ao usuário uma chave numérica para a cifra (entre 1 e 25).
    # Retorna o valor como inteiro.
    chave = int(input("Digite uma chave (número inteiro de 1 a 25): "))
    return chave


def criptografarMensagem(mensagem, chaveCifra, alfabeto):
    # Criptografa uma mensagem usando a cifra de César.
    # Converte a mensagem para maiúsculas.
    # Substitui cada letra pela letra deslocada pelo valor da chave.
    
    # Uso do 'def':
    # Em Python, 'def' é usado para definir uma função. Ele cria um bloco reutilizável de código
    # que pode ser chamado em diferentes partes do programa.
    
    mensagemCriptografada = ""
    mensagemMaiuscula = mensagem.upper()  # .upper() converte toda a string para letras maiúsculas
    
    for caractere in mensagemMaiuscula:  # Percorre cada caractere da mensagem
        posicao = alfabeto.find(caractere)  # .find() retorna o índice da letra no alfabeto
        novaPosicao = posicao + chaveCifra  # Aplica o deslocamento da cifra
        
        if caractere in alfabeto:  # Verifica se o caractere está no alfabeto
            mensagemCriptografada += alfabeto[novaPosicao]  # Adiciona a nova letra
        else:
            mensagemCriptografada += caractere  # Mantém caracteres não encontrados (espaços, pontuação, etc.)
            
        # Explicação do bloco for/if-else:
        # - O loop 'for' percorre cada caractere da mensagem.
        # - 'if caractere in alfabeto' verifica se o caractere está no alfabeto definido.
        # - Se a condição for verdadeira, a letra é deslocada pela chave e adicionada à mensagem.
        # - Caso contrário, o caractere original é mantido (como espaços e pontuações).
    
    return mensagemCriptografada


def descriptografarMensagem(mensagem, chaveCifra, alfabeto):
    # Descriptografa a mensagem criptografada.
    # Como a cifra de César é reversível, basta inverter a chave para obter a mensagem original.
    chaveDescriptografar = -chaveCifra  # Inverte o valor da chave
    return criptografarMensagem(mensagem, chaveDescriptografar, alfabeto)


def executarProgramaCifraCesar():
    # Função principal que coordena a execução do programa de cifra de César.
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alfabeto original: {alfabeto}')
    
    alfabetoDuplicado = obterAlfabetoDuplicado(alfabeto)  # Dobra o alfabeto
    print(f'Alfabeto duplicado: {alfabetoDuplicado}')
    
    mensagem = obterMensagem()  # Obtém a mensagem do usuário
    print(f'Mensagem original: {mensagem}')
    
    chaveCifra = obterChaveCifra()  # Obtém a chave numérica
    print(f'Chave escolhida: {chaveCifra}')
    
    mensagemCriptografada = criptografarMensagem(mensagem, chaveCifra, alfabetoDuplicado)
    print(f'Mensagem criptografada: {mensagemCriptografada}')
    
    mensagemDescriptografada = descriptografarMensagem(mensagemCriptografada, chaveCifra, alfabetoDuplicado)
    print(f'Mensagem descriptografada: {mensagemDescriptografada}')


# Chamada da função principal para iniciar o programa
executarProgramaCifraCesar()