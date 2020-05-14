from data_structures.linked_list import LinkedList, Node

ll = LinkedList()
for i in range (22) :
    ll.append_val(i)

print(ll)
print(ll.length())

ll.add_to_start(Node(-666))
print(ll)
print(ll.length())


ll.reverse()
print(ll)
print (ll.length())

ix =ll.search_val(13)
print(ix)

ll.remove_val_by_index(ix)
print(ll)
