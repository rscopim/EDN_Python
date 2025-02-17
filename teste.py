import os


def new_user():
    confirm = "N"
    whileconfirm!= "Y"
    username = input("Insira o nome do usuário a ser adicionado: ")
    print("Usar o nome de usuário '"+ username+ "'? (S/N)")
    confirm= input() .upper()
    os.system("sudoadduser"+ username)