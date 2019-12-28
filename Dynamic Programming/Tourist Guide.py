
import math

def fun(matrix, n):
    k=0
    while k<n:
        i=0
        while i<n:
            j=0
            while j<n:
                matrix[i][j]=max( matrix[i][j], min( matrix[i][k], matrix[k][j] ) )
                j+=1
            i+=1
        k+=1


inf = math.inf
matrix = [
    [0, 30, 15, 10, inf, inf, inf],
    [30, 0, inf, 25, 60, inf, inf],
    [15, inf, 0, 40, inf, 20, inf],
    [10, 25, 40, 0, inf, inf, 35],
    [inf, 60, inf, inf, 0, inf, 20],
    [inf, inf, 20, inf, inf, 0, 30],
    [inf, inf, inf, 35, 20, 30, 0]
]
fun(matrix, 7)
print(matrix[0][6])
