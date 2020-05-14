class Node:
    def __init__(self, key,value=None):
        self.left = self.right = None
        self.data = key
        self.value = value

    def __str__(self) :
        if self.value :
            return str(self.value)
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    @staticmethod
    def _get_node_for_key(key,value) :
        if isinstance(key,Node) :
            return key
        elif issubclass(type(value),Node) :
            return value
        else :
            return Node(key,value)

    def insert(self, key, value=None):
        if self.root == None :
            self.root = BST._get_node_for_key(key,value)
        else :
            self._insert(self.root,BST._get_node_for_key(key,value))

    def _insert(self, curr, node):
        if curr.data == node.data :
            return

        if node.data < curr.data :
            if curr.left :
                self._insert(curr.left,node)
            else :
                curr.left = node
        if node.data > curr.data :
            if curr.right:
                self._insert(curr.right,node)
            else :
                curr.right = node

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, curr):
        if curr :
            self._in_order(curr.left)
            print(curr)
            self._in_order(curr.right)

    def pre_order(self):
        '''root, left, right'''
        self._pre_order(self.root)

    def _pre_order(self, curr):
        if curr:
            print(curr)
            self._pre_order(curr.left)
            self._pre_order(curr.right)

    def post_order(self):
        '''left, right, root'''
        self._post_order(self.root)

    def _post_order(self, curr):
        if curr :
            self._pre_order(curr.left)
            self._pre_order(curr.right)
            print(curr)

    def flatten(self) :
        arr = [self.root]
        return self._flatten(self.root,arr)

    def _flatten(self,node,arr) :
        if node.left :
            arr.append(node.left)
            self._flatten(node.left,arr)

        if node.right :
            arr.append(node.right)
            self._flatten(node.right,arr)

        return arr

    def has_val(self, key):
        if isinstance(key,Node) :
            key = key.data
        return self._has_val(self.root,key)

    def _has_val(self, curr, key):
        if curr == None :
            return False
        if curr.data == key :
            return True
        if key < curr.data :
            return self._find_val(curr.left,key)
        else :
            return self._find_val(curr.right,key)

    def find_val(self, key):
        if isinstance(key,Node) :
            key = key.data
        return self._find_val(self.root,key)

    def _find_val(self, curr, key):
        if curr == None :
            return None
        if curr.data == key :
            return curr.value
        if key < curr.data :
            return self._find_val(curr.left,key)
        else :
            return self._find_val(curr.right,key)

    def delete_val(self, key):
        if isinstance(key,Node) :
            key = key.data
        self._delete_val(self.root,None,False,key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr  :
            if curr.data == key :
                if is_left :
                    # we can swap in either branch and still honor the rules
                    if curr.right :
                        prev.left = curr.right
                        n = curr.right
                        while n.left  :
                            n = n.left
                        # attach the left branch to the bottom of the left side of the right branch (confused yet?)
                        n.left = curr.left
                    else :
                        prev.left = curr.left
                else :
                    # we can swap in either branch and still honor the rules, just ctr
                    if curr.left :
                        prev.right = curr.left
                        n = curr.left
                        while n.right  :
                            n = n.right
                        # attach the right branch to the bottom of the right side of the left branch (confused yet?)
                        n.right = curr.right
                    else :
                        prev.right = curr.right

            elif curr.data > key :
                self._delete_val(curr.left,curr,True,key)
            else :
                self._delete_val(curr.right,curr,False,key)
