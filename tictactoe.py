import os

board = [1,2,3,4,5,6,7,8,9]
player = "X"
gameOver = False
winner = ""

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


def checkGameOVer():
    global winner
    #[1,2,3][4,5,6][7,8,9][1,4,7][2,5,8][3,6,9][1,6,9][7,8,9]
    global gameOver
    if (board[0] == board[1] and board[2] == board[3]) or (board[3]== board[4] and board[4] == board[5]) or (board[6]== board[7] and board[7] == board[8]) or (board[0]== board[3] and board[3] == board[6]) or (board[1]== board[4] and board[4] == board[7]) or (board[2]== board[5] and board[5] == board[9]) or (board[0]== board[5] and board[5] == board[8]) or (board[6]== board[7] and board[7] == board[8]):
        gameOver = True
        winner = "A"
    

while not gameOver:
    printBoard()
    checkGameOVer()
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



    except:
        print("---------------------------------------------------------------")
        print("| You're really a dumb. Can't you just choose a valid option. |")
        print("---------------------------------------------------------------")
    
if gameOver == True:
    print(checkGameOVer())   