class Queue:
    def __init__(self, ls = None):
        self.count = 0
        self.count1 = 0
        if ls == None:
            self.items = []
        else:
            self.items = ls
        self.getTripleCharactor()
        
    def enqueue(self, val):
        self.items.append(val)
        return ("Add {} index is {}".format(val, len(self.items) - 1))

    def dequeue(self):
        return self.items.pop(0)

    def __str__ (self):
        self.items.reverse()
        if self.isEmpty(): return ("Empty")
        tmp = ""
        for i in range(self.size()):
            tmp += self.items[i][0]
        return tmp
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def getTripleCharactor(self):
        i = 0
        check = False
        while(True):
            if i < len(self.items) - 2:
                if self.items[i][0] == self.items[i+1][0] == self.items[i+2][0]:
                    if self.items[i][1] or self.items[i+1][1] or self.items[i+2][1]: self.count1 += 1
                    self.items.pop(i+2)
                    self.items.pop(i+1)
                    self.items.pop(i)
                    self.count += 1
                    check = True
                    i = -1
            if i == len(self.items) and check:
                i = 0
                check = False
            elif (i == len(self.items) and check == False) or self.size() < 3: break
            i += 1
    
class Stack:
    def __init__(self, ls = None):
        self.stack = []
        self.items = []
        self.count = 0
        if ls != None:
            for i in range(len(ls)):
                lsss = [ls[len(ls) - 1 - i], True]
                self.push(lsss)
        self.getTripleCharactor()
        self.items.reverse()

    def push(self, val): 
        self.stack.append(val)

    def pop(self):
        return self.items.pop()
    
    def __str__ (self):
        self.stack.reverse()
        if self.is_empty(): return ("ytpmE")
        tmp = ""
        for i in range(self.size()):
            tmp += self.stack[i][0]
        return tmp
        
    def size(self):
        return len(self.stack)
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def getTripleCharactor(self):
        i = 0
        check = False
        while(True):
            if i < self.size() - 2:
                if self.stack[i][0] == self.stack[i+1][0] == self.stack[i+2][0]:
                    self.items.append(self.stack[i])
                    self.stack.pop(i+2)
                    self.stack.pop(i+1)
                    self.stack.pop(i)
                    self.count += 1
                    check = True
                    i = -1
            if i == len(self.stack) and check:
                i = 0
                check = False
            elif (i == len(self.stack) and check == False) or self.size() < 3: break
            i += 1
    
inp = input("Enter Input (Normal, Mirror) : ").split()
s = Stack(inp[1])
ls_l = []
ls_l2 = []
ls_l3 = []
tmp = [0, 0, 0]
for i in range(len(inp[0])):
    if i < len(inp[0]) - 2:
        if inp[0][i] == inp[0][i+1] == inp[0][i+2]:
            ls_l2.append(i)
    lllll = [inp[0][i], False]
    ls_l.append(lllll)
ls_l3 = ls_l
for i in range(len(ls_l)):
    if tmp[0] <= len(ls_l2) - 1 and s.count > tmp[2]:
        if ls_l2[tmp[0]] == i:
            ls_l3.insert(i + 2 + tmp[0], s.pop())
            tmp[0] += 1
            tmp[2] += 1
q = Queue(ls_l)
print("NORMAL : \n{}".format(q.size()))
print(q)
print("{} Explosive(s) ! ! ! (NORMAL)".format(q.count - q.count1))
if q.count1 > 0: print("Failed Interrupted {} Bomb(s)".format(q.count1))
print("------------MIRROR------------\n: RORRIM\n{}".format(s.size()))
print(s)
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(s.count))