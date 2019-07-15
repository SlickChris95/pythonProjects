
theBoard = {
'top-L':' ',
'top-M':' ',
'top-R':' ',
'mid-L':' ',
'mid-M':' ',
'mid-R':' ',
'low-L':' ',
'low-M':' ',
'low-R':' '
}

def printBoard(board):
    print(board['top-L']+ '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L']+ '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L']+ '|' + board['low-M'] + '|' + board['low-R'])

def checkWin(board,player):
    #rows
    if board['top-L'] == player and board['top-M'] == player and board['top-R'] == player:
        return True
    elif board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player:
        return True
    elif board['low-L'] == player and board['low-M'] == player and board['low-R'] == player:
        return True
    #columns
    elif board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player:
        return True
    elif board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player:
        return True
    elif board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player:
        return True
    #diagnonals
    elif board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player:
        return True
    elif board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player:
        return True

    else:
        return False

def main():
    print('Welcome to tic tac toe! \nPlay against your opponent!')
    turn = 'X'
    gameOver = False
    #change this for loop into a while loop, ends when gameOver= true
    while(gameOver != True):
        print('List of possible moves: top-L,top-M,top-R,mid-L,mid-M,mid-R,low-L,low-M,low-R')
        printBoard(theBoard)
        move = input('Turn for ' + turn + '. move on which space?')
        if(move == 'q'):
            break
        if(move in theBoard):
            if(theBoard[move] == ' '):
                theBoard[move] = turn
                print(checkWin(theBoard,turn))
                winner = checkWin(theBoard,turn)
                if(winner == True):
                    print(str(turn) + ' Won the game!')
                    break
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
            else:
                print('############')
                print('Space occupied')
                print('############')

        else:
            print('############')
            print('Invalid move')
            print('############')

    printBoard(theBoard)

main()
