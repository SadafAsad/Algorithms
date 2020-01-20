def computingMins(table):
    n=len(table)
    k=0
    while k<n:
        i=0
        while i<n:
            j=0
            while j<n:
                table[i][j] =  min( table[i][j] , table[i][k] + table[k][j] )
                j+=1
            i+=1
        k+=1


# t = [[0, 5, 999, 10],
#      [999, 0, 3, 999],
#      [999, 999, 0, 1],
#      [999, 999, 999, 0]]

t = [[0, 999, -2, 999],
     [4, 0, 3, 999],
     [999, 999, 0, 2],
     [999, -1, 999, 0]]

# t = [[0, 8, 999, 1],
#      [999, 0, 1, 999],
#      [4, 999, 0, 999],
#      [999, 2, 9, 0]]

computingMins(t)
print(t)

