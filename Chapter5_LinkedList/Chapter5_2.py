class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def __str__(self):
        current = self.head.next
        string = ""
        while current is not self.tail:
            string += str(current.data) + " "
            current = current.next

        if string == "":
            return ""
        else:
            return "->".join(string.split())

    def str_reverse(self):
        current = self.tail.prev
        string = ""
        while current is not self.head:
            string += str(current.data) + " "
            current = current.prev

        if string == "":
            return ""
        else:
            return "->".join(string.split())

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        newNode = Node(data, self.tail.prev, self.tail)
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size += 1

    def insert(self, pos, data):
        if pos >= 0 and pos <= self.size:
            current = self.head
            for i in range(pos):
                current = current.next
            newNode = Node(data, current, current.next)
            current.next.prev = newNode
            current.next = newNode
            self.size += 1
        else:
            print("Data cannot be added")

    def remove(self, data):
        try:
            index = -1
            current = self.head
            while current.data != data:
                index += 1
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            print("removed : {} from index : {}".format(data, index))
        except AttributeError:
            print("Not Found!")

commanList = input("Enter Input : ").split(',')

DLL = DoublyLinkedList()
for i in commanList:
    A = i.split()[0]
    if A == "A":
        p = i.split()[1]
        DLL.append(p)

    elif A == "Ab":
        p = i.split()[1]
        DLL.insert(0, p)

    elif A == "I":
        p = i.split()[1]
        position, data = p.split(':')
        DLL.insert(int(position), data)
        if int(position) >= 0 and int(position) <= DLL.size:
            print("index = {} and data = {}".format(position, data))

    elif A == "R":
        p = i.split()[1]
        DLL.remove(p)

    print("linked list : {}".format(DLL))
    print("reverse : {}".format(DLL.str_reverse()))