class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next

        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self) :
        s = ''
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail =p
        self.size += 1

    def push_front(self, data):
        if self.isEmpty():
            self.head = self.tail = self.Node(data)
        else:
            p = self.Node(data, self.head)
            self.head = p
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self) :
        return self.size == 0

    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def removeDup(self):
        if not self.isEmpty():
            mem = {}
            prev = None
            buffer = self.head
            while buffer is not None:
                if mem.get(buffer.data,0) == 0:
                    mem[buffer.data] = 1
                    prev = buffer
                    buffer = buffer.next
                else:
                    if buffer.next is not None:
                        prev.next = buffer.next
                        buffer.next = None
                        buffer = prev.next
                    else:
                        prev.next = None
                        buffer = None


    def contentEquivalence(self, other):
        if len(self) != len(other):
            return False

        s1 = str(self)
        s2 = str(other)

        a1 = []
        a2 = []

        a1 = s1.split()
        a2 = s2.split()

        a1 = sorted(a1) 
        a2 = sorted(a2) 
        
        return a1==a2



if __name__ == '__main__':
    splitted = input('List1,List2 : ').split(',')
    list1 = splitted[0].split()
    list2 = splitted[1].split()
    link1 = LinkedList()
    link2 = LinkedList()
    for item in list1:
        link1.append(item)
    for item in list2:
        link2.append(item)
    print('List1 content Equivalence List2 : '+str(link1.contentEquivalence(link2)))
