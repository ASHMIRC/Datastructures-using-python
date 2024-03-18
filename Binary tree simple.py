class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def insert(root,data):
        if root is None:
            return node(data)

        if data < root.data:
            root.left=insert(root.left,data)
        else:
            root.right=insert(root.right,data)
        return root
root=node(int(input()))
data=list(map(int,input("enter the ele: ").split()))

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
for i in data:
    insert(root, i)


inorder(root)

print("\n")
preorder(root)

print("\n ")
postorder(root)
