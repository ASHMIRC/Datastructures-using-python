postorder

class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def postorder(root):
    if root:

        postorder(root.left)

        postorder(root.right)
        print(root.data)

root=node(40)
root.left=node(50)
root.right=node(60)
root.left.left=node(70)
root.left.right=node(80)
root.right.left=node(10)
postorder(root)
