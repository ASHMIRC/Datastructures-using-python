'''Queue
enqueue
Dequeue'''

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class qlinkedlist:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        newNode=node(data)
        if self.front is None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode

    def dequeue(self):
        if self.front is None:
            print('the queue is empty')
        else:
            self.front=self.front.next

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

l1=qlinkedlist()
l1.enqueue(1)
l1.enqueue(3)
l1.dequeue()
l1.display()
