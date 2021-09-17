class Stack:
    def __init__(self):
        self.stack = []
    def push(self,appended):
        self.stack.append(appended)
    def pop(self,i):
        return self.stack.pop(self.stack.index(i))
    def size(self):
        return len(self.stack)
    def getStack(self):
        return self.stack

def watchBack(input,stack):
    #Final = 0
    for i in input:
        if(i == 'B'):
            count = 0
            max = -1
            for j in stack.getStack()[len(stack.getStack())-1::-1]:

                if(max < j):
                    max = j
                    count += 1
            print(count)
        else:
            stack.push(int((i.split())[-1]))
        

myInput = input("Enter Input : ").split(',')
stack = Stack()
watchBack(myInput,stack)