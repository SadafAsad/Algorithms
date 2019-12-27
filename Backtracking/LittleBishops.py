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


def bishop(board, k, row, column):

    global counter
    n = len(board)
    i = row
    j = column

    while i<n:
        while j<n:
            if isSafe(board, i, j):
                board[i][j]=1
                if i==n-1:
                    if j==n-1: 
                        if bishop(board, k-1, i+1, 0):
                            counter+=1
                            board[i][j]=0
                    else:
                        if bishop(board, k-1, i+1, j):
                            counter+=1
                            board[i][j]=0
                elif j==n-1:
                    if bishop(board, k-1, i, 0):
                        counter+=1
                        board[i][j]=0
                else:
                    if bishop(board, k-1, i, j):
                        counter+=1
                        board[i][j]=0
            j+=1
        i+=1

counter = 0
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
bishop(board, 2, 0, 0)
print(counter)
