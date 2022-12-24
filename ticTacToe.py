theBoard = {1 : ' ', 2 : ' ', 3 : ' ', 
            4 : ' ', 5 : ' ', 6 : ' ',
            7 : ' ', 8 : ' ', 9 : ' '}

def printBoard(board):
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[7]}|{board[8]}|{board[9]}")

printBoard(theBoard)
turn = 'X'
while True:
    if turn == 'X':
        try:
            move= int(input('Enter column number : '))
            if theBoard[move] == ' ':
                theBoard[move] = 'X'
                printBoard(theBoard)
                turn = 'O'

            else: 
                print('Bad move')
        except KeyError or ValueError:
            print('invalid move')
    else:
        try:
            move= int(input('Enter column number : '))
            if theBoard[move] == ' ':
                theBoard[move] = 'O'
                printBoard(theBoard)
                turn = 'X'
            else: 
                print('bad move')
        except KeyError or ValueError:
            print('invalid move')
    
    
        
    if (theBoard[1] == theBoard[4] == theBoard[7] and theBoard[1] == 'X' and theBoard[4] == 'X' and theBoard[7] == 'X' or 
            theBoard[2] == theBoard[5] == theBoard[8] and theBoard[2] == 'X' and theBoard[5] == 'X' and theBoard[8] == 'X' or
            theBoard[3] == theBoard[6] == theBoard[9] and theBoard[3] == 'X' and theBoard[6] == 'X' and theBoard[9] == 'X' or
            theBoard[1] == theBoard[2] == theBoard[3] and theBoard[1] == 'X' and theBoard[2] == 'X' and theBoard[3] == 'X' or
            theBoard[4] == theBoard[5] == theBoard[6] and theBoard[4] == 'X' and theBoard[5] == 'X' and theBoard[6] == 'X' or
            theBoard[7] == theBoard[8] == theBoard[9] and theBoard[7] == 'X' and theBoard[8] == 'X' and theBoard[9] == 'X' or
            theBoard[1] == theBoard[5] == theBoard[9] and theBoard[1] == 'X' and theBoard[5] == 'X' and theBoard[9] == 'X' or
            theBoard[3] == theBoard[5] == theBoard[7] and theBoard[3] == 'X' and theBoard[5] == 'X' and theBoard[7] == 'X'):
                
                print("X won")
                break
            
    elif (theBoard[1] == theBoard[4] == theBoard[7] and theBoard[1] == 'O' and theBoard[4] == 'O' and theBoard[7] == 'O' or 
        theBoard[2] == theBoard[5] == theBoard[8] and theBoard[2] == 'O' and theBoard[5] == 'O' and theBoard[8] == 'O' or
        theBoard[3] == theBoard[6] == theBoard[9] and theBoard[3] == 'O' and theBoard[6] == 'O' and theBoard[9] == 'O' or
        theBoard[1] == theBoard[2] == theBoard[3] and theBoard[1] == 'O' and theBoard[2] == 'O' and theBoard[3] == 'O' or
        theBoard[4] == theBoard[5] == theBoard[6] and theBoard[4] == 'O' and theBoard[5] == 'O' and theBoard[6] == 'O' or
        theBoard[7] == theBoard[8] == theBoard[9] and theBoard[7] == 'O' and theBoard[8] == 'O' and theBoard[9] == 'O' or
        theBoard[1] == theBoard[5] == theBoard[9] and theBoard[1] == 'O' and theBoard[5] == 'O' and theBoard[9] == 'O' or
        theBoard[3] == theBoard[5] == theBoard[7] and theBoard[3] == 'O' and theBoard[5] == 'O' and theBoard[7] == 'O'):

            print('O won')
            break