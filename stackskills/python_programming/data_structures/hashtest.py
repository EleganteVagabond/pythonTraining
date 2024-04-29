from .hashmap import HashMap

hm = HashMap()
hm.put("Test","Test")
print("1-",hm)
v = hm.get("Test")
print("2-",v)
hm.put("Test","Test2")
print ("3-",hm)
hm.put("tesT","Test3")
print ("4-",hm)
