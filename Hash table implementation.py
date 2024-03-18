class hashtable:
    def __init__(self):
        self.Max=100
        self.arr=[ None for i in range(self.Max)]
    def hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h % 200



    def add(self,key,val):
        h=self.hash(key)
        self.arr[h]=val
    def get(self,key):
        h=self.hash(key)
        return self.arr[h]
t=hashtable()
t.add('march 6',130)
print(t.arr)
print(t.get('march 6'))

