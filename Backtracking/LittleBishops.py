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


def initializeBoard(board, n):
    i=0
    while i<n:
        board.append([])
        j=0
        while j<n:
            board[i].append(0)
            j+=1
        i+=1



inputsArr =[]
inputs = 0

while(inputs !="0 0"): # this while will fill the list of Inputs
    inputs = input()
    inputsArr.append(inputs)
i = len(inputsArr)
j=0
while(i != 0): #this while will take each inputs and run it
    
    new_input=inputsArr[j]
    if(new_input == "0 0"): # here will check if its have to be done or not ("0 0")
        break
    n = new_input[0]
    k = new_input[2]
    board = list() #reload the board
    counter = 0 #reload the counter 
    initializeBoard(board,int(n))
    bishop(board, int(k), 0, 0)
    print(counter)
    j +=1
    i -=1


