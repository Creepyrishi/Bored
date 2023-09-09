import os
board = [1,2,3,4,5,6,7,8,9]
player = "X"
gameOver = False
winner = ""
gameTie = False

def printBoard():
    print(board[0] , "|" , board[1],  "|" , board[2])
    print("--|---|--")
    print(board[3] , "|" , board[4],  "|" , board[5])
    print("--|---|--")
    print(board[6] , "|" , board[7],  "|" , board[8])

def updateBoard(playerC, change):
    global player
    change = change-1
    if board[change] not in ["X", "O"]:
        board[change] = playerC
        if player == "X":
            player = "O"
        else:
            player  ="X"        
    else:
        print("---------------------------")
        print("| Spot already taken Dumb |")
        print("---------------------------")

def gameTie():
    pass

def checkGameOVer():
    global gameTie
    if (board[0] == board[1] and board[1]==board[2]):
        return True
    elif (board[3] == board[4] and board[4]==board[5]):
        return True
    elif (board[6] == board[7] and board[7]==board[8]):
        return True
    elif (board[0] == board[3] and board[3]==board[6]):
        return True
    elif (board[1] == board[4] and board[4]==board[7]):
        return True
    elif (board[2] == board[5] and board[5]==board[8]):
        return True
    elif (board[0] == board[4] and board[4]==board[8]):
        return True
    elif (board[2] == board[4] and board[4]==board[6]):
        return True
    elif (gameTie()):
        gameTie = True
        return True
    else:
        return False
    
printBoard()

while not gameOver:
    print(f"\n\n Current player : {player} \n\n")
    try:
        change = int(input("Enter Your Sweet Spot\t"))
        if change not in [1,2,3,4,5,6,7,8,9]:
            print("---------------------------------------------------------------")
            print("| You're really a dumb. Can't you just choose a valid option. |")
            print("---------------------------------------------------------------")
        else:
            updateBoard(player, change)
            os.system("cls")
            printBoard()
            if checkGameOVer():
                gameOver = True
                if player == "X":
                    winner = "O"
                else:
                    winner  ="X"   

    except:
        print("---------------------------------------------------------------")
        print("| You're really a dumb. Can't you just choose a valid option. |")
        print("---------------------------------------------------------------")
    
if gameOver == True:
    if not gameTie == True:
        print("--------------")
        print(f"| Winner is {winner} |")
        print("--------------")
    else:
        print("----------------------------------------------")
        print(f"| Game is Tie You Dumb. Just start new one.|")
        print("----------------------------------------------")
        