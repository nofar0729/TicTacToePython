#!/usr/bin/env python3


import random

def display_board(board):
    print(board[7]+ "|" + board[8] + "|" + board[9])
    print("-----")
    print(board[4]+ "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[1]+ "|" + board[2] + "|" + board[3])


def player_input(board, player):
    invalid = True
    inp = input(player + ", please enter your pick")
    num = int(inp)
    while (invalid):
        if not (1 <= num <= 9):
            print("Invalid pick, please try again a number between 1-9")
        elif (board[num] != " "):
            print("This place is already taken! Please choose a different place")
        else:
            invalid = False
            board[num] = player
            display_board(board)
            break
        inp = input(player + ", please enter your pick")
        num = int(inp)


def win(board, mark):
    if((board[1] == board[2] and board[2] == board[3] and board[1] == mark) or
       (board[4] == board[5] and board[5] == board[6] and board[4] == mark) or
       (board[7] == board[8] and board[9] == board[8] and board[8] == mark) or
       (board[1] == board[4] and board[4] == board[7] and board[7] == mark) or
       (board[2] == board[5] and board[5] == board[8] and board[8] == mark) or
       (board[3] == board[6] and board[9] == board[3] and board[3] == mark) or
       (board[1] == board[5] and board[5] == board[9] and board[9] == mark) or
       (board[3] == board[5] and board[7] == board[3] and board[3] == mark)) :
        return True
    return False


def choose_first():
    ran = random.randint(0,100)
    if ran %2 != 0:
        first = player2
        second = player1


def space_check(board,position):
    return not(board[position] != " ")


def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def replay():
    again = input("Would you like to play again? (yes/no)")
    if again == "no":
        game = False
    board = ([" "," "," "," "," "," "," "," "," "," "])
    return again


print("Tic Tac Toe Game")
print("Hello Player 1, please enter your name:")
name1 = input()
player1 = input(name1 + " now choose your mark, X or O")
name2 = input("Great, now player 2 please enter your name:")
player2 = "O"
if player1 == 'O' or player1 == 'o':
    player1 = 'O'
    player2 ='X'
print( name1 + ", you are " + player1 + " and " + name2 + ", you will be " + player2)
print("Let's start")
print("This will be your board game:")
board = ([" "," "," "," "," "," "," "," "," "," "])
display_board(["0","1","2","3","4","5","6","7","8","9"])
while(True):
    first = player1
    second = player2
    choose_first()
    player = first
    while not(full_board(board)):
        player_input(board,player)
        if(win(board,player)):
            print("Congrats " + player + " won the game!")
            break
        if player == first:
            player = second
        else:
            player = first
    if (full_board(board) and not win(board,player)):
        print("What a game, there was a tie!")
    if (replay() == "no"):
        print("The end!")
        break
    else:
        board = ([" "," "," "," "," "," "," "," "," "," "])

