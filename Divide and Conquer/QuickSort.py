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


x = [1, 4, 8, 2, 1, 0, 2]
quick_sort(x, 0, 6)
print(x)
