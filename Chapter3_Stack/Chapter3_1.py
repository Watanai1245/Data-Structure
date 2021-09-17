class Stack():
    def __init__(self,list = None):
        if list == None:
            self.word = []
        else:
            self.word = list
        
    def push(self,i):
        self.word.append(i)

    def pop(self):
        return self.word.pop()

    def isEmpty(self):
        return self.word == []

    def size(self):
        return len(self.word)


s = Stack()
print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
for e in ls:
    s.push(e)

print(s.size(),"Data in stack : ",s.word)

while not s.isEmpty():
    s.pop()
print(s.size(),"Data in stack : ",s.word)