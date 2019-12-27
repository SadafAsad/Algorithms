def partition(ilist, low, high):

    pivot_index = (low+high) // 2
    pivot = ilist[pivot_index]

    i = low
    while i <= high:
        if ilist[i] < pivot and i != pivot_index:
            temp = ilist[low]
            ilist[low] = ilist[i]
            ilist[i] = temp
            low = low+1
        i = i+1

    return low


def quick_sort(ilist, low, high):

    if low < high:
        index = partition(ilist, low, high)
        quick_sort(ilist, low, index-1)
        quick_sort(ilist, index+1, high)




inputArr = []
new_input = 0
while(new_input!="0 0"):
    new_input = input()
    if(new_input !="0 0" and new_input != ''):
        inputArr.append(new_input)
print(inputArr)
Arr= inputArr
quick_sort(Arr, 0, len(Arr)-1)
print(Arr)

