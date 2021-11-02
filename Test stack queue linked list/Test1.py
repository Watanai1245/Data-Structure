class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self,value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def bottom(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def __str__(self):
        if not self.is_empty():
            out = "Data in Stack is : "
            for item in self.items:
                out += str(item)+' '
            return out
        return 'Empty'


if __name__ == '__main__':
    s1 = Stack()
    choice = int(input("Enter choice : "))
    if choice == 1:
        s1 = Stack()
        s1.push(10)
        s1.push(20)
        print(s1)
        s1.pop()
        s1.push(30)
        print("Peek of stack :",s1.peek())
        print("Bottom of stack :",s1.bottom())
    elif choice == 2:
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :",s1.is_empty())
    elif choice == 3:
        s1 = Stack()
        s1.push(11)
        s1.push(22)
        s1.push(33)
        s1.pop()
        print(s1)
        print("Stack size :",s1.size())