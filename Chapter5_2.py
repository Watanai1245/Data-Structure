class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return ''
        else:
            current, word = self.head, str(self.head.data)
            while current.next != None:
                word += '->' + str(current.next.data)
                current = current.next
            return word

    def str_reverse(self):
        if self.isEmpty():
            return ''
        else:
            current, word = self.tail, str(self.head.data)
            while current.previous != None:
                word += '->' + str(current.previous.data)
                current = current.previous
            return word

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return 0
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            node = Node(item)
            node.previous = current
            current.next = node
            self.tail = node
            self._size += 1

    def add_before(self,item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return 0
        else:
            node = Node(item)
            if self.size() == 1:
                node.next = self.tail
                self.tail.previous = node
                self.head = node
            else:
                node.next = self.head
                self.head.previous = node
                self.head = node
            self._size += 1

    def insert(self,pos,item):
        if pos > self.size() or pos <0:
            return print('Data cannot be added')

        if self.isEmpty():
            self.head = self.tail = Node(item)
            self._size += 1
            return print(f'index = {pos} and data = {item}')
        node = Node(item)

        if pos == 0:
            self._size +=1
            node.next = self.head
            self.head.previous = node
            self.head = node

        if pos == self.size():
            self._size += 1
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        current , index = self.head , 0

        while index != pos -1:
            index += 1
            current = current.next
        
        current.next.previous = node
        node.next = current.next
        node.previous = current
        current.next = node
        self._size += 1
        return print(f'index = {pos} and data = {item}')

    def size(self):
        return self._size

    def remove(self,item):
        if self.isEmpty():
            return print("Not Found!")
        current = self.head

        if self.size() == 1 and current.data == item:
            self.head = self.tail = None
            self._size -= 1
            return print(f'removed : {item} from index : 0')
        self._size -= 1

        if item == self.head.data:
            self.head = self.head.next
            self.head.previous = None
            return print(f'removed : {item} from index : 0')
        index = 0

        while current.next != None:
            if current.data == item:
                current.previous.next = current.next
                current.next.previous = current.previous
                return print(f'removed : {item} from index : {index}')
            index += 1
            current = current.next
        if current.data == item:
            self.tail = self.tail.previous
            self.tail.next = None
            return print(f'removed : {item} from index : {index}')
        self._size += 1
        return print('Not Found!')

if __name__ == '__main__':
    Inp = input('Enter Input : ').split(',')

    L = LinkedList()

    for a in Inp:
        a = a.split()
        if a[0] == 'A':
            L.append(a[1])
        elif a[0] == 'Ab':
            L.add_before(a[1])
        elif a[0] == 'I':
            L.insert(int(a[1].split(':')[0]),a[1].split(':')[1])
        elif a[0] == 'R':
            L.remove(a[1])
        print('linked list :',L)
        print('reverse :',L.str_reverse())