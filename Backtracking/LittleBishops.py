def isSafe(board,row,column):
    
    n = len(board)
    
    i = row
    j = column
    while i!=0 and j!=0:
        i-=1
        j-=1
        if board[i][j]==1:
            return False

    i = row
    j = column
    while i!=n and j!=n:
        i+=1
        j+=1
        if board[i][j]==1:
            return False
        
    i = row
    j = column
    while i!=0 and j!=n:
        i-=1
        j+=1
        if board[i][j]==1:
            return False

    i = row
    j = column
    while i!=n and j!=0:
        i+=1
        j-=1
        if board[i][j]==1:
            return False

    return True

