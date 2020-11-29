import numpy as np
import math
from numpy import random
# x==
turn = 'x'
# board =np.zeros((9,9))
board=np.full((9,9), ['e'],dtype=str)
inputMB=-1
inputPosition=-1
miniboardOutcome=np.full((9), ['e'],dtype=str)
print(miniboardOutcome)

def StateOfGame():
    global miniboardOutcome
    for i in range(3):
        if (miniboardOutcome[i] == miniboardOutcome[i + 3] == miniboardOutcome[i + 6]):  # check col
            if miniboardOutcome[i] != 'e':#this assumes that undefined state is e
                print("Player "+ miniboardOutcome[i]+" has won")
                return miniboardOutcome[i]#returning winnning symbol x or y

        if (miniboardOutcome[0 + (i * 3)] == miniboardOutcome[1 + (i * 3)] == miniboardOutcome[2 + (i * 3)]):  # check row
            if miniboardOutcome[0 + (i * 3)] != 'e':
                print("Player " + miniboardOutcome[0 + (i * 3)] + " has won")
                return miniboardOutcome[0 + (i * 3)]#return x or y

    if (miniboardOutcome[0] == miniboardOutcome[4] == miniboardOutcome[8]):  # check diag
        if miniboardOutcome[0] != 'e':
            print("Player " + miniboardOutcome[0] + " has won")
            return miniboardOutcome[0]

    if (miniboardOutcome[2] == miniboardOutcome[4] == miniboardOutcome[6]):  # check inv-diag
        if miniboardOutcome[2] != 'e':
            print("Player "+miniboardOutcome[2]+" has won")
            return miniboardOutcome[2]

    for i in range(9):
        if (miniboardOutcome[i] == 'e'):
            return 'i'#i for incomplete

    print("The game is tied :)")
    return 't'#the game is completly tied

def inputXO():
    global turn
    global inputMB
    global board
    global inputPosition

    isValid = False

    if (inputMB == -1):  ##very first input of game
        manualMB = True
    else:
        if (miniboardOutcome[inputMB] != 'e'):  # has an outcome
            print(miniboardOutcome)
            manualMB = True
        else:  # does not have an outcome
            manualMB = False

    while isValid==False:


        if(manualMB):
            # inputMB = int(input(turn + "'s turn: input your Miniboard number:  "))
            # inputMB-=1

            inputMB=random.randint(9)
            if not(inputMB <= 8 and inputMB >= 0 and miniboardOutcome[inputMB] == 'e'):


                isValid=False
                print("Miniboard input is not valid")
                continue
        else:
            print("you are paying in miniboard "+str(inputMB+1))
        # inputPosition =  int(input(turn + "'s turn:input your Position number:  "))
        # inputPosition-=1
        inputPosition = random.randint(9)
        if not(inputPosition <= 8 and inputPosition >= 0):
            isValid = False
            print("Input Position input is not valid")
            continue
        if(board[inputMB][inputPosition]=='e'):
            board[inputMB][inputPosition] = turn
            isValid = True
        else:
            print("Position is invalid, reinput")
    print(turn + " "+str(inputMB)+ " "+str(inputPosition) )
    print(manualMB)
    if(turn=='x'): turn = 'o'
    else: turn = 'x'
    miniboardOutcomeF(inputMB)
    inputMB = inputPosition
    printBoard()
    print(miniboardOutcome)

def miniboardOutcomeF(miniboard):
    for i in range(3):
        if(board[miniboard][i]==board[miniboard][i+3]==board[miniboard][i+6]): #check col
            if board[miniboard][i] != 'e':
                miniboardOutcome[miniboard] = board[miniboard][i]
                return board[miniboard][i]

        if(board[miniboard][0+(i*3)]==board[miniboard][1+(i*3)]==board[miniboard][2+(i*3)]): #check row
            if board[miniboard][0+(i*3)] !='e':
                miniboardOutcome[miniboard]=board[miniboard][0+(i*3)]
                return board[miniboard][0+(i*3)]

    if(board[miniboard][0]==board[miniboard][4]==board[miniboard][8]): #check diag
        if board[miniboard][0]!='e':
            miniboardOutcome[miniboard] = board[miniboard][0]
            return board[miniboard][0]

    if(board[miniboard][2]==board[miniboard][4]==board[miniboard][6]): #check inv-diag
        if board[miniboard][2] != 'e':
            miniboardOutcome[miniboard] = board[miniboard][2]#why is this 0 should be 2
            return board[miniboard][2]

    for i in range(9):
        if(board[miniboard][i]=='e'):
            return 'e'#should return e
    miniboardOutcome[miniboard] = 't'
    print(miniboardOutcome)
    return 't'




def printBoard():
    for q in range(3):
        for k in range(3):
            line = ""
            for i in range(3):
                for j in range(3):
                    line = line + board[i+(q*3)][j+(k*3)]
                    #line = line + str(i + (q * 3)) + str(j + (k * 3)) + " "
                line += "|"
            print(line)
        print("------------")
#     for i in range(3): #first three boards
#         for k in range(3):
#             print(board[i)
#             print(board[k][k*(i+1)]+board[k][k*(i+1)]+board[k][k*(i+1)]+' | ')
#     for j in range(3,6):
#
#     for i in range(6,9):


while StateOfGame()=='i':
    inputXO() #while loop




## x o x
## e e x
## x e e
