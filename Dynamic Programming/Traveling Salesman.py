def initializeTable(n):
    counter = 2**(n-2)
    table = list()
    i=0
    while i<n-1:
        table.append([])
        j=0
        while j<counter:
            table[i].append([])
            table[i][j].append([])
            table[i][j].append(0)
            j+=1
        i+=1
    return table
