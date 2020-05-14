#tuples (immutable), order maintained, like an array
t1 = (1,2,False,4,"drew",None,5.0,1)

print(t1)
print(t1[5])
print(type(t1))
print(t1[::-1])
print(len(t1))
print(t1.count(1))

for item in t1 :
    print(item)

t2 = ("^one",'^two',"^three")
print(t2)
one,two,three = t2
print(one,three)
