def bubble_sort(arr) :
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1] :
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr


# l = [10,2,5,8,4,6,7,1,3,9]
# print(bubble_sort(l))
# from random import randint
# # l = [randint(1,1000) for i in range(1000)]
# # print(bubble_sort(l))
