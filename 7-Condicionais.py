# Solicita ao usuário uma resposta sobre envio de pacote
# input(): captura a entrada do usuário e armazena na variável respostaUsuario
respostaUsuario = input("Você precisa enviar um pacote? (Enter Sim ou Não) ")

# if/else: estrutura condicional para verificar a resposta do usuário
if respostaUsuario == "Sim":
    # print(): exibe uma mensagem na tela
    print("Podemos ajudar você a enviar esse pacote!")  # Mensagem de confirmação
else:
    print("Por favor, volte quando precisar enviar um pacote. Obrigado.")  # Mensagem de despedida

# Solicita ao usuário uma escolha sobre serviços adicionais
respUser = input("Você gostaria de comprar selos, comprar um envelope ou fazer uma cópia? (Digite selos, envelope ou cópia) ")

# if/elif/else: estrutura condicional para verificar qual serviço o usuário escolheu
if respUser == "selos":
    print("Temos muitos designs de selos para escolher.")  # Resposta caso o usuário escolha selos
elif respUser == "envelope":
    print("Temos muitos tamanhos de envelope para escolher.")  # Resposta caso o usuário escolha envelope
elif respUser == "cópia":
    # Se o usuário escolher cópias, solicita a quantidade desejada
    # input(): captura o número de cópias que o usuário deseja
    copias = input("Quantas cópias você gostaria? (Digite um número) ")
    print("Aqui estão {} cópias.".format(copias))  # Exibe a quantidade de cópias solicitadas
else:
    print("Obrigado, volte sempre.")  # Caso o usuário digite uma opção inválida

# Explicação adicional sobre if/else e if/elif:
# - O if/else é usado quando há apenas duas possibilidades: uma condição verdadeira (if) e uma alternativa (else).
# - O if/elif/else é utilizado quando há múltiplas condições possíveis. O programa verifica cada condição na ordem em que aparecem.
# - O elif (else if) permite adicionar quantas verificações forem necessárias antes de chegar ao else, que age como um padrão caso nenhuma condição anterior seja atendida.
