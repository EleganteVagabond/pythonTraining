class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data) + str(self.next)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''
        if isinstance(x,Node) :
            add = x
        else :
            add =Node(x)
        if self.head == None :
            self.head = self.tail = add
        else :
            self.tail.next = add
            self.tail = self.tail.next

    def __str__(self):
        ret = ""
        n = self.head
        while n != None :
            ret += "->"+str(n.data)
            n = n.next
        return ret

    def add_to_start(self, x):
        if isinstance(x,Node) :
            n = x
        else :
            n = Node(x)
        n.next = self.head
        self.head = n
        pass

    def search_val(self, x):
        '''return indices where x was found'''
        n = self.head
        ix = 0
        while n != None :
            if n.data == x :
                return ix
            n = n.next
            ix+=1

        return ix

    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        n = self.head
        p = None
        ix = 0
        while n != None :
            if ix == x :
                # there is some parent node. Otherwise it might be the head
                if p != None :
                    p.next = n.next
                    # need to update the tail pointer
                    if self.tail == n :
                        self.tail = p.next
                else :
                    # see if there is a new node to use as the head
                    if n.next != None :
                        self.head = n.next
                    # this means there is an empty list
                    else :
                        self.head = self.tail = None
                break
            p = n
            n = n.next
            ix+=1

    def length(self):
        '''return the length of the list, rep'd by number of nodes'''
        n = self.head
        cnt = 0
        while n != None :
            cnt += 1
            n = n.next
        return cnt

    def reverse(self) :
        self.reverse_list_recur(self.head,None)
        # just swap head/tail
        self.head = self.tail

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        if current != None :
            self.reverse_list_recur(current.next, current)
            current.next = previous
