from data_structures.binary_search_tree import BST


tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(6)
print(tree.flatten())
print("-"*40)

tree.delete_val(3)
assert tree.root.left == None
tree.delete_val(6)
assert tree.root.right == None
print("-"*40)

tree.insert(3)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(0)
tree.pre_order()
print("-"*40)

tree.delete_val(3)
tree.pre_order()
assert tree.root.left != None
assert tree.root.left.data == 4
assert tree.root.left.left.data != None
assert tree.root.left.left.data == 1

print("-"*40)

tree.insert(10)
tree.insert(7)
tree.insert(8)
tree.insert(6)
tree.insert(15)
tree.insert(12)
tree.insert(11)
tree.insert(13)
tree.insert(18)
tree.insert(20)
tree.pre_order()
print("-"*40)
tree.delete_val(8)
assert tree.root.right.left.right == None
tree.delete_val(18)
assert tree.root.right.right.right.data == 20
tree.delete_val(6)
assert tree.root.right.left.left == None
tree.delete_val(15)
assert tree.root.right.right.data == 12
assert tree.root.right.right.right.right.data == 20
tree.pre_order()
print("-"*40)

tree = BST()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("H")
tree.insert("E")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
print("-"*40)
tree.in_order()
# print("-"*40)
# tree.pre_order()
# print("-"*40)
# tree.post_order()
# print(tree.find_val("L"))
# print(tree.find_val("Z"))
# print("-"*40)
# tree.delete_val("Z")
# tree.delete_val("E")
# tree.in_order()
