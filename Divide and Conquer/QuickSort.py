def partition(ilist, low, high):

    pivot_index = len(ilist) // 2
    pivot = ilist[pivot_index]

    i = 0
    while i <= high:
        if ilist[i] < pivot and i != pivot_index:
            temp = ilist[low]
            ilist[low] = ilist[i]
            ilist[i] = temp
            low = low+1
        i = i+1

