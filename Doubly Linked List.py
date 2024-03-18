'''Doubly Linked List
Insertend
Insertfront
Delete end
Delete front'''


class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None


    def create(self):
        li=list(map(int,input().split()))
        for i in li:
            self.insertend(i)


    def insertend(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp.data


    def insertfront(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.prev is None:
                newNode.next=temp
                temp.prev=newNode
                self.head=newNode


    def delfront(self):
        self.head=self.head.next
        self.head.prev=None

    def delend(self):
        prevv=None
        current=self.head
        while current.next is not None:
            prevv=current
            current=current.next
        prevv.next=None





    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next


l1=doublelinkedlist()
l1.create()
l1.insertend(2)
l1.insertfront(0)
l1.insertfront(3)
l1.delfront()
l1.delend()

l1.display()
