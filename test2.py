class Queue :
    def __init__ (self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def deQueue(self):
        if self.size() > 0:
            return self.item.pop(0)

    def size(self):
        return len(self.item)

    def str(self):
        return str(self.item)

    def isEmpty(self):
        return len(self.item) == 0

I = input('Enter people and time : ').split()
C1 = Queue()
C2 = Queue()
Cus = Queue()
C1.push(I[0])
C2.push(I[1])
Cus.push(I[2])
print(C1.item,C2.item,Cus.item)