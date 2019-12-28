
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





new_input = input()
cityNum, roads = new_input.split()

matris=list()
initializeMatris(matris,int(cityNum))

i=0
while(new_input !="0 0"):
    while(i < int(roads)):
        new_input = input()
        x, y, capa = new_input.split()
        matris[int(x)-1][int(y)-1] = int(capa)
        matris[int(y)-1][int(x)-1] = int(capa)
        i += 1
    new_input = input()
    a, b, c = new_input.split()
    new_input = input()

solution(matris)
print( round(int(c)/matris[int(a)-1][int(b)-1]) )
    


