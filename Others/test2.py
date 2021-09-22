class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty(): return "reverse : "
        return "reverse : "+"->".join(str(i) for i in reversed(self.display()))


    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None: 
            self.addHead(item)
        else:
            current = self.head
            while current.next != None :
                current = current.next
            current.next = Node(item)
        

    def addHead(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        

    def search(self, item):
        current = self.head
        while current != None :
            if current.data == item :
                return 'Found'
            current = current.next
        if current == None :
            return 'Not Found'
            

    def index(self, item):
        current = self.head
        count = 0
        while current != None :
            if current.data == item :
                return count
            count += 1
            current = current.next
        if current == None :
            return '-1'
            
    def remove(self,item):
        current = self.head
        if current is not None :
            if current.data == item :
                self.head = current.next
                current = None
                return
        while current is not None :
            if current.data == item:
                break
            prev = current
            current = current.next
        if current == None:
            return
        prev.next = current.next
        current = None

    def size(self):
        current = self.head
        count = 0
        while current != None :
            current = current.next
            count += 1
        return count

   
    def pop(self, item):
        current = self.head
        if item == 0:
            if not self.isEmpty():
                self.head = self.head.next
                return "Success"
            else:
                return "Out of Range"
        else:
            previous = None
            index = 0
            while current is not None:
                if index == item:
                    previous.next = current.next
                    return "Success"
                index += 1
                previous = current
                current = current.next
            return "Out of Range"
            
        

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), i[3:]),end='')
        print(" in {}".format(L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1} ".format(k,L)))
print("Linked List :", L)