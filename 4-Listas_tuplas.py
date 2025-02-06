# Criando uma lista de frutas
# Uma lista em Python é uma coleção ordenada e mutável
listaFruta = ["maça", "banana", "abacaxi"]
print(listaFruta)  # Exibe toda a lista
print(type(listaFruta))  # Mostra o tipo da variável (list)

# Acessando elementos da lista pelo índice
print(listaFruta[0])  # Primeiro elemento
print(listaFruta[1])  # Segundo elemento
print(listaFruta[2])  # Terceiro elemento

# Modificando um elemento da lista
listaFruta[2] = "goiaba"  # Substitui "abacaxi" por "goiaba"
print(listaFruta)  # Exibe a lista atualizada

# Criando uma tupla de frutas
# Uma tupla é uma coleção ordenada e imutável
listaFinaltupla = ("maça", "banana", "goiaba")
print(listaFinaltupla)  # Exibe toda a tupla
print(type(listaFinaltupla))  # Mostra o tipo da variável (tuple)

# Acessando elementos da tupla pelo índice
print(listaFinaltupla[0])  # Primeiro elemento
print(listaFinaltupla[1])  # Segundo elemento
print(listaFinaltupla[2])  # Terceiro elemento

# Criando um dicionário com frutas favoritas
# Um dicionário em Python é uma coleção de pares chave-valor
frutaFavoritaDictionary = {
  "Ricardo" : "maça",
  "Simines" : "banana",
  "Scopim" : "laranja"
}
print(frutaFavoritaDictionary)  # Exibe todo o dicionário
print(type(frutaFavoritaDictionary))  # Mostra o tipo da variável (dict)

# Acessando valores do dicionário através das chaves
print(frutaFavoritaDictionary["Ricardo"])  # Exibe a fruta favorita de Ricardo
print(frutaFavoritaDictionary["Simines"])  # Exibe a fruta favorita de Simines
print(frutaFavoritaDictionary["Scopim"])  # Exibe a fruta favorita de Scopim

# Explicação adicional:
# - type(): é uma função que retorna o tipo de uma variável, útil para verificar se uma estrutura de dados é lista, tupla ou dicionário.
# - Lista: uma coleção ordenada e mutável, permitindo alterações nos elementos.
# - Tupla: uma coleção ordenada e imutável, ou seja, seus valores não podem ser modificados após a criação.
# - Dicionário: uma coleção de pares chave-valor, onde cada chave é única e usada para acessar um valor associado.