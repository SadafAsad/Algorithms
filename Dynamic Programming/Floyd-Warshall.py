def initializeTable(n):
    table = list()
    k=0
    while k<n+1:
        i=0
        table.append([])
        while i<n:
            j=0
            table[k].append([])
            while j<n:
                table[k][i].append(0)
                j+=1
            i+=1
        k+=1
    return table


def fillingTable(table, input_table):
    n = len(input_table)
    i=0
    while i<n:
        j=0
        while j<n:
            if input_table[i][j]!=0:
                table[0][i][j] = input_table[i][j]
            j+=1
        i+=1


def computingMins(table):
    n = len(table)
    k=0
    while k<n:
        i=0
        while i<n-1:
            j=0
            while j<n-1:
                table[k][i]][j] =  min( table[k-1][i]][j] , table[k-1][i][k] + table[k-1][k][j] )
                j+=1
            i+=1
        k+=1
