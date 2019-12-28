
import math

def fun(matrix):
    k=0
    while k<n:
        i=0
        while i<n:
            j=0
            while j<n:
                matrix[][]=max( matrix[i][j], min( matrix[i][k], matrix[k][j] ) )
                j+=1
            i+=1
        k+=1


inf = math.inf

