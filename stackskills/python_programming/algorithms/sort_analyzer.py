import random, timeit, time

def analyze_func(func_name,arr) :
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc-tic
    return seconds

from . import selection_sort,quick_sort,bubble_sort,merge_sort
def test_all(runs) :
    l=[random.randint(1,maxval) for i in range(lsize)]
    qst_times,mst_times,bst_times,sst_times,srst_times = [],[],[],[],[]
    for i in range(runs) :
        qst_times.append(analyze_func(quick_sort.quick_sort,l))
        mst_times.append(analyze_func(merge_sort.merge_sort,l))
        bst_times.append(analyze_func(bubble_sort.bubble_sort,l))
        sst_times.append(analyze_func(selection_sort.selection_sort,l))
        srst_times.append(analyze_func(sorted,l))
    return qst_times,mst_times,bst_times,sst_times,srst_times

lsize = int(input("What size list do you want to create? "))
maxval = int(input("What is the max value of the range? "))
runs = int(input("How many times do you want to run? "))

# l=[random.randint(1,maxval) for i in range(lsize)]
# qst = timeit.Timer("quick_sort(l.copy())", f"from quick_sort import quick_sort\nfrom __main__ import l" )
# # qst = timeit.Timer("quick_sort(l)", f"from quick_sort import quick_sort\nfrom random import randint\nl=[randint(1,{maxval}) for i in range({lsize})]" )
# qst_times = qst.repeat(runs,1)
# #start
# # quick_sort.quick_sort(l)
# #stop
# #start
# l=[random.randint(1,maxval) for i in range(lsize)]
# mst = timeit.Timer("merge_sort(l.copy())", f"from merge_sort import merge_sort\nfrom __main__ import l" )
# mst_times = mst.repeat(runs,1)
# # merge_sort.merge_sort(l)
# #stop
# #start
# l=[random.randint(1,maxval) for i in range(lsize)]
# bst = timeit.Timer("bubble_sort(l.copy())", f"from bubble_sort import bubble_sort\nfrom __main__ import l" )
# bst_times = mst.repeat(runs,1)
# # bubble_sort.bubble_sort(l)
# #stop
# #start
# # selection_sort.selection_sort(l)
# l=[random.randint(1,maxval) for i in range(lsize)]
# sst = timeit.Timer("selection_sort(l.copy())", f"from selection_sort import selection_sort\nfrom __main__ import l" )
# sst_times = mst.repeat(runs,1)
# #stop
# #start
# # sorted(l)
# l=[random.randint(1,maxval) for i in range(lsize)]
# srst = timeit.Timer("sorted(l)", f"from __main__ import l" )
# srst_times = mst.repeat(runs,1)
# #stop
qst_times,mst_times,bst_times,sst_times,srst_times = test_all(runs)
for i in range(runs):
    print(f"Run: {i+1}")
    print(f"Quicksort\t-> Elapsed time: {qst_times[i]:.5f}")
    print(f"Mergesort\t-> Elapsed time: {mst_times[i]:.5f}")
    print(f"Bubblesort\t-> Elapsed time: {bst_times[i]:.5f}")
    print(f"Selectionsort\t-> Elapsed time: {sst_times[i]:.5f}")
    print(f"BIn-sorted\t-> Elapsed time: {srst_times[i]:.5f}")
    print("-"*40)
