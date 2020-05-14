node_1 = "booger"
# List, like an array
l1 = [1,2,False,4,"drew",None,node_1,5.0]
print(l1)
print(l1[2])
print(type(l1))

lnum = [15,6,7,8,35,12,14,4,10,15]
lstr = ["cs","phy","ee","phil"]
print(f"sorted {sorted(lnum)}")
print(f"unsorted {lnum}")
lnum.sort()
print(f"sorted forever {lnum}")

print("ce" in lstr)
print(lstr.index("cs"))
print(len(lstr))
print(lstr[len(lstr)-1])
print(lstr[-1])
print(min(lstr))
print(max(lstr))
# adds this as an element
lstr.append(["ce","bus"])
print(lstr)
# merges a list of items into the calling list
lstr.extend(["ce","bus"])
print(lstr)
print(lstr.remove(["ce","bus"]))
print(lstr.pop())
print(lstr.pop(lstr.index("phil")))
print(lstr.pop())

print(4 in lnum)
print(min(lnum))
print(max(lnum))
print(lnum.append(15))
print(lnum.insert(4,69))
lnum[-1]=99
print(lnum)
print(lnum[4:-1])
print(lnum[:len(lnum)//2])
#step size
print(lnum[::len(lnum)//2])
# reverse the whole list
print(lnum[::-1])
print(lnum.count(15))

for item in lnum:
    print(f"-->{item}")

#print(dir(lstr))
