class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil


    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return
        
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node


    def rotate_left(self, x):
        if x == self.nil or x.right == self.nil:
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:     # if y's left child isn't a leaf node
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:     # if x is the root node...
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        elif x == x.parent.right:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        if x == self.nil or x.left == self.nil:
            return
        y = x.left
        x.left = y.right
        if y.right != self.nil:     # if y's right child isn't a leaf node
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:     # if x is the root node...
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        elif x == x.parent.left:
            x.parent.left = y
        y.right = x
        x.parent = y