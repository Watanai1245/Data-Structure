#การสร้าง queue แบบไม่ต้อใช้ list แต่ใช้ deque
from collections import deque
class Queue :
    def __init__ (self):
        self.items = deque('def')
    
    def enQueue (self,i):
        self.items.append(i)
    
    def deQueue(self): #ไม่ต้องใส่ค่าพารามิเตอร์เข้าไป เพราะเราต้องการให้มันส่งค่าออกมา
        return self.items.popleft() #ต่างจาก queue ธรรมดา เพราะสามารถเอาข้อมูลออกได้ทั้งทางหัวทางท้าย
    
    def isEmpty(self): #เช็คว่ามีสมาชิกอยู่ใน Queue หรือไม่
        return self.items == 0

    def size(self):
        return len(self.items)
         
d = Queue()
print(d.items)
d.enQueue('g')
d.enQueue('h')
print(d.items)
pop1 = d.deQueue()
pop2 = d.deQueue() 
print(d.items)
print(pop1,pop2)
print(len(d.items))