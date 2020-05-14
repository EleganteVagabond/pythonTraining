def selection_sort(arr):
    # need to find all numbers - 1
    for i in range(len(arr)-1):
        swapix = i
        min = arr[i]
        for i2 in range(i+1,len(arr)):
             if arr[i2] < min:
                 min = arr[i2]
                 swapix = i2
        if i != swapix:
            arr[i], arr[swapix] = arr[swapix], arr[i]

    return arr

# l = [10,2,5,8,4,6,7,1,3,9]
# print(selection_sort(l))
# # from random import randint
# # l = [randint(1,1000) for i in range(1000)]
# # print(selection_sort(l))
