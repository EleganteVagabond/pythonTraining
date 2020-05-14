#Dictionaries (key/value)
d1 = {'name':"drew","course":"python",1:1}
print(d1)
print(d1["name"])
print(d1.get('name'))
print(d1[1])
print(d1.keys())
print(d1.values())
print(type(d1))

for k in d1 :
    print("key",k)

for k,v in d1.items() :
    print(k,"=",v)

dcpx = {'a':{'b':'bah','c':'cah'},
        'b':{'d':'dah','e':'eah'}
        }
print(dcpx)
print(dcpx['b'])

print(dcpx['b']['e'])
