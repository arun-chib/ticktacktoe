board = ['-','-','-',
         '-','-','-',
         '-','-','-',]

currPlayer='X'
#oPlayer='O'
gameRunning = True
def printBoard(board):
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[6],"|",board[7],"|",board[8])
    
#Display board.


# Take input from players

def enterInput(board):
    inp = int(input(f"Hey {currPlayer}! Enter number from 1-9:"))
    

    if inp >= 1  and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currPlayer
    else:
        print("Sorry! currPlayer is already at that position!! Try Again!!\n\n")

def winner_horizontal(board):
    global winner
    if board [0] == board [1] == board [2] and board[2] != '-':
        winner = board [0]
        return True
    if board [3] == board [4] == board [5] and board[5] != '-':
        winner = board [3]
        return True
    if board [6] == board [7] == board [8] and board[6] != '-':
        winner = board [6]
        return True
    

def winner_vertical(board):
    global winner
    if board [0] == board [3] == board [6] and board[6] != '-':
       winner = board [6]
       return True
    if board [1] == board [4] == board [7] and board[7] != '-':
        winner = board [4]
        return True
    if board [2] == board [5] == board [8] and board[5] != '-':
        winner = board [2]
        return True

def winner_diagonal(board):
    global winner
    if board [0] == board [4] == board [8] and board[8] != '-':
        winner = board [4]
        return True
    if board [2] == board [4] == board [6] and board[6] != '-':
        winner = board [6]
        return True

def checkwin(board):
    global winner
    global gameRunning
    if winner_diagonal(board) or winner_horizontal(board) or winner_vertical(board):
        print (f"The Winner is {winner}")
        gameRunning = False


   
def checktie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print ("Its a Tie")
        gameRunning = False
#switch Player
        
def switchPlayer():
    global currPlayer
    if currPlayer == 'X':
        currPlayer = 'O'
    elif currPlayer == "O":
        currPlayer = 'X'

while gameRunning:
    printBoard(board)
    enterInput(board)
    checkwin(board)
    checktie(board)
    switchPlayer()