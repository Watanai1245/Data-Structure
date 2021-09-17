class Queue:
    def __init__(self, ls = None):
        if ls == None: self.items = []
        else: self.items = ls
            
    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.isEmpty(): return
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
input_val = input("Enter people and time : ").split()
ls = [i for i in input_val[0]]
q0 = Queue(ls)
q1 = Queue()
q2 = Queue()
count1 = 0
count2 = 0
check = 0
for i in range(1, int(input_val[1]) + 1):
    item = ""
    if q0.isEmpty() == False: item += q0.dequeue()
    else: check += 1
    
    if i > 2:
        if count1 == 3: 
            q1.dequeue()
            count1 = 0
        if count2 == 2: 
            q2.dequeue()
            count2 = 0
            
    if q0.isEmpty() == False or check == 0:
        if q1.size() < 5: q1.enqueue(item)
        else: q2.enqueue(item)
    
    if q1.isEmpty() == False: count1 += 1
    if q2.isEmpty() == False: count2 += 1
    print(i, q0.items, q1.items, q2.items, sep = " ")
