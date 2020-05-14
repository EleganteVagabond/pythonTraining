def quick_sort(arr):
    if(len(arr) < 2) :
        return arr
    left, right = [],[]
    pivot = arr[-1]
    pivots= [pivot]
    for i in range(len(arr)-1):
        if arr[i] < pivot :
            left.append(arr[i])
        elif arr[i] > pivot :
            right.append(arr[i])
        else:
            pivots.append(pivot)
    return quick_sort(left) + pivots + quick_sort(right)

# l = [10,2,5,8,4,6,7,1,3,9]
# print(quick_sort(l))
# from random import randint
# l = [randint(1,1000) for i in range(1000)]
# print(quick_sort(l))
