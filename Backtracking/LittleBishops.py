def isSafe(board,row,column):
    
    int board_len = board.len()
    
    int i = row
    int j = column
    for i!=0 and j!=0:
        i-=1
        j-=1
        if board[i][j]==1:
            return False

    i = row
    j = column
    for i!=board_len and j!=board_len:
        i+=1
        j+=1
        if board[i][j]==1:
            return False
        
    i = row
    j = column
    for i!=0 and j!=board_len:
        i-=1
        j+=1
        if board[i][j]==1:
            return False

    i = row
    j = column
    for i!=board_len and j!=0:
        i+=1
        j-=1
        if board[i][j]==1:
            return False

    return True

