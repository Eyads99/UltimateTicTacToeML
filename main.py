import numpy as np
import math
import random
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
                #miniboardOutcome[miniboard] = board[miniboard][i]
                return miniboardOutcome[i]#returning winnning symbol x or y

        if (miniboardOutcome[0 + (i * 3)] == miniboardOutcome[1 + (i * 3)] == miniboardOutcome[2 + (i * 3)]):  # check row
            if miniboardOutcome[0 + (i * 3)] != 'e':
                #miniboardOutcome[miniboard] = board[miniboard][0 + (i * 3)]
                return miniboardOutcome[0 + (i * 3)]#return x or y

    if (miniboardOutcome[0] == miniboardOutcome[4] == miniboardOutcome[8]):  # check diag
        if miniboardOutcome[0] != 'e':
            #miniboardOutcome[miniboard] = board[miniboard][0]
            return miniboardOutcome[0]

    if (miniboardOutcome[2] == miniboardOutcome[4] == miniboardOutcome[6]):  # check inv-diag
        if miniboardOutcome[2] != 'e':
            #miniboardOutcome[miniboard] = board[miniboard][0]
            return miniboardOutcome[2]

    for i in range(9):
        if (miniboardOutcome[i] != 0):
            return 'i'#i for incomplete

    #print(miniboardOutcome)
    return 't'#the game is completly tied

def inputXO():
    global turn
    global inputMB

    global board
    global inputPosition
    isValid = False

    if(inputMB==-1): ##very first input of game
        manualMB = True
    else:
        if (minboardOutcome(inputMB)=='e'): #has an outcome
            manualMB=True
        else: #does not have an outcome
            manualMB=True


    while isValid==False:
        if(manualMB):
            inputMB = int(input(turn + "'s turn: input your Miniboard number"))
            if inputMB>9 or inputMB<0:
                isValid=False
                print("Miniboard input is not valid")
                break
        else:
            print("you are paying in miniboard"+str(inputMB))
        inputPosition =  int(input(turn + "'s turn:intput your Position number"))
        if inputPosition > 9 or inputPosition < 0:
            isValid = False
            print("Input Position input is not valid")
            break
        if(board[inputMB][inputPosition]=='e'):
            board[inputMB][inputPosition] = turn
            isValid=True
        else:
            print("Position is invalid, reinput")
    if(turn=='x'): turn='o'
    else: turn='x'
    inputMB=inputPosition
    print(board)

def minboardOutcome(miniboard):
    for i in range(3):
        if(board[miniboard][i]==board[miniboard][i+3]==board[miniboard][i+6]): #check col
            if board[miniboard][i] !=0:
                miniboardOutcome[miniboard]=board[miniboard][i]
                return board[miniboard][i]

        if(board[miniboard][0+(i*3)]==board[miniboard][1+(i*3)]==board[miniboard][2+(i*3)]): #check row
            if board[miniboard][0+(i*3)] !=0:
                miniboardOutcome[miniboard]=board[miniboard][0+(i*3)]
                return board[miniboard][0+(i*3)]

    if(board[miniboard][0]==board[miniboard][4]==board[miniboard][8]): #check diag
        if board[miniboard][0]!=0:
            miniboardOutcome[miniboard]=board[miniboard][0]
            return board[miniboard][0]
    if(board[miniboard][2]==board[miniboard][4]==board[miniboard][6]): #check inv-diag
        if board[miniboard][2] != 0:
            miniboardOutcome[miniboard]=board[miniboard][0]
            return board[miniboard][2]

    for i in range(9):
        if(board[miniboard][i]!=0):
            return 0
    miniboardOutcome[miniboard] = 't'
    print(miniboardOutcome)
    return 't'



while StateOfGame()=='i':
    inputXO() #while loop

