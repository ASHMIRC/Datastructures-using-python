
 '''Linked List 
 Insertend
 Insertfront
 Delete end
 Delete front'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
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

    def insertfront(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode

    def delfront(self):
        self.head=self.head.next

    def delend(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None


    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

l1=linkedlist()
l1.create()
l1.insertend(1)
l1.insertend(2)
l1.insertfront(6)
l1.delfront()
l1.delend()
l1.display()
