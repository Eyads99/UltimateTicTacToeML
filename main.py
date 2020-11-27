import numpy as np
import math
import random
# x==
turn = 'x'
board =np.zeros((9,9))
inputMB=-1
inputPosition=-1
miniboardOutcome=np.zeros(9)


def inputXO():
    global turn
    global inputMB
    global board
    global inputPosition
    isValid = False

    if(inputMB!=-1): ##very first input of game
        manualMB = True
    else: #very first input of game
        if (miniboardOutcome[inputMB]!=0): #has an outcome
            manualMB=False
        else: #does not have an outcome
            manualMB=True


    while isValid==False:
        if(manualMB):
            inputMB = input(turn + "'s turn: input your Miniboard number")
        else:
            print("you are paying in miniboard"+inputMB)
        inputPosition = input(turn + "'s turn:intput your Position number")
        if(board[inputMB][inputPosition]==0):
            board[inputMB][inputPosition] == turn
            isValid=True
        else:
            print("Position is invalid, reinput")
    if(turn=='x'): turn='o'
    else: turn='x'
    inputMB=inputPosition


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

    miniboardOutcome[miniboard] = 't'
    return 't'
