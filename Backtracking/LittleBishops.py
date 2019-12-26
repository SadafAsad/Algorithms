def isSafe(board, row, column):
    
    n = len(board)
    
    i = row
    j = column
    while i != 0 and j != 0:
        i-=1
        j-=1
        if board[i][j]==1:
            return False

    i = row
    j = column
    while i != n-1 and j != n-1:
        i+=1
        j+=1
        if board[i][j] == 1:
            return False
        
    i = row
    j = column
    while i != 0 and j != n-1:
        i-=1
        j+=1
        if board[i][j] == 1:
            return False

    i = row
    j = column
    while i != n-1 and j != 0:
        i+=1
        j-=1
        if board[i][j] == 1:
            return False

    return True


def bishopSolution(board, k, row, column):

    global counter
    n = len(board)
    j = column
    
    if k == 0 and j == n-1:
        return True

    while j != n-1:
        if isSafe(board, row, j):
            board[row][j]=1
            if bishopSolution(board, k-1, row, j+1):
                counter+=1
                board[row][j]=0
        j+=1


    while row != n-1:



    j = 0
    row+=1
    while j != n:
        if isSafe(board, row, j):
            board[row][j]=1
            if bishopSolution(board, k-1, row+1, j):
                counter+=1
                board[row][j]=0
        j+=1
    
    board[row-1][column]=0


def bishopINLINE(board, k, row, column):

    global counter
    n = len(board)
    j = column

    if k == 0 and j == n:
        return True

    while j != n-1:
        if isSafe(board, row, j):
            board[row][j]=1
            if bishopINLINE(board, k-1, row, j+1):
                counter+=1
                board[row][j]=0
        j+=1

counter = 0
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
bishopSolution(board, 2, 0, 0)
print(counter)
