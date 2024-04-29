from random import randint

l1 = [randint(1,100) for _ in range(1000)]
val = 25

for ix, num in enumerate(l1):
    if(num == val) :
        print(f"{val} found at {ix}")
        break


# while True :
#     print("choose 1,2 or 3")
#     sel = input("Choose")
#     if int(sel) == 3 :
#         break

l1 = ['.py','.js','.rb','.java','.c']
l2 = ['python','javascript','ruby','java','C']

tupled = tuple(zip(l1,l2))
print(tupled)
listed = list(zip(l1,l2))
print(listed)
setted = set(zip(l1,l2))
print(setted)
dictd = dict(zip(l1,l2))
print(dictd)
