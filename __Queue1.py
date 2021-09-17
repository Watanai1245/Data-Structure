class Queue :
    def __init__(self,list = None) :
        if(list == None):
            self.items = []
        else :
            self.items = list
    
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self): #ไม่ต้องใส่ค่าพารามิเตอร์เข้าไป เพราะเราต้องการให้มันส่งค่าออกมา
        return self.items.pop(0)
    
    def isEmpty(self): #เช็คว่ามีสมาชิกอยู่ใน Queue หรือไม่
        return self.items == []

    def size(self):
        return len(self.items)
         


q = Queue()

print(q.items)
q.enQueue("A") #เพิ่มคิว
print(q.items)
q.enQueue("B")
print(q.items)
q.enQueue("C")
print(q.items)

print(q.isEmpty())

print(q.size())

# print(q.deQueue()) #เอาคิวออก
# print(q.items)
# print(q.deQueue())
# print(q.items)
# print(q.deQueue())
# print(q.items)
# print(q.isEmpty())
