Binary search tree  .Iterative method.


class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=node(data)
            return
        temp=self.root
        while True:
            if data<temp.data:
                if temp.left is None:
                    temp.left=node(data)
                    break
                temp=temp.left
            elif data>temp.data:
                if temp.right is None:
                    temp.right=node(data)
                    break
                temp=temp.right




    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)


b=bst()
b.insert(8)
b.insert(4)
b.insert(6)
b.inorder(b.root)
