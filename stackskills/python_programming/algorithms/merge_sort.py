def merge_sort(arr):
    if len(arr) == 1 :
        return arr
    else :
        mid = len(arr)//2
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:])
        # merge the merged
        ret = []
        while len(ret) < len(arr) :
            # out of left elements, add all the right (sorted)
            if len(left)==0:
                ret.extend(right)
            # out of right elements, add all the left (sorted)
            elif 0 == len(right):
                ret.extend(left)
            # left less than right
            elif left[0] < right[0] :
                ret.append(left.pop(0))
            # just do the right (could be r==l or r<l)
            else :
                ret.append(right.pop(0))
        return ret

# l = [10,2,5,8,4,6,7,1,3,9]
# print(merge_sort(l))
# from random import randint
# l = [randint(1,1000) for i in range(1000)]
# print(merge_sort(l))
