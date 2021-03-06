import math

# initializes dynamic table with infinities
def buildTable(n):
    table = list()
    i=0
    while i<n:
        table.append([])
        j=0
        while j<n:
            table[i].append(math.inf)
            j+=1
        i+=1
    return table

# this is where magic happens
def floydWarshall(table):
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


n = int(input("How many nodes? "))
table = buildTable(n)
e = int(input("How many edges? "))
print("Enter edges: ")
counter = 0
while counter<e:
    input_e = input().split()
    i = int(input_e[0])-1
    j = int(input_e[1])-1
    e_value = int(input_e[2])
    table[i][j] = e_value
    counter+=1
i = 0
while i<n:
    j = 0
    while j<n:
        if i==j:
            table[i][j] = 0
        j+=1
    i+=1
floydWarshall(table)
print(table)
