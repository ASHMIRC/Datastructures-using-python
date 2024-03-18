inorder


class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def inorder(root):
    if root:

        inorder(root.left)
        print(root.data)
        inorder(root.right)

root=node(40)
root.left=node(50)
root.right=node(60)
root.left.left=node(70)
root.left.right=node(80)
root.right.left=node(10)
inorder(root)
