'''Stack 
Push
Pop
Peek'''


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stacklinkedlist:
    def __init__(self):
        self.top=None
    def push(self,data):
        newNode=node(data)
        if self.top is  None:
            self.top=newNode
        else:
            temp=self.top
            while temp.next is not None:
                temp=temp.next
            temp.next=newNode
            newNode=temp

    def pop(self):
        if self.top is None:
            print('the stack is empty')
        else:
            temp=self.top
            yep=None
            while temp.next is not None:
                yep=temp
                temp=temp.next
            yep.next=None

    def peek(self):
        temp=self.top
        while temp.next is not None:
            temp=temp.next
        print(temp.data,end=" ")


    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


l1=stacklinkedlist()
l1.push(1)
l1.push(3)
l1.pop()
l1.peek()
l1.display()

