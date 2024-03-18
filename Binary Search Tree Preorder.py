class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def bst(root,val):
    if root is None:
        return node(val)
    elif root.data>val:
        root.left=bst(root.left,val)
    elif root.data<val:
        root.right=bst(root.right,val)
    return root
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)

        preorder(root.right)
root=node(40)
n=int(input("enter the val: "))
for i in range(n):
    ele=int(input("enter the ele: "))
    bst(root,ele)
preorder(root)
