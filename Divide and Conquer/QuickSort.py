def partition(ilist, low, high):

    pivot_index = (low+high) // 2
    pivot = ilist[pivot_index]

    i = low
    j = high
    while i <= high and j > low:
        if ilist[i] < pivot and i != pivot_index:
            temp = ilist[low]
            ilist[low] = ilist[i]
            ilist[i] = temp
            low = low+1
            i = i+1
        elif ilist[i] > pivot:
            temp2 = ilist[j]
            ilist[j] = ilist[i]
            ilist[i] = temp2
            j = j-1
        elif ilist[i] == pivot:
            i = i+1
    return low


def quick_sort(ilist, low, high):

    if low < high:
        index = partition(ilist, low, high)
        quick_sort(ilist, low, index-1)
        quick_sort(ilist, index+1, high)




inputArr = []
new_input = 0
while(new_input!="0 0"): # for ending the Input stream u have to enter "0 0"
    new_input = input()
    if(new_input !="0 0" and new_input != ''):
        inputArr.append(int(new_input))
print(inputArr)
Arr= inputArr
quick_sort(Arr, 0, len(Arr)-1)
print(Arr)

# input Example : hit enter after each number then enter "0 0"  like below:
'''
2
3
4
0
2
1
0 0

'''