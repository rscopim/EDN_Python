myString = "Isso é uma string"
print(myString)
print(type(myString))
print(myString + ", ela é do tipo de dados " + str(type(myString)))

primeiraString = "Ricardo "
segundaString = "Scopim"
terceiraString = primeiraString + segundaString
print(terceiraString)
print(primeiraString)
print(segundaString)
print(type(primeiraString))
print(primeiraString + ", ela é do tipo de dados " + str(type(primeiraString)))

name = input("Qual é o seu nome? ")
print(name)

color = input("Qual é a sua cor favorita?  ")
animal = input("Qual é o seu animal favorito?  ")
print("{}, você gosta da cor {} e do animal {}!".format(name,color,animal))