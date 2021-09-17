class Stack:
    def __init__(self,ls=None):
        self.stack = []
        pass    
    def push(self,i):
        self.stack.append(i)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return self.size <= 0
    def size(self):
        return len(self.stack)
def postFixeval(st):
    s = Stack()
    for i in range(len(st)):
        if st[i] not in "+-/*":
            s.push(int(st[i]))
        else :
            temp = [s.pop(),s.pop()]
            if st[i] == '+':
                s.push(temp[1]+ temp[0])
            if st[i] == '-':
                s.push(temp[1] - temp[0])
            if st[i] == '*':
                s.push(temp[1] * temp[0])
            if st[i] == '/':
                s.push(temp[1] / temp[0])
    return s.pop()
print(" ***Postfix expression calcuation*** ")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))
