import os
import random
continua = True
cont = 0
def verificar(xoro):
    xoro = xoro
    w = False
    for i in range(3):
            if velha[i][0] == xoro and velha[i][1] == xoro and velha[i][2] == xoro:
                print("Jogador " + xoro + " Venceu!")
                w = True
                break
            elif velha[0][i] == xoro and velha[1][i] == xoro and velha[2][i] == xoro:
                print("Jogador " + xoro + " Venceu!")
                w = True
                break
            elif velha[0][0] == xoro and velha[1][1] == xoro and velha[2][2] == xoro:
                print("Jogador " + xoro + " Venceu!")
                w = True
                break
            else:
                w = False 
    return w    
while continua:
    velha = [
        [" ", " " , " "],
        [" ", " " , " "],                                
        [" ", " " , " "]  
    ]    
    while cont <= 4:
        print("Jogo da Velha:")
        for a,b,c in velha:    
            print("|" + a + "|" + b + "|" + c + "|")
        linha = int(input("Digite a linha:"))
        coluna = int(input("Digite a coluna:"))
        velha[linha][coluna] = "x"
        win = verificar("x")
        if win==True:
            break                
        while velha[linha][coluna] == "x" or velha[linha][coluna] == "o":           
            if cont == 4:
                break
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)        
        velha[linha][coluna] = "o"
        win = verificar("o")        
        for a,b,c in velha:    
            print("|" + a + "|" + b + "|" + c + "|")
        if win==True:
            break              
        cont+=1
    continua = True if input("Digite s para outra partida: ") == "s" else False
    cont = 0
    win = False

"""
import os
import random
continua = True
cont = 0
win = False
while continua:
    velha = [
        [" ", " " , " "],
        [" ", " " , " "],                                
        [" ", " " , " "]  
    ]    
    while cont <= 4:
        print("Jogo da Velha:")
        for a,b,c in velha:    
            print("|" + a + "|" + b + "|" + c + "|")
        linha = int(input("Digite a linha:"))
        coluna = int(input("Digite a coluna:"))
        velha[linha][coluna] = "x"
        for i in range(3):
            if velha[i][0] == "x" and velha[i][1] == "x" and velha[i][2] == "x":
                print("Jogador x Venceu!")
                win = True
                break
            elif velha[0][i] == "x" and velha[1][i] == "x" and velha[2][i] == "x":
                print("Jogador x Venceu!")
                win = True
                break
            elif velha[0][0] == "x" and velha[1][1] == "x" and velha[2][2] == "x":
                print("Jogador x Venceu!")
                win = True
                break
        if win==True:
            break                
        while velha[linha][coluna] == "x" or velha[linha][coluna] == "o":           
            if cont == 4:
                break
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)        
        velha[linha][coluna] = "o"
        for i in range(3):
            if velha[i][0] == "o" and velha[i][1] == "o" and velha[i][2] == "o":
                print("Jogador o Venceu!")
                win = True
                break
            elif velha[0][i] == "o" and velha[1][i] == "o" and velha[2][i] == "o":
                print("Jogador o Venceu!")
                win = True
                break
            elif velha[0][0] == "o" and velha[1][1] == "o" and velha[2][2] == "o":
                print("Jogador o Venceu!")
                win = True
                break        
        for a,b,c in velha:    
            print("|" + a + "|" + b + "|" + c + "|")
        if win==True:
            break              
        cont+=1
    cont = 0
    win = False
    continua = True if input("Digite s para outra partida: ") == "s" else False
"""