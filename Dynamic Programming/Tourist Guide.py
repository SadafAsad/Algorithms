
def solution(dynamic_table):
    n=len(dynamic_table)
    k=0
    while k<n:
        i=0
        while i<n:
            j=0
            while j<n:
                dynamic_table[i][j]=max( dynamic_table[i][j], min( dynamic_table[i][k], dynamic_table[k][j] ) )
                j+=1
            i+=1
        k+=1

def initializeMatris(matris, n):
    i=0
    while i<n:
        matris.append([])
        j=0
        while j<n:
            matris[i].append(0)
            j+=1
        i+=1



matrix = [
    [0, 30, 15, 10, 0, 0, 0],
    [30, 0, 0, 25, 60, 0, 0],
    [15, 0, 0, 40, 0, 20, 0],
    [10, 25, 40, 0, 0, 0, 35],
    [0, 60, 0, 0, 0, 0, 20],
    [0, 0, 20, 0, 0, 0, 30],
    [0, 0, 0, 35, 20, 30, 0]
]
solution(matrix)
print(99//matrix[0][6])



new_input = input()

inputsArr = []
cityNum = int(new_input[0])
roads = int(new_input[2])
matris=list()
initializeMatris(matris,cityNum)
i=0
while(new_input !="0 0"):
    new_input =input()
    while(i < roads):
        x, y, capa = new_input.split()
        matris[int(x)-1][int(y)-1] = int(capa)
        matris[int(y)-1][int(x)-1] = int(capa)
        i += 1
    


