import string

class HashItem :

    def __init__(self,key,value,nxt = None):
        self.key = key
        self.value = value
        self.next = nxt

    def __str__(self) :
        return "{"+self.key+","+self.value+"}"

class HashMap :

    def __init__(self,s=10) :
        self.table = [None]*s

    def __str__(self) :
        ret = "["
        for v in self.table :
            ret += "[" + str(v)
            if isinstance(v,HashItem) :
                while v.next != None :
                    v = v.next
                    ret += ","+ str(v)
            ret += "]"
            ret += ","
        ret += "]"

        return ret

    def put(self,key,value):
        hi = HashMap.get(self,key)
        if hi == None :
            hi = HashItem(key,value)
            h = HashMap.hash(self,key)
            v = self.table[h]
            #doesn't exist
            if v == None :
                self.table[h] = hi
            # collision
            else :
                while v.next != None :
                    v = v.next
                v.next = hi
        else :
            hi.value = value


    def get(self, key) :
        v = self.table[HashMap.hash(self,key)]
        while v != None :
            if v.key == key:
                return v
            else :
                v = v.next
        return v


    def hash(self,key) :
        hv = 0
        for k in key :
            hv += ord(k)
        hv = hv % len(self.table)
        return hv
