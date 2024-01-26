class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val

        if val > self.val and not self.right:
            self.right = BSTNode(val)
        elif val > self.val:
            self.right.insert(val)

        if val < self.val and not self.left:
            self.left = BSTNode(val)
        elif val < self.val:
            self.left.insert(val)


    # def insert(self, val):
    #     if not self.val:
    #         self.val = val
    #         return
        
    #     if self.val == val:
    #         return
        
    #     if val < self.val:
    #         if self.left:
    #             self.left.insert(val)
    #             return
    #         self.left = BSTNode(val)
    #         return
        
    #     if self.right:
    #         self.right.insert(val)
    #         return
    #     self.right = BSTNode(val)

    def get_min(self):
        min = self
        while min.left:
            min = min.left
        return min.val
    
    def get_max(self):
        max = self
        while max.right:
            max = max.right
        return max.val

    def delete(self, val):
        if not self.val:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if val == self.val:
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            if self.left and self.right:
                min_larger_node = self.right
                while min_larger_node.left:
                    min_larger_node = min_larger_node.left
                self.val = min_larger_node.val
                self.right = self.right.delete(min_larger_node.val)
        return self

    def preorder(self, visited):
        if self.val:
            visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited

    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        if self.val:
            visited.append(self.val)
        return visited

    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        if self:
            visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited

    def exists(self, val):
        if self and self.val == val:
            return True
        if self.left and val < self.val:
            return self.left.exists(val)
        if self.right and val > self.val:
            return self.right.exists(val)
        return False
    