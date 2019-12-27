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

    if k==0:
        return True

    while i<n:
        while j<n:
            if isSafe(board, i, j):
                board[i][j]=1
                if j==n-1:
                    if bishop(board, k-1, i+1, 0):
                        counter+=1
                else:
                    if bishop(board, k-1, i, j+1):
                        counter+=1
                board[i][j]=0        
            j+=1
        i+=1
        j=0
    return False

counter = 0
board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
bishop(board, 4, 0, 0)
print(counter)
