class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def create(root, n):
    if root is None:
        return node(n)
    else:
        temp = root
        temp1 = root
        flag = 0
        while True:
            if temp.left is None:
                temp.left = node(n)
                break
            elif temp.right is None:
                temp.right = node(n)
                break
            elif flag == 0:
                temp = temp1.left
                flag = 1
            else:
                temp = temp1.right
                flag = 0
                temp1 = temp1.left
        return root


def postorder(temp):
    if temp:

        postorder(temp.left)

        postorder(temp.right)
        print(temp.data)

root = None
while True:
    n = int(input("enter the val: "))
    if n > 0:
        root = create(root, n)
    else:
        break
postorder(root)
