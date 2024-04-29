node_1="value"
#sets, unordered (hashed)
s1 = {1,2,False,4,"drew",None,node_1,5.0,5.0,2}
s2 = {1,2,3,4,5}
print(s1)
print(s1.add(2))
print(True in s1)
print(False in s1)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(type(s1))

for item in s1 :
    print(f"\t\t{item}")
