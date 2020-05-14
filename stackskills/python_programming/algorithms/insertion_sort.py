def insertion_sort(arr):
    for k in range(1,len(arr)):
        # print(arr)
        chkIx = k
        while chkIx > 0 :
            if arr[chkIx] < arr[chkIx-1]:
                arr[chkIx], arr[chkIx-1] = arr[chkIx-1], arr[chkIx]
            chkIx-=1
    return arr

l = [10,2,5,8,4,6,7,1,3,9]
print(insertion_sort(l))
from random import randint
l = [randint(1,1000) for i in range(1000)]
print(insertion_sort(l))
