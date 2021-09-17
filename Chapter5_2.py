class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.size == 0

    def append(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self.size += 1
            return

        new_tail = Node(item)
        old_tail = self.tail

        old_tail.next = new_tail
        new_tail.previous = old_tail
        
        self.tail = new_tail
        self.size += 1

    def addHead(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self.size += 1
            return
        
        new_head = Node(item)
        old_head = self.head

        new_head.next = old_head
        old_head.previous = new_head

        self.head = new_head
        self.size += 1

    def insert(self, pos, item):

        inserted_node = Node(item)
        if pos == 0:
            self.addHead(item)
            return
        if pos > 0:
            if pos >= self.size - 1:
                self.append(item)
                return
            else:
                node = self.head
                for _ in range(0,pos):
                    node = node.next

                previous_node = node
                next_node = previous_node.next

                previous_node.next = inserted_node
                inserted_node.previous = previous_node

                next_node.previous = inserted_node
                inserted_node.next = next_node
        else:
            if pos <= -self.size:
                self.addHead(item)
                return
            else:
                node = self.tail
                for _ in range(-1, pos-1, -1):
                    node = node.previous

                previous_node = node
                next_node = previous_node.next

                previous_node.next = inserted_node
                inserted_node.previous = previous_node

                next_node.previous = inserted_node
                inserted_node.next = next_node

        self.size += 1

    def search(self, item):
        node = self.head
        while node is not None:
            if node.value == item:
                return "Found"
            node = node.next
        return "Not Found"

    def index(self, item):
        index = 0
        node = self.head
        while node is not None:
            if node.value == item:
                return index
            node = node.next
            index += 1
        return -1

    def size(self):
        return self.size

    def pop(self, pos):
        if self.size-1 < pos or pos < 0:
            return "Out of Range"

        if self.size == 1:
            self.head = None
            self.tail = None

        elif pos == 0:
            print(f"l {self}")
            print("size "+ str(self.size))
            new_head = self.head.next
            new_head.previous = None

            self.head = new_head
            
        elif pos == self.size-1:
            new_tail = self.tail.previous
            new_tail.next = None

            self.tail = new_tail

        else:
            node = self.head
            for _ in range(0, pos):
                node = node.next

            previous_node = node.previous
            next_node = node.next

            if previous_node is not None:
                previous_node.next = next_node
                next_node.previous = previous_node

        self.size -= 1

        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())