
# #this does not work. Trying to figure out how to do it without passing start/stop
# def binary_search_recur(arr,lup):
#     return binary_search_recur_w_ix(arr,lup,len(arr)//2)
#
# def binary_search_recur_w_ix(arr,lup,cix) :
#     if len(arr) == 0 :
#         return None
#
#     mid = len(arr)//2
#     print("searching for",lup,"in",arr,"with mid",mid)
#     if lup == arr[mid] :
#         return cix + mid
#
#     if lup < arr[mid]:
#         newArr = arr[:mid]
#         bsr = binary_search_recur_w_ix(newArr,lup)
#
#         mod = bsr-arr_mod
#         print('lt, bsr ret=',bsr,', modifying mid by',mod,'and',arr_mod, 'for',arr)
#         return mid + mod
#
#     if lup > arr[mid]:
#         newArr = arr[:mid]
#         mod = binary_search_recur(arr[mid+1:],lup)+(1*(len(newArr)%2))
#         print('lt, modifying mid by',mod)
#         return mid - mod

def binary_search_iter(arr,lup):
    ret = None
    lix,rix = 0,len(arr)-1
    cnt = 0
    while cnt < 10 and lix <= rix:
        mid = (rix+lix)//2
        if lup == arr[mid] :
            ret = mid
            break
        if lup > arr[mid] :
            lix =mid+1
        else :
            rix = mid-1
        cnt+=1

    return ret

# import random
# #test_list = sorted([random.randint(0,10) for i in range(11)])
# test_list = [0,1,2,3,4,5,6,7,8,9,10]
# cval = random.randint(0,11)
#
# for i in range(0,1) :
#     bs = binary_search_iter(test_list,i)
#     # bs = binary_search_recur(test_list,i)
#     print("Binary search for",i,"in",test_list,"returned",bs)
