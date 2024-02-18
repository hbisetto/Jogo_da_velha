"""
Jogo da Velha em linguagem Python.
Desenvolvido por Henrique Bisetto em Fev/2024
"""
__version__ = "0.0.1"
__author__ = "Henrique Bisetto"

import os
import sys

lin = 3
col = 3

contador = 1

M = []

for i in range(lin): 
    linha = []       
    for j in range(col):
        linha.append(contador)
        contador += 1
    M.append(linha)

def exibir(): 
    os.system("clear")
    print("JOGO DA VELHA")
    print("")
        
    for i in range(lin):
        for j in range(col):
            print(M[i][j], end = "  ")
        print(" ")

def verificacao():
    # Linhas horizontais
    if M[0][0] == "X" and M[0][1] == "X" and M[0][2] == "X":
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input() # este comando é para que o usuário leia a msgm, digite algo e feche o programa,
        sys.exit()
    elif M[1][0] == "X" and M[1][1] == "X" and M[1][2] == "X":
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input()
        sys.exit()
    elif M[2][0] == "X" and M[2][1] == "X" and M[2][2] == "X":
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input()
        sys.exit()
    elif M[0][0] == "O" and M[0][1] == "O" and M[0][2] == "O":
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
    elif M[1][0] == "O" and M[1][1] == "O" and M[1][2] == "O":
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
    elif M[2][0] == "O" and M[2][1] == "O" and M[2][2] == "O":
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
    # Linhas verticais
    elif M[0][0] == "X" and M[1][0] == "X" and M[2][0] == "X":
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input()
        sys.exit()
    elif M[0][1] == "X" and M[1][1] == "X" and M[2][1] == "X":
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input()
        sys.exit()
    elif M[0][2] == "X" and M[1][2] == "X" and M[2][2] == "X":
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input()
        sys.exit()
    elif M[0][0] == "O" and M[1][0] == "O" and M[2][0] == "O":
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
    elif M[0][1] == "O" and M[1][1] == "O" and M[2][1] == "O":
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
    elif M[0][2] == "O" and M[1][2] == "O" and M[2][2] == "O":
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
    # Diagonais
    elif M[0][0] == "X" and M[1][1] == "X" and M[2][2] == "X": 
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input()
        sys.exit()
    elif M[0][2] == "X" and M[1][1] == "X" and M[2][0] == "X":
        os.system("clear")
        print("VITÓRIA DO JOGADOR X!!")
        x = input()
        sys.exit() 
    elif M[0][0] == "O" and M[1][1] == "O" and M[2][2] == "O": 
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
    elif M[0][2] == "O" and M[1][1] == "O" and M[2][0] == "O":
        os.system("clear")
        print("VITÓRIA DO JOGADOR O!!")
        x = input()
        sys.exit()
                 
while True:
#    def exibir(): 
#        os.system("clear")
#        print("JOGO DA VELHA")
#        print("")
#        
#        for i in range(lin):
#            for j in range(col):
#                print(M[i][j], end = "  ")
#            print(" ")

    exibir()

    print()        
    casaX = input("Jogador X. Digite a casa escolhida: ")

    for i in range(lin):
        for j in range(col):
            if int(casaX) == M[i][j]:
                M[i][j] = "X"

    verificacao()
    exibir()

    print()
    casaO = input("Jogador O. Digite a casa escolhida: ")

    for i in range(lin):
            for j in range(col):
                if int(casaO) == M[i][j]:
                    M[i][j] = "O"
                    
    verificacao()
        
# TODO: verificar erros (se digitar valor < 1 ou >9)
# TODO: rodar em windows e Linux
# TODO: escolha randomica do jogador O
# TODO: converter para rodar em android
# TODO: adicionar placar



        




